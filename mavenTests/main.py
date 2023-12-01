from pullData import run, runFixed
from tests import runTests, fixRepos


if '__main__' == __name__:
    data = run()
    if not data:
        print("No data found")
        exit(1)
    else:
        data = runFixed()

        if not data:
            fixRepos(data)
            data = runFixed()
            runTests(data)
        else:
            runTests(data)
