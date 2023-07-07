# from analyze import versionize, parseDiffoscopeOutput
# # Convert json to csv
#
# import json
#
# from analyze import versionize
# #
# # with open('data/records.json', 'r') as f:
# #     data = json.load(f)
# #
# #     print(len(data["results"]))
# #
# #     # create a csv file
# #     with open('data/records_300_n.csv', 'w') as f:
# #         f.write("name,status\n")
# #         data = data["results"]
# #         for record in data:
# #             print(record)
# #             f.write("{0},{1}\n".format(
# #                 record['project'],
# #                 record['gh_version']
# #             ))
#
# def run():
#
#     # Pull the project that had record['gh_version'] == "Reproducible"
#     # Re-add them to the queue and get their github link from the records.json file
#
#     records = json.loads(open('data/records.json', 'r').read())
#
#     pypiCSV = open('data/pypi_importantProj120k.csv', 'r').readlines()
#
#     # Get the list of projects that had record['gh_version'] == "Reproducible"
#     reproducible = [record['project'] for record in records['results'] if record['gh_version'] == "Reproducible"]
#
#     queue = []
#
#     for line in pypiCSV:
#         if line.split(',')[0] in reproducible:
#             queue.append(line)
#
#     # write the queue to the record file
#     with open('data/records.json', 'w') as f:
#         json.dump(queue, f)
#
#     # Get the github link of the projects in the queue
#
# run()
#
#
#
#
#
#
import json

records = json.loads(open('data/recordsTesting.json', 'r').read())
records = records['results']

print(records)
