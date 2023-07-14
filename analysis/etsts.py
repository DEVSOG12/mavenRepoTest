# from analyze import versionize, parseDiffoscopeOutput

import json
# import requests

# def tranform():
#     rep = ["awscli-plugin-endpoint", "aws-cdk-aws-cloudtrail", "webrtcvad", "gast", "upb-lib", "simple-term-menu", "gapic-google-cloud-logging-v2", "branca", "bertopic", "grafana-api", "word2vec", "technopy", "logger-bundle", "makefun", "azure-cognitiveservices-search-websearch", "split-folders", "connected-components-3d", "papermill", "lorem", "pyshac", "bytecode", "astral", "myo", "jsonpickle", "stackprinter", "docxbuilder", "edalize", "pymartini", "mypy-boto3-network-firewall", "azure-cli-backup", "python-pcre", "cfn-flip", "django-admin-multiple-choice-list-filter", "exchange-calendars", "easytrader", "flashday", "grpc-google-cloud-pubsub-v1", "resnest", "tfhelper", "ory-hydra-client", "selenium-base", "tencentcloud-sdk-python-taf", "mistletoe", "runai", "baymax", "urlextract", "minisom", "behave-pandas", "ulid2", "mkdocs-git-committers-plugin", "samsungtvws", "proactive", "django-pandas", "pydmxcontrol", "pymilvus", "vk-api", "oschmod", "bebi103", "cloudtools", "mypy-boto3-ec2", "pytest-flask", "download", "capy", "mypy-boto3-athena", "pythondata-cpu-rocket", "socketio-client", "nxpd", "data-converter", "qiskit-terra", "aws-cdk-aws-cloud9", "pygmsh", "pytest-custom-exit-code", "tencentcloud-sdk-python-iir", "sbvirtualdisplay", "rest-condition", "django-map-widgets", "tencentcloud-sdk-python-ecm", "articledateextractor", "insightface", "django-token", "tox-travis", "fcm-django", "python-gmaps", "wechaty-grpc", "django-feature-policy", "cprint", "django-oscar", "av", "aiohttp-json-api", "mkdocs-macros-plugin", "django-angular", "flake8-gl-codeclimate", "speak2mary", "pbd", "flow-network", "citeproc-py-styles", "stix2-patterns", "django-sso-app", "mkdocs-minify-plugin", "fuzzyfinder", "python-easyconfig", "mypy-boto3-elastictranscoder", "collections-extended", "feincms3", "javaobj-py3", "pyshorteners", "s3contents", "transmission-rpc", "pyminknow", "stone", "pytricia", "pkgconfig", "djangocms-installer", "tableaudocumentapi", "fatpack", "falcon-apispec", "zlhawq", "sobol-seq", "picmistandard", "museval", "dgl-cu101", "utlz", "azure-cognitiveservices-search-nspkg", "circuitbreaker", "azure", "peewee", "validx", "flake8-eradicate", "tencentcloud-sdk-python-tem", "django-db-readonly", "pyobjc-framework-fileproviderui", "snuggs", "ppscore", "vdms", "awscliv2", "linecache2", "dynamicforms", "trio-asyncio", "pytest-rerunfailures", "compressive-transformer-pytorch", "pym2149", "ldapdomaindump", "django-pizza", "jupyterlab-widgets", "kaggler", "pyzbar", "saspy", "opentelemetry-semantic-conventions", "quantum-gateway", "mypy-boto3-ssm-contacts", "ai", "twitterapi", "firexapp", "tencentcloud-sdk-python-tsw", "structlog-sentry", "django-registration", "pygments-markdown-lexer", "dyn", "pygeohash", "pyproject-parser", "pandas-alive", "textgenrnn", "nosecomplete", "kglobal", "aws-cdk-aws-codeartifact", "awslimitchecker", "b3j0f-utils", "zookeeper", "bit", "robotframework-assertion-engine", "datacube", "mypy-boto3-pinpoint-email", "pytgcalls"]
#     n = []
#     # Pull slug from pypi_importantProj120k.csv
#     with open('data/pypi_importantProj120k.csv', 'r') as f:
#         # Check if slug is in rep list
#         for line in f:
#             if line.split(",")[0] in rep:
#                 # If yes, aadd to list
#                 n.append(line)
#     print(n)
#
# tranform()
#
# # #

# with open('data/records.json', 'r') as f:
#     records = json.load(f)
#     for i in range(len(records)):
#         # curl - -silent
#         # 'https://api.github.com/repos/jasonrudolph/keyboard' - H
#         # 'Accept: application/vnd.github.preview' | jq
#         # '.watchers_count'
#         #

#         headers = {'Accept': 'application/vnd.github.preview', 'Authorization': 'Bearer '
#                                                                                 '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'}

#         print(records[i].split(",")[2])
#         k = records[i].split(",")[2].split("/")[-2]
#         j = records[i].split(",")[2].split("/")[-1]

#         # remove \n from j
#         j = j[:-1]

#         url = "https://api.github.com/repos/" + "{}/{}".format(k, j)
#         print(url)
#         reqs = requests.get(url, headers=headers)
#         print(reqs.status_code)
#         print(reqs.json())
#         try:
#             print(reqs.json()['stargazers_count'])
#             nRec = json.loads(open('data/B_records.json', 'r').read())
#             nRec["data"].append({
#                 "project": records[i].split(",")[0],
#                 "url": records[i].split(",")[1],
#                 "stars": reqs.json()['stargazers_count']
#             })
#         except:
#             print("No star")
#             nRec = json.loads(open('data/B_records.json', 'r').read())
#             nRec["data"].append({
#                 "project": records[i].split(",")[0],
#                 "url": records[i].split(",")[1],
#                 "stars": -1
#             })

#         with open('data/B_records.json', 'w') as f:
#             json.dump(nRec, f)
#         print("Done with {}".format(records[i].split(",")[0]))




# # curl -ni "https://api.github.com/search/repositories?q=more+useful+keyboard" -H 'Accept: application/vnd.github.preview'

# with open('data/pypi_python_620.json', 'r') as f:
#     records = json.load(f)

#     print(len(records['data']))

#     # Make a distrubution of number of distinct projects


