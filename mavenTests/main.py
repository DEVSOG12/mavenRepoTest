from pullData import *
from tests import runTests, fixRepos, runReTests


if '__main__' == __name__:
    data = run()
    if not data:
        print("No data found")
        exit(1)
    else:
        data = runFixed()

        # if not data:
        #     fixRepos(data)
        #     data = runFixed()
        #     data = data[:1]
        #     runTests(data)
        # else:
        #     data = data[:4]
        #     runTests(data)

        results = pullResults()

        if results:
            results = results["results"]
            results = [[item["repo"][::-1][0:8], item["repo"]] for item in results]
            # test on 1
            # results = results[:1]
            # print(results[0])
            runReTests(results)


