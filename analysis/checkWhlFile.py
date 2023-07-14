import os

import analyze
import json


def pickRandom(n):
    i = 0
    while i < n:
        if analyze.randomProject():
            print("Success")
            i += 1
        else:
            print("Failed")


def getLineStartPoint(path):
    # Given the path for the setup.py file, return the line number where the the last import statement is
    with open(path, 'r') as f:
        lines = f.readlines()
        f.close()
    k = []
    for i in range(len(lines)):
        if lines[i].startswith("import"):
            k.append(i)

    return (k[-1] if len(k) > 0 else 1) + 1


def check_whl_file(data):
    try:
        gitH = analyze.getRepoGH(data["url"])
    except Exception as e:
        print("No repo")
        print(e)
        return [False, "No repo"]

    if gitH[0]:
        # Add a line after the import in the setup.py file
        directory = gitH[1]

        print(directory)

        # Check if Env variable is set
        # if not os.environ.get("SOURCE_DATE_EPOCH"):
        #     os.environ["SOURCE_DATE_EPOCH"] = "315532800"

        # Change directory to the repo
        os.chdir(directory)

        # check if it has a setup.py file
        if not os.path.exists(os.path.join(directory, 'setup.py')):
            pass

        # check if the project has a diffoscopeLogs folder

        # create project folder in diffoscopeLogs
        if not os.path.exists(os.path.join(directory,
                                           "/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs/{}".format(
                                                   data["project"]))):
            os.system("mkdir /home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs/{}".format(data["project"]))
        else:
            pass

        # Run reprotest in variations
        # First, run it with the default settings and check if the whl file is reproducible
        # If not, run it with the variations
        # If it is reproducible, return the variations that made it reproducible
        # If it is not reproducible, return the variations that made it not reproducible

        # +all reprotest --diffoscope-arg='--html=out.html' --variations=+all 'pip wheel . --no-deps
        # --no-build-isolation --no-clean -w ./dist' 'dist/*.whl'

        possible_variations = ["environment", "build_path", "user_group.available+=builduser:builduser", "fileordering",
                               "home", "kernel", "locales", "exec_path", "time", "timezone", "umask"]

        variations_reproducible = []
        variations_not_reproducible = []

        try:
            code = os.system(
                "reprotest --diffoscope-arg='--html=/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs/{}/all.html' --variations=+all 'pip wheel . --no-deps "
                "--no-build-isolation --no-clean -w ./dist' 'dist/*.whl'".format(data["project"]))
            print("Exit Code: ", code)

            # Check if the whl file is reproducible
            if not os.path.exists(os.path.join(directory,
                                               "/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs/{}/all.html".format(
                                                       data["project"]))) and code == 0:
                # If it is reproducible,
                return [True, "Reproducible"]
            else:
                print("Not reproducible with +all")

                for variation in possible_variations:
                    kcode = os.system(
                        "reprotest --diffoscope-arg='--html=/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs/{}/{}.html' --variations=-all,"
                        "{} 'pip wheel . --no-deps "
                        "--no-build-isolation --no-clean -w ./dist' 'dist/*.whl'"
                        .format(data["project"], variation, variation))

                    print("Exit Code ({}): ".format(variation), kcode)

                    # Check if the whl file is reproducible
                    if not os.path.exists(
                            os.path.join(directory, "/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs/"
                                                    "{}/{}.html".format(data["project"], variation))):
                        variations_reproducible.append(variation)
                    else:
                        variations_not_reproducible.append(variation)
                return [False, "Not reproducible", variations_not_reproducible, variations_reproducible]
        except Exception as e:
            print("Error from body of code smh: ", e)
            return [False, "Not repo", variations_not_reproducible, variations_reproducible]
    else:
        print("wahala repo")
        return [False, "No repo", gitH[1]]


if __name__ == '__main__':
    # pickRandom(49)
    records = json.loads(open('data/pypi_python_620.json', 'r').read())

    # parse records a s a list
    records = records['data']
    print(records)
    i = 0
    while len(json.loads(open('/home/osolarin/ReproducibleTests/analysis/data/recordsTestingPlainAfterEpoch.json', 'r').read())[
                  'results']) < 400:
        rep = check_whl_file(records[i])
        # Change directory to main directory
        # os.system("cd ../..")

        if rep[0]:
            record = json.loads(
                open('/home/osolarin/ReproducibleTests/analysis/data/recordsTestingPlainAfterEpoch.json', 'r').read())
            record = record['results']
            record.append({
                "project": records[i]["project"],
                "stars": records[i]["stars"],
                "status": "Fully Reproducible",
                "variationsNonReproducible": [],
                "variationsReproducible": ["all"]
            })
            print(record)
            analyze.write_json({"results": record})
            print("Done with {}".format(records[i]["project"]))
        else:
            if rep[1] == "No repo":
                i += 1
                continue
            record = json.loads(
                open('/home/osolarin/ReproducibleTests/analysis/data/recordsTestingPlainAfterEpoch.json', 'r').read())
            record = record['results']
            record.append({
                "project": records[i]["project"],
                "stars": records[i]["stars"],
                "status": "Not Reproducible",
                "variationsNonReproducible": rep[2],
                "variationsReproducible": rep[3]
            })
            print(record)
            analyze.write_json({"results": record})
            print("Done with {}".format(records[i]["project"]))
        i += 1

    # print(len(records['queue']))
    # # # for record in records['queue']:
    # # # rep = check_whl_file(['google-ads-python', "https://github.com/googleads/google-ads-python"])
    # # # print(rep)
    # # #

    # for record in records['queue']:
    #     rep = check_whl_file(record)
    #     if rep[0]:
    #         records = json.loads(analyze.read_json()[0])
    #         records["queue"].remove(record)
    #         records["results"].append({
    #             "project": record[0],
    #             "gh_version": rep[1],
    #             "status": rep[2],
    #             })
    #         analyze.write_json(records)
    #         print("Done with {}".format(record[0]))
    #     else:
    #         records = json.loads(analyze.read_json()[0])
    #         records["queue"].remove(record)
    #         records["results"].append({
    #             "project": record[0],
    #             "gh_version": rep[2],
    #             "status": rep[1],
    #             "error": rep[3]
    #             })
    #         analyze.write_json(records)
    #         print("Done with {}".format(record[0]))
