from pullData import *
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
            data = data[:1]
            runTests(data)
        else:
            data = data[:4]
            runTests(data)
