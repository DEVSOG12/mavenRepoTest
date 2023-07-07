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

        print(directory)

        # Check if Env variable is set
        if not os.environ.get("SOURCE_DATE_EPOCH"):
            os.environ["SOURCE_DATE_EPOCH"] = "315532800"

        # Change directory to the repo
        os.chdir(directory)


        # check if it has a setup.py file
        if not os.path.exists(os.path.join(directory, 'setup.py')):
            pass




        # Run reprotest in variations
        # First, run it with the default settings and check if the whl file is reproducible
        # If not, run it with the variations
        # If it is reproducible, return the variations that made it reproducible
        # If it is not reproducible, return the variations that made it not reproducible

        # +all reprotest --diffoscope-arg='--html=out.html' --variations=+all 'pip wheel . --no-deps
        # --no-build-isolation --no-clean -w ./dist' 'dist/*.whl'
        os.system("reprotest --diffoscope-arg='--html={}.html' --variations=+all 'pip wheel . --no-deps "
                  "--no-build-isolation --no-clean -w ./dist' 'dist/*.whl'".format(data[0]))

        possible_variations = ["environment", "build_path", "user_group.available+=builduser:builduser", "fileordering",
                               "home", "kernel", "locales", "exec_path", "time", "timezone", "umask" ]

        variations_reproducible = []
        variations_not_reproducible = []

        # Check if the whl file is reproducible
        if not os.path.exists(os.path.join(directory, "{}.html".format(data[0]))):
            os.system('rm -rf dist && rm {}.html'.format(data[0]))
            # If it is reproducible,
            return [True, "Reproducible"]
        else:
            os.system('rm -rf dist && rm {}.html'.format(data[0]))
            print("Not reproducible with +all")

            for variation in possible_variations:
                os.system("reprotest --diffoscope-arg='--html={}.html' --variations=-all,{} 'pip wheel . --no-deps "
                          "--no-build-isolation --no-clean -w ./dist' 'dist/*.whl'".format(data[0], variation))
                # Check if the whl file is reproducible
                if not os.path.exists(os.path.join(directory, "{}.html".format(data[0]))):
                    os.system('rm -rf dist && rm {}.html'.format(data[0]))
                    variations_reproducible.append(variation)
                else:
                    os.system('rm -rf dist && rm {}.html'.format(data[0]))
                    variations_not_reproducible.append(variation)
            return [False, "Not reproducible", variations_not_reproducible, variations_reproducible]
    else:
        return [False, "No repo", gitH[1]]


if __name__ == '__main__':
    # pickRandom(49)
    records = json.loads(open('data/records.json', 'r').read())

    # parse records a s a list
    records = [record.split(',') for record in records]
    print(records)

    for i in range(1):
        rep = check_whl_file(records[i])
        if rep[0]:
            records = json.loads(open('data/recordsTesting.json', 'r').read())
            records = records['results']
            records.append({
                "project": records[i][0],
                "status": "Fully Reproducible",
                "variationsNonReproducible": [],
                "variationsReproducible": ["all"]
                })
            analyze.write_json(records)
            print("Done with {}".format(records[i][0]))
        else:
            records = json.loads(open('data/recordsTesting.json', 'r').read())
            records = records['results']
            records.append({
                "project": records[i][0],
                "status": "Not Reproducible",
                "variationsNonReproducible": rep[2],
                "variationsReproducible": rep[3]
                })
            analyze.write_json(records)




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








