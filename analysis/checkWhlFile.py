import os

import analyze
import json
def pickRandom(n):
    for i in range(n):
        analyze.randomProject()

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
        directory = gitH[2]

        # edit the setup.py file and add:
        # Line 1: import os and Line 2: os.environ["SOURCE_DATE_EPOCH"] = "315532800"
        with open(directory + "/setup.py", 'r') as f:
            lines = f.readlines()
            num = getLineStartPoint(directory + "/setup.py")
            lines.insert(num, "import os\n")
            lines.insert(num + 1, 'os.environ["SOURCE_DATE_EPOCH"] = "315532800"\n')
            f.close()
        with open(directory + "/setup.py", 'w') as f:
            f.writelines(lines)
            f.close()

        # Build the wheel file
        os.system("cd " + directory + " && pip wheel . --no-deps --no-build-isolation --no-clean -w " + directory + "/dist")

        # Build the wheel again with differnt name
        os.system("cd " + directory + " && pip wheel . --no-deps --no-build-isolation --no-clean -w " + directory + "/dist2")

        # Name of the wheel file. top file in dir
        name = os.listdir(directory + "/dist")[0]

        # Compare the two wheel files
        os.system("diffoscope --exclude-directory-metadata=recursive" + " " + "--html output.html " + directory + "/dist/{} ".format(name) + directory + "/dist2/{}".format(name))

        # check if the file is reproducible
        if os.path.exists("output.html"):
            return [False, "Not Reproducible", gitH[1] ,"NA"]

        else:
            return [True, "Reproducible", gitH[1], "NA"]

    else:
        return [False, "Error", "Not Determined", gitH[1]]


if __name__ == '__main__':
    # pickRandom(90)
    records = json.loads(open('data/records.json', 'r').read())
    print(len(records['queue']))
    # for record in records['queue']:
    # rep = check_whl_file(['google-ads-python', "https://github.com/googleads/google-ads-python"])
    # print(rep)

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








