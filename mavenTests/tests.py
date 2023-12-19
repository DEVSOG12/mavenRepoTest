from importss import *
from processing import *


def regexRepoUrl(repository_url):
    # Regular expression to match different types of repository URLs
    url_pattern = re.compile(r"""
            (?:scm:git:|https?://|git@|git://)    # Match URL prefixes
            ([^\/:]+)                             # Match the domain or username (group 1)
            (?:\/|:)                              # Match slash or colon separator
            ([^\/]+)                              # Match the repository name (group 2)
            (?:\/(.*))?                           # Match optional path after the repository name (group 3)
        """, re.VERBOSE)

    # Match the URL components using the pattern
    match = url_pattern.match(repository_url)

    if match:
        # Extract matched components
        domain_or_username = match.group(1)
        repo_name = match.group(2)
        path = match.group(3) or ""

        # Format the URL for git clone command
        formatted_url = f"git clone {repository_url}"

        # Format the URL into a proper format if possible
        proper_format_url = f"https://{domain_or_username}/{repo_name}/{path.split('/')[0] if path else ''}"

        return [repo_name, path.split('/')[0] if path else ''], proper_format_url
    else:
        return None, None

def findArtifactMaven(directory):
    # Look for .jar files in the target folder if else loop to check other folders
    path = directory + "/target"
    f_path = None
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".jar"):
                    f_path = os.path.join(root, file)
                    return f_path
        return f_path
    else:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".jar"):
                    f_path = os.path.join(root, file)
                    return f_path
        return f_path




def reprotestRun(arg):
    # Reprotest
    print("Running Reprotest", f"reprotest --variations=+{arg[0]} 'mvn package -Dmaven.test.skip' 'target/{arg[1]}'")
    reproducible = subprocess.run(f"reprotest --variations=+{arg[0]} 'mvn package -Dmaven.test.skip' 'target/{arg[1]}'",
                                  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode != 0

    return {"variant": arg[0], "reproducible": reproducible}


def mvnBuildAndTest():
    variations_reproducible = []
    variations_not_reproducible = []
    variation_errors = []
    try:
        # print(os.getcwd())
        # Can build
        build = subprocess.run('mvn package -Dmaven.test.skip', shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).returncode == 0

        # Repotest
        if build:
            # print("Build Successful")
            # Find artifact
            artifact = findArtifactMaven(os.getcwd())

            if artifact is None:
                return [build, [False, variations_reproducible, variations_not_reproducible, variation_errors,
                                ], "No artifact found"]

            artifact = artifact.split("/")[-1]

            fullReproducible = subprocess.run("reprotest --variations=+all 'mvn package -Dmaven.test.skip' 'target/{}'".format(artifact),
                                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
            if fullReproducible:
                variations_reproducible.append("+all")
                return [build, [fullReproducible, variations_reproducible, variations_not_reproducible, variation_errors]]

            possible_variations = ["environment", "fileordering", "home", "kernel", "locales", "exec_path", "time",
                                   "timezone", "umask"]

            possible_variations = [[item, artifact] for item in possible_variations]

            results = runMProcessWithReturn(possible_variations, reprotestRun)
            for result in results:
                if result["reproducible"]:
                    variations_reproducible.append(result["variant"])
                else:
                    variations_not_reproducible.append(result["variant"])

            return [build, [fullReproducible, variations_reproducible, variations_not_reproducible, variation_errors], "Full Reproducible" if fullReproducible or len(variations_not_reproducible) == 0 else "Partially Reproducible" if len(variations_reproducible) > 0 else "Not Reproducible"]
        else:
            return [build, [False, variations_reproducible, variations_not_reproducible, variation_errors], "Build Failed"]

    except Exception as e:
        print(e)
        return [False, [False, variations_reproducible, variations_not_reproducible, variation_errors], "Error"]
        # backToBase()

def pomFileFix(directory):
    path = directory + "/pom.xml"
    if os.path.exists(path):
        with open(path, "r") as f:
            data = f.read()
        """
        Enable Reproducible Builds mode for plugins, by adding project.build.outputTimestamp property to the project's pom.xml:
        <properties>
         <project.build.outputTimestamp>2023-01-01T00:00:00Z</project.build.outputTimestamp>
        </properties>
        
        https://maven.apache.org/guides/mini/guide-reproducible-builds.html
        """
        # check if the properties tag already exists
        if "<properties>" not in data:
            data = data.replace("<project>", "<project>\n<properties>\n<project.build.outputTimestamp>2023-01-01T00:00:00Z</project.build.outputTimestamp>\n</properties>")
        else:
            # check if the project.build.outputTimestamp already exists
            if "<project.build.outputTimestamp>" not in data:
                data = data.replace("</properties>", "<project.build.outputTimestamp>2023-01-01T00:00:00Z</project.build.outputTimestamp>\n</properties>")
        with open(path, "w") as f:
            f.write(data)

        return directory
    else:
        return False
def runReTests(data):
    result = runMProcessWithReturn(data, runReTest)
    print("Results", result)
    inform({"title": "Maven", "text": f"Finished testing {len(result)} repositories"})

    return 0 if len(result) > 1 else False

def runReTest(item):
    if subprocess.run('mvn --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode != 0:
        print("Maven is not installed")
        exit(1)

    # Clone
    if subprocess.run('git clone ' + item[1] + ' ' + item[0], shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE).returncode != 0:
            print("Git clone failed")
            exit(1)

    # cd into the folder
    os.chdir(item[0])

    # Find all pom.xml files
    possiblePaths = findAllPomSubFolders(os.getcwd())

    # print(possiblePaths)

    if len(possiblePaths) == 0:
        print("No pom.xml found")
        backToBase(item[0])
        exit(1)

    path = runMProcessWithReturn(possiblePaths, pomFileFix)

    path = [item for item in path if item is not False]

    if len(path) == 0:
        print("No pom.xml found")
        backToBase(item[0])
        exit(1)

    results = runMProcessWithReturn(path, changeDirAndRun)

    postResultsToFile("//Users/devsog12/mavenRepoTest/mavenTests/data/results/maven_results_afterFix.json", {"repo": item[1], "results": results})

    # Go back to base
    backToBase(item[0])

    return results






def runTests(data):
    result = runMProcessWithReturn(data, runTest)
    print("Results", result)
    inform({"title": "Maven", "text": f"Finished testing {len(result)} repositories"})

    return len(result)



def postResultsToFile(path, data):
    # print(os.getcwd().split())
    with open(path, "r") as f:
        datas = json.load(f)

    datas["results"].append(data)

    with open(path, "w") as f:
        json.dump(datas, f, indent=4)


def inform(info):
    requests.post("https://api.pushcut.io/Fsoe_07fAhA2C93wwGT77/notifications/MyNotification",
                  json={"text": info["text"], "title": info["title"]},
                  headers={"Content-Type": "application/json"})


def backToBase(repodir):

    # if os.getcwd().split("/")[-1] == repodir:
    os.chdir("..")
    # delete the folder

    shutil.rmtree(repodir)
    print("Deleted", repodir)


def changeDirAndRun(path):
    os.chdir(path)
    return mvnBuildAndTest()


def runTest(item):
    if subprocess.run('mvn --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode != 0:
        print("Maven is not installed")
        exit(1)

    # Clone
    if subprocess.run('git clone ' + item[1] + ' ' + item[0], shell=True, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE).returncode != 0:
        print("Git clone failed")
        exit(1)

    # cd into the folder

    os.chdir(item[0])

    # Find all pom.xml files
    possiblePaths = findAllPomSubFolders(os.getcwd())
    if len(possiblePaths) ==   0:
        print("No pom.xml found")
        backToBase(item[0])
        exit(1)

    results = runMProcessWithReturn(possiblePaths, changeDirAndRun)

    postResultsToFile("/home/osolarin/mavenRepoTest/mavenTests/data/results/maven_results_afterFix.json", {"repo": item[1], "results": results})

    # Go back to base
    backToBase(item[0])

    # i

    return results


def fixRepos(data=None):
    def repoValid(data):
        repoUrl = data[1]
        url = "https://api.github.com/repos/" + regexRepoUrl(repoUrl)[0][0] + "/" + regexRepoUrl(repoUrl)[0][1]
        headers = {'Authorization': 'token ' + 'ghp_2'}
        response = requests.get(url, headers=headers)
        return [data[0], data[1]] if response.status_code == 200 else None

    dataFixed = []

    for item in data:
        # print(item[1])
        dataFixed.append([item[0], regexRepoUrl(item[1])[1]])
        # Each item is a Map item of repository data
        # if repoValid(item["url"]):
        #     validationTest(item)`

    dataFixed = [item for item in dataFixed if item[1] is not None]

    # def T()
    dataFixed = runMProcessWithReturn(dataFixed, repoValid)

    dataFixed = [item for item in dataFixed if item is not None]

    # create csv file with dataFixed
    with open('data/raw/maven_sample_5000Fixed.csv', 'w') as outfile:
        csvWriter = csv.writer(outfile)
        csvWriter.writerow(["repoName", "repoUrl"])
        for item in dataFixed:
            csvWriter.writerow(item)

    return dataFixed


def validationTest(repoData):
    pass


def findAllPomSubFolders(repoPath):
    paths = []
    # print(repoPath)
    for root, dirs, files in os.walk(repoPath):
        for file in files:
            if file.endswith("pom.xml"):
                # print(root)
                paths.append(root)
    # find all pom.xml files
    # print(paths)
    return paths

