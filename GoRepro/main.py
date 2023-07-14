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
        repo = Repo.clone_from(repoInfo[1], '/Users/oreofe/Projects/test/reproducibleTests/GoRepro/data/repos/{}'.format(repoInfo[0].replace("/", "_")))
    except Exception as e:
        print("Could not clone the repo", e)
        return [False, "No repo"]



    # Check if the repo has a diffoscopeLogs folder
    if not os.path.exists('/Users/oreofe/Projects/test/reproducibleTests/GoRepro/data/diffoscopeLogs{}'.format(resultFileName)):
        os.mkdir('/Users/oreofe/Projects/test/reproducibleTests/GoRepro/data/diffoscopeLogs{}'.format(resultFileName))


    if not os.path.exists('/Users/oreofe/Projects/test/reproducibleTests/GoRepro/data/diffoscopeLogs{}/{}'.format(resultFileName, repoInfo[0].replace("/", "_"))):
        os.mkdir('/Users/oreofe/Projects/test/reproducibleTests/GoRepro/data/diffoscopeLogs{}/{}'.format(resultFileName, repoInfo[0].replace("/", "_")))

    # Change directory to the repo
    os.chdir('/Users/oreofe/Projects/test/reproducibleTests/GoRepro/data/repos/{}'.format(
        repoInfo[0].replace("/", "_"), repoInfo[0].replace("/", "_")))

    # Run the test
    command = "reprotest --diffoscope-arg='--html=/Users/oreofe/Projects/test/reproducibleTests/GoRepro/" \
              "data/diffoscopeLogs{}/{}/all.html' --variations=+all "\
              "\"go build -mod=mod -modcacherw -ldflags '-s -w -extldflags=-Z' -trimpath -o dist/bin\" "\
              "'dist/*'".format(resultFileName, repoInfo[0])
    print(command)
    exit_code = os.system(command)

    print("Exit Code: ", exit_code)


if __name__ == "__main__":
    # pull_repos()
    # fixStars()
    with open('data/go_Random400.json', 'r') as f:
        data = json.load(f)
        print(len(data['data']))

        for i in range(1):
            testGoReproducible([data['data'][i]['project'], data['data'][i]['url']], "go_Random400")


