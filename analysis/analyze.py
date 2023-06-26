import json
import os
import random
from git import Repo
import requests
import subprocess

def read_csv():
    with open(os.path.join(os.path.dirname(__file__), 'data/pypi_importantProj120k.csv'), 'r') as f:
        return f.readlines()

def read_json():
    with open(os.path.join(os.path.dirname(__file__), 'data/records.json'), 'r') as f:
        return f.readlines()

def write_json(data):
    with open(os.path.join(os.path.dirname(__file__), 'data/records.json'), 'w') as f:
        json.dump(data, f)

def parseDiffoscopeOutput(output):
    # Parse the output of diffoscope and return a list of files that are different
    # If there is no difference, return an empty list

    # Split the output by new line
    output = output.split('\n')

    # Get the index of the line that starts with "├──"
    files_index = [i for i in range(len(output)) if output[i].startswith("├──")]

    # Get file name by checking the last part of the line with / split
    files = [output[i].split('/')[-1] for i in files_index] if files_index else []

    # print(files)
    return files

def versionize(stringversion):
    # Convert the version string to the format of x.x.x where x is a digit
    # If the version string is not in the format of x.x.x, return False
    if not any(char.isdigit() for char in stringversion):
        return [False, "No digit found",]
    else:
        # remove all non-digit characters except for .
        stringversion = ''.join([i for i in stringversion if i.isdigit() or i == '.'])

        return [True, stringversion]

def getMainFolder(path):
    # Get the folder that has __init__.py in it
    folders = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]

    for folder in folders:
        if '__init__.py' in os.listdir(os.path.join(path, folder)):
            return [True, os.path.join(path, folder)]
        else:
            return [False, "No __init__.py found",]


def getRepoGH(link):
    # Download the repo from github

    #add a :@ before github
    link = link.replace('github', ':@github')


    try:
        Repo.clone_from(link, os.path.join(os.path.dirname(__file__), 'data/repos/{0}/github_{0}'.format(link.split('/')[-1])))

        # Get the version number from setup.py in the repo
        version = None
        name = None
        try:
            with open(os.path.join(os.path.dirname(__file__), 'data/repos/{0}/github_{0}/setup.py'.format(link.split('/')[-1])), 'r') as f:
                setup = f.readlines()
                try:
                    version = [i for i in setup if i.strip().startswith("version")][0].split('=')[1].strip().replace("'", "")
                except Exception as e:
                    print(e)
                    print("No version found in setup.py")
                    return [False, "No version found in setup.py", ]

                # Check if version has  a digit in it
                if not any(char.isdigit() for char in version):
                    ifname = getMainFolder(os.path.join(os.path.dirname(__file__), 'data/repos/{0}/github_{0}'.format(link.split('/')[-1])))
                    if (ifname is list) and ifname[0]:
                        name = ifname[1].split('/')[-1]
                        # Load the version directly from __init__.py module

                        with open(os.path.join(os.path.dirname(__file__), 'data/repos/{0}/github_{0}/{1}/__init__.py'.format(link.split('/')[-1], name)), 'r') as f:
                            init = f.readlines()
                            version = [i for i in init if '__version__' in i][0].split('=')[1].strip().replace("'", "")
                    else:
                        print("No version found after checking __init__.py")
                        return [False, "No version found after checking __init__.py", ]
        except Exception as e:
            print(e)
            print("No setup.py found")
            return [False, "No setup.py found", ]

        return [True, version, os.path.join(os.path.dirname(__file__), 'data/repos/{0}/github_{0}'.format(link.split('/')[-1]))]

    except Exception as e:
        print("Could not clone the repo")
        print(e)
        return [False, "Could not clone the repo"]

def getRepoPyPi(name, link):
    # https: // pypi.org / simple
    req_uri = "https://pypi.org/simple/{0}/".format(name)

    # Download the repo from pypi
    try:
        r = requests.get(req_uri)
        # Extract the links from the html
        links = [i.split('"')[1] for i in r.text.split('\n') if 'href=' in i]
        # filter list for tar.gz
        links = [i for i in links if '.tar.gz' in i]

        # Get version number of latest release by sorting the list and getting the last element
        version = links[-1].split('/')[-1].split('.tar.gz')[0]

        latest_version_link = [i for i in links if version in i][0]

        version_number = version.split('-')[-1]

        # Download the tar.gz file
        r = requests.get(latest_version_link)
        with open(os.path.join(os.path.dirname(__file__), 'data/repos/{0}/pypi_{0}_{1}.tar.gz'.format(link.split('/')[-1], version_number)), 'wb') as f:
            f.write(r.content)

        # Extract the tar.gz file
        os.system("mkdir {1}-{2} && tar -xzf {0} -C {1}-{2} --strip-components 1".format(os.path.join(os.path.dirname(__file__), 'data/repos/{0}/pypi_{0}_{1}.tar.gz'.format(link.split('/')[-1], version_number)), link.split('/')[-1], version_number))

        # Remove the tar.gz file
        os.system("rm {0}".format(os.path.join(os.path.dirname(__file__), 'data/repos/{0}/pypi_{0}_{1}.tar.gz'.format(link.split('/')[-1], version_number))))

        # Move the extracted folder to the repo folder
        os.system("mv {0} {1}".format(os.path.join(os.path.dirname(__file__), '{0}-{1}'.format(link.split('/')[-1], version_number)), os.path.join(os.path.dirname(__file__), 'data/repos/{0}/pypi_{0}'.format(link.split('/')[-1]))))


        return [True, version_number, os.path.join(os.path.dirname(__file__), 'data/repos/{0}/pypi_{0}'.format(link.split('/')[-1]))]

    except Exception as e:
        print("Could not fetch PyPi Source")
        print(e)
        return [False, "Could not fetch PyPi Source"]


def randomProject():
    # k = input("1 == Stats, 2 == Process, 3 == Pick \n")

    k = 3

    # match k:
    #     case "1":
    #         print("Stats")
    #         records = json.loads(read_json()[0])
    #         print("Number of projects in queue: " + str(len(records["queue"])))
    #         for i in records["queue"]:
    #             print(i)
    #         print("Number of projects in processed: " + str(len(records["completed"])))
    #         for i in records["completed"]:
    #             print(i)
    #
    #     case "2":
    #         records = json.loads(read_json()[0])
    #         print("Select a project to push as completed")
    #         for i in records["queue"]:
    #             print(i)
    #         k = input("Project: ")
    #         if k in records["queue"]:
    #             records["queue"].remove(k)
    #             records["completed"].append(k)
    #             write_json(records)

        # case "3":
    rand = random.randint(1, len(read_csv()))

    records = json.loads(read_json()[0])

    print(records)
    if read_csv()[rand].split(',')[0] in records:
        print("Already Selected")
        pass
    else:
        print("Selecting: " + read_csv()[rand].split(',')[0])
        print("Details: " + read_csv()[rand].split(',')[0] + " " + read_csv()[rand].split(',')[1])
        records["queue"].append(read_csv()[rand].split(',')[0])
        write_json(records)
        return list(read_csv()[rand].split(',')[0:2])

        # case _:
        #     print("Invalid input")


def main():
    project = randomProject()
    gh = getRepoGH(project[1])
    pypi = getRepoPyPi(project[0], project[1])

    if gh[0] and pypi[0]:
        print("Success: Fetched PyPi and GH")
        # Run diffoscope on the two folders
        if versionize(gh[1])[0] == versionize(pypi[1])[0]:
            print("Same version found", versionize(gh[1])[1])
            try:
                output = subprocess.check_output("diffoscope --exclude-directory-metadata=recursive {0} {1}".format(gh[2], pypi[2]), shell=True)
            except subprocess.CalledProcessError as e:
                output = e.output.decode('utf-8')

            print("Output:" + "\n" + output)

            # Remove the project from the queue and report status "results"
            records = json.loads(read_json()[0])
            records["queue"].remove(project[0])
            result = {"project": project[0], "gh_version": gh[1], "pypi_version": pypi[1], "status": "Success", "diffoscope:": " ".join(parseDiffoscopeOutput(output)), "error": "NA"}
            records["results"].append(result)
            write_json(records)

        else:
            print("Different version")
            print("GH: " + str(gh[1]))
            print("PyPi: " + str(pypi[1]))

            # Remove the project from the queue and report status "results"
            records = json.loads(read_json()[0])
            records["queue"].remove(project[0])
            result = {"project": project[0], "gh_version": gh[1], "pypi_version": pypi[1], "status": "Failed","diffoscope:": "NA", "error": "Version Mismatch"}
            records["results"].append(result)
            write_json(records)

    elif gh[0] and not pypi[0] or not gh[0] and pypi[0]:
        print("Failed due to one of the sources not being fetched")
        print("GH: " + str(gh))
        print("PyPi: " + str(pypi))

        # Remove the project from the queue and report status "results"
        records = json.loads(read_json()[0])
        records["queue"].remove(project[0])
        result = {"project": project[0], "gh_version": versionize(gh[1])[0] if versionize(gh[1])[0] else "Failed", "pypi_version": versionize(gh[1])[0] if versionize(gh[1])[0] else "Failed", "status": "Failed", "diffoscope:": "NA", "error": "GH: " + gh[1] if not gh[0] else "Not Error from GithHub" + " PyPi: " + pypi[1] if not pypi[0] else "Not Error from PyPi"}
        records["results"].append(result)
        write_json(records)

    else:
        print("Failed")
        print("GH: " + str(gh))
        print("PyPi: " + str(pypi))

        # Remove the project from the queue and report status "results"
        records = json.loads(read_json()[0])
        records["queue"].remove(project[0])
        result = {"project": project[0], "gh_version": versionize(gh[1])[0] if versionize(gh[1])[0] else "Failed", "pypi_version": versionize(gh[1])[0] if versionize(gh[1])[0] else "Failed", "status": "Failed", "diffoscope:": "NA", "error": "GH: " + gh[1] if not gh[0] else "Not Error from GithHub" + " PyPi: " + pypi[1] if not pypi[0] else "Not Error from PyPi"}
        records["results"].append(result)
        write_json(records)




if __name__ == "__main__":
    n = input("Number of projects to run: ")
    for i in range(int(n)):
        print("Running project: " + str(i))
        main()


