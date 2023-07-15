import requests
import json
from git import Repo
import os


def fixStars():
    with open('data/sh.json', 'r') as f:
        data = json.load(f)
        print(len(data['results']))

        for item in range(len(data['results'])):
            if data['results'][item]['stars'] == -1:
                print("Fixing {}".format(data['results'][item]['project']))
                url = "https://libraries.io/api/search?api_key=141f39abc3f98e29647df1b93f02afaf&languages=Python&q=" \
                      "{}&platforms".format(data['results'][item]['project']) + "=Pypi"
                try:
                    response = requests.get(url)
                    datal = response.json()
                    star = datal[0]['stars'] if len(datal) > 0 else -1

                    data['results'][item]['stars'] = star
                    print(star)
                except:
                    print("Error")
                    data['results'][item]['stars'] = -1

        with open('data/sh.json', 'w') as outfile:
            json.dump(data, outfile)



def pull_repos():
    # https://libraries.io/search?languages=Go&order=desc&platforms=Go&sort=stars
    page = 1


    resources = []

    while len(resources) < 100:
        url = "https://libraries.io/api/search?api_key=141f39abc3f98e29647df1b93f02afaf&languages=Python&order=desc&page=" \
              "{}&platforms".format(page) + "=Pypi&sort=stars"
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

    with open('data/pypi_Top100.json', 'w') as outfile:
        final = {"data": resources}
        json.dump(final, outfile)


def testGoReproducible(repoInfo, resultFileName):
    # sudo  reprotest "go build -mod=mod -modcacherw -ldflags '-s -w -extldflags=-Z' -trimpath -o dist/bin" dist/*

    # Clone the repo
    possible_variations = ["environment", "build_path", "user_group.available+=builduser:builduser", "fileordering",
                           "home", "kernel", "locales", "exec_path", "time", "timezone", "umask"]

    variations_reproducible = []
    variations_not_reproducible = []

    try:
        repo = Repo.clone_from(repoInfo[1], '/home/osolarin/ReproducibleTests/GoRepro/data/repos/{}'.format(repoInfo[0].replace("/", "_")))
    except Exception as e:
        print("Could not clone the repo", e)
        return [False, "No repo"]



    # Check if the repo has a diffoscopeLogs folder
    if not os.path.exists('/home/osolarin/ReproducibleTests/GoRepro/data/diffoscopeLogs{}'.format(resultFileName)):
        os.mkdir('/home/osolarin/ReproducibleTests/GoRepro/data/diffoscopeLogs{}'.format(resultFileName))


    if not os.path.exists('/home/osolarin/ReproducibleTests/GoRepro/data/diffoscopeLogs{}/{}'.format(resultFileName, repoInfo[0].replace("/", "_"))):
        os.mkdir('/home/osolarin/ReproducibleTests/GoRepro/data/diffoscopeLogs{}/{}'.format(resultFileName, repoInfo[0].replace("/", "_")))

    # Change directory to the repo
    os.chdir('/home/osolarin/ReproducibleTests/GoRepro/data/repos/{}'.format(
        repoInfo[0].replace("/", "_"), repoInfo[0].replace("/", "_")))

    # Run the test
    command = "sudo reprotest --diffoscope-arg='--html=/home/osolarin/ReproducibleTests/GoRepro/" \
              "data/diffoscopeLogs{}/{}/all.html' --variations=+all "\
              "\"go build -mod=mod -modcacherw -ldflags '-s -w -extldflags=-Z' -trimpath -o dist/bin\" "\
              "'dist/*'".format(resultFileName, repoInfo[0].replace("/", "_"))
    print(command)
    exit_code = os.system(command)

    print("Exit Code: ", exit_code)

    if exit_code == 0:
        # Its reproducible
        record = json.loads(
            open('/home/osolarin/ReproducibleTests/GoRepro/data/{}.json'.format(resultFileName), 'r').read())["results"]
        record.append({
            "project": repoInfo[0],
            "stars": repoInfo[2],
            "status": "Fully Reproducible",
            "variationsNonReproducible": [],
            "variationsReproducible": ["all"]
        })
        print(record)
        with open('/home/osolarin/ReproducibleTests/GoRepro/data/{}.json'.format(resultFileName), 'w') as f:
            json.dump({"results": record}, f)
        return [True, "Fully Reproducible"]
    else:
        # Try all other variations
        for variation in possible_variations:
            command = "sudo reprotest --diffoscope-arg='--html=/home/osolarin/ReproducibleTests/GoRepro/" \
                      "data/diffoscopeLogs{}/{}/all.html' --variations=+{} " \
                      "\"go build -mod=mod -modcacherw -ldflags '-s -w -extldflags=-Z' -trimpath -o dist/bin\" " \
                      "'dist/*'".format(resultFileName, repoInfo[0].replace("/", "_"), variation)
            print(command)
            exit_code = os.system(command)
            if exit_code == 0:
                variations_reproducible.append(variation)
            else:
                variations_not_reproducible.append(variation)

        # Record the results
        record = json.loads(
            open('/home/osolarin/ReproducibleTests/GoRepro/data/{}.json'.format(resultFileName), 'r').read())["results"]
        record.append({
            "project": repoInfo[0],
            "stars": repoInfo[2],
            "status": "Partially Reproducible" if len(variations_reproducible) > 0 else "Not Reproducible",
            "variationsNonReproducible": variations_not_reproducible,
            "variationsReproducible": variations_reproducible
        })

        print(record)

        with open('/home/osolarin/ReproducibleTests/GoRepro/data/{}.json'.format(resultFileName), 'w') as f:
            json.dump({"results": record}, f)

        return [True, "Partially Reproducible" if len(variations_reproducible) > 0 else "Not Reproducible"]


if __name__ == "__main__":
    # pull_repos()
    # fixStars()
    with open('data/go_Random400.json', 'r') as f:
        data = json.load(f)
        print(len(data['data']))

        for i in range(0, len(data['data'])):
            if not testGoReproducible([data['data'][i]['project'], data['data'][i]['url'], data['data'][i]['stars']], "go_Random400Results"):
                continue


