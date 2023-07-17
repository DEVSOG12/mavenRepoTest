from git import Repo
import os
import json


def runWhlTest(repoInfo, resultFile):

    if not os.environ.get("SOURCE_DATE_EPOCH"):
        os.environ["SOURCE_DATE_EPOCH"] = "315532800"

    print("Running whl test for {}".format(repoInfo[0]))

    possible_variations = ["environment", "build_path", "user_group.available+=builduser:builduser", "fileordering",
                           "home", "kernel", "locales", "exec_path", "time", "timezone", "umask"]

    variations_reproducible = []
    variations_not_reproducible = []

    # Clone the repo
    try:
        repo = Repo.clone_from(repoInfo[1], '/home/osolarin/ReproducibleTests/analysis/data/whlTest/{}'.format(repoInfo[0]))
    except Exception as e:
        print("Could not clone the repo", e)
        return [False, "No repo"]

    # Check if the repo has a setup.py file
    if not os.path.exists(
            os.path.join('/home/osolarin/ReproducibleTests/analysis/data/whlTest/{}'.format(repoInfo[0]), 'setup.py')):
        return [False, "No setup.py file"]

    # Check if the repo has a diffoscopeLogs folder
    if not os.path.exists('/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs{}'.format(resultFile)):
        os.mkdir('/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs{}'.format(resultFile))


    if not os.path.exists('/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs{}/{}'.format(resultFile,repoInfo[0])):
        os.mkdir('/home/osolarin/ReproducibleTests/analysis/data/diffoscopeLogs{}/{}'.format(resultFile,repoInfo[0]))

    # Change directory to the repo
    os.chdir('/home/osolarin/ReproducibleTests/analysis/data/whlTest/{}'.format(repoInfo[0]))

    # Run the test
    exit_code = os.system("reprotest --diffoscope-arg='--html=/home/osolarin/ReproducibleTests/analysis/data"
                          "/diffoscopeLogs{}/{}/all.html' --variations=+all 'pip wheel . --no-deps "
                          "--no-build-isolation --no-clean -w ./dist' 'dist/*.whl'".format(resultFile, repoInfo[0]))

    print("Exit Code: ", exit_code)

    # Check if the whl file is reproducible
    if exit_code == 0:
        # Its reproducible
        record = json.loads(
            open('/home/osolarin/ReproducibleTests/analysis/data/{}.json'.format(resultFile), 'r').read())["results"]
        record.append({
            "project": repoInfo[0],
            "stars": repoInfo[2],
            "status": "Fully Reproducible",
            "variationsNonReproducible": [],
            "variationsReproducible": ["all"]
        })
        print(record)
        with open('/home/osolarin/ReproducibleTests/analysis/data/{}.json'.format(resultFile), 'w') as f:
            json.dump({"results": record}, f)
        return [True, "Fully Reproducible"]
    else:
        # Try all other variations
        for variation in possible_variations:
            exit_code = os.system("reprotest --diffoscope-arg='--html=/home/osolarin/ReproducibleTests/analysis/data"
                                  "/diffoscopeLogs{}/{}/{}.html' --variations=+{} 'pip wheel . --no-deps "
                                  "--no-build-isolation --no-clean -w ./dist' 'dist/*.whl'".format(resultFile, repoInfo[0],
                                                                                                    variation,
                                                                                                    variation))
            if exit_code == 0:
                variations_reproducible.append(variation)
            else:
                variations_not_reproducible.append(variation)

        # Record the results
        record = json.loads(
            open('/home/osolarin/ReproducibleTests/analysis/data/{}.json'.format(resultFile), 'r').read())["results"]
        record.append({
            "project": repoInfo[0],
            "stars": repoInfo[2],
            "status": "Partially Reproducible",
            "variationsNonReproducible": variations_not_reproducible,
            "variationsReproducible": variations_reproducible
        })

        print(record)

        with open('/home/osolarin/ReproducibleTests/analysis/data/{}.json'.format(resultFile), 'w') as f:
            json.dump({"results": record}, f)

        return [True, "Partially Reproducible"]





if __name__ == '__main__':
    name = input("Dataset name: ")
    k = int(input("Number of projects: "))
    finalizeName = input("Finalize name: ")

    dataset = json.loads(open("/home/osolarin/ReproducibleTests/analysis/data/{}.json".format(name), 'r').read())[
        "data"]

    numberOfProjects = k
    k = len(dataset) - 1
    while len(json.loads(open("/home/osolarin/ReproducibleTests/analysis/data/{}.json".format(finalizeName), 'r').read())[
                  "results"]) < numberOfProjects and k > 0:
        success = runWhlTest([dataset[k]["project"], dataset[k]["url"], dataset[k]["stars"]], finalizeName)
        if success[0]:
            print("Success", dataset[k]["project"])
        else:
            print("Failed", dataset[k]["project"])
        k -= 1
