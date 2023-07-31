from multiprocessing import Pool

import requests
import json
import os
from git import Repo

possible_variations = ["environment", "build_path", "user_group", "fileordering",
                       "home", "kernel", "locales", "exec_path", "time", "timezone", "umask"]

def run_reprotest(variation):
    command = "sudo reprotest --variations=+{} " \
              "npm pack --pack-destination='./dest'" \
              "'dest/*.tgz'".format(variation)
    print(command)
    exit_code = os.system(command)
    return [True, variation] if exit_code == 0 else [False, variation]


def pull_repos():
    # https://libraries.io/search?languages=Go&order=desc&platforms=Go&sort=stars
    page = 1

    resources = []

    while len(resources) < 400:
        url = "https://libraries.io/api/search?api_key=141f39abc3f98e29647df1b93f02afaf&languages=JavaScript&&page=" \
              "{}&platforms".format(page) + "=NPM"
        response = requests.get(url)
        data = response.json()
        for item in data:
            if str(item['repository_url']).startswith("https://github.com"):
                d = {
                    "project": item['name'],
                    "url": item['repository_url'],
                    "stars": item['stars'],
                }
                resources.append(d)

        page += 1
        print(url)
        print(len(resources))

    with open('data/npm_400.json', 'w') as outfile:
        final = {"data": resources}
        json.dump(final, outfile)


def runTest():
    with open('data/npm_400.json', 'r') as f:
        records = json.load(f)['data']
        f.close()

    for record in records:
        # print(record)
        name = record['project']
        url = record['url']
        stars = record['stars']

        # Clone the repo
        try:
            Repo.clone_from(url, name)

        except:
            print("Error cloning repo")

        # change directory
        os.chdir(name)

        os.system("mkdir dest")

        # run reprotest

        exit_code = os.system("reprotest --variation=+environment,fileordering,locales,exec_path,time,timezone,umask 'npm pack --pack-destination='./dest'' 'dest/*.tgz'")

        if exit_code == 0:
            # Fully Reproducible
            print("Fully Reproducible")
            record = json.loads(
                open('/home/osolarin/ReproducibleTests/NPMTest/data/NPMTest_400_res.json', 'r').read())[
                "results"]
            record.append({
                "project": name,
                "stars": stars,
                "status": "Fully Reproducible",
                "variationsNonReproducible": [],
                "variationsReproducible": ["all"]
            })

            with open('/home/osolarin/ReproducibleTests/NPMTest/data/NPMTest_400_res.json', 'w') as f:
                json.dump({"results": record}, f)
        else:
            # Try all other variations
            variations_reproducible = []
            variations_not_reproducible = []

            # Use multiprocessing to run reprotest commands in parallel
            pool = Pool()
            results = pool.starmap(run_reprotest,
                                   [variation for variation in possible_variations])
            pool.close()
            pool.join()

            for result in results:
                if result[0]:
                    variations_reproducible.append(result[1])
                else:
                    variations_not_reproducible.append(result[1])

            # Record the results
            record = json.loads(
                open('/home/osolarin/ReproducibleTests/NPMTest/data/NPMTest_400_res.json', 'r').read())[
                "results"]
            record.append({
                "project": name,
                "stars": stars,
                "status": "Partially Reproducible" if len(variations_reproducible) > 0 else "Not Reproducible",
                "variationsNonReproducible": variations_not_reproducible,
                "variationsReproducible": variations_reproducible
            })

            print(record)

            with open('/home/osolarin/ReproducibleTests/NPMTest/data/NPMTest_400_res.json', 'w') as f:
                json.dump({"results": record}, f)


       

if __name__ == '__main__':
    # pull_repos()
    runTest()
