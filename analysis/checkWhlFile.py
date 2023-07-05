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
    gitH = analyze.getRepoGH(data[1])

    if gitH[0]:
        # Add a line after the import in the setup.py file
        directory = gitH[1]

        # Check if Env variable is set
        if not os.environ.get("SOURCE_DATE_EPOCH"):
            os.environ["SOURCE_DATE_EPOCH"] = "315532800"

        # Build the wheel file
        os.system("cd " + directory + " && pip wheel . --no-deps --no-build-isolation --no-clean -w " + directory + "/dist")

        # Build the wheel again with differnt name
        os.system("cd " + directory + " && pip wheel . --no-deps --no-build-isolation --no-clean -w " + directory + "/dist2")

        # Name of the wheel file. top file in dir
        name = os.listdir(directory + "/dist")[0]

        # Compare the two wheel files
        os.system("diffoscope --exclude-directory-metadata=recursive" + " " + "--html output.html " + directory + "/dist/{} ".format(name) + directory + "/dist2/{}".format(name))

        # Use reprotest to check if the file is reproducible ignore zipinfo

        # os.system("reprotest --diffoscope-arg=\"--exclude-directory-metadata=recursive\" 'python3 setup.py bdist' 'dist/*.tar.gz'")

        # reprotest --diffoscope-arg="--exclude-directory-metadata=recursive" 'python3 setup.py bdist' 'dist/*.tar.gz'





        # check if the file is reproducible
        if os.path.exists("output.html"):
            return [False, "Not Reproducible", gitH[1] ,"NA"]

        else:
            return [True, "Reproducible", gitH[1], "NA"]

    else:
        return [False, "Error", "Not Determined", gitH[1]]


if __name__ == '__main__':
    # pickRandom(2)
    records = json.loads(open('data/records.json', 'r').read())
    print(len(records['queue']))
    # # for record in records['queue']:
    # # rep = check_whl_file(['google-ads-python', "https://github.com/googleads/google-ads-python"])
    # # print(rep)
    # #
    for record in records['queue']:
        rep = check_whl_file(record)
        if rep[0]:
            records = json.loads(analyze.read_json()[0])
            records["queue"].remove(record)
            records["results"].append({
                "project": record[0],
                "gh_version": rep[1],
                "status": rep[2],
                })
            analyze.write_json(records)
            print("Done with {}".format(record[0]))
        else:
            records = json.loads(analyze.read_json()[0])
            records["queue"].remove(record)
            records["results"].append({
                "project": record[0],
                "gh_version": rep[2],
                "status": rep[1],
                "error": rep[3]
                })
            analyze.write_json(records)
            print("Done with {}".format(record[0]))
    







