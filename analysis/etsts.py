from analyze import versionize, parseDiffoscopeOutput
# Convert json to csv

import json

from analyze import versionize

with open('data/records.json', 'r') as f:
    data = json.load(f)

    print(len(data["results"]))

    # create a csv file
    with open('data/records_third.csv', 'w') as f:
        f.write("name,gh_version,pypi_version,status,diffoscope,error\n")
        data = data["results"]
        for record in data:
            print(record)
            f.write("{0},{1},{2},{3},{4}, {5}\n".format(
                record['project'],
                versionize(record['gh_version'])[1] if versionize(record['gh_version'])[0] else record['gh_version'],
                versionize(record['pypi_version'])[1] if versionize(record['pypi_version'])[0] else record[
                    'pypi_version'],
                record['status'],
                record['diffoscope:'] if record['diffoscope:'] != "NA" else "Error",
                record['error']

            ))

#
# output = """
# --- /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/github_wireless
# +++ /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/pypi_wireless
# ├── file list
# │ @@ -1,11 +1,8 @@
# │ -.git
# │ -.gitignore
# │ -.travis.yml
# │  LICENSE
# │  MANIFEST.in
# │ +PKG-INFO
# │  README.md
# │  setup.cfg
# │  setup.py
# │ -tests
# │ -tox.ini
# │ -wireless
# │ +wireless
# │ +wireless.egg-info
# │   --- /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/github_wireless/README.md
# ├── +++ /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/pypi_wireless/README.md
# │ @@ -95,12 +95,12 @@
# │  First, install `pandoc` so that setup.py can auto-convert Markdown syntax into reStructuredText:
# │
# │  ```bash
# │  sudo apt-get install pandoc
# │  sudo pip install pypandoc
# │  ```
# │
# │ -Then, following [this guide](https://packaging.python.org/tutorials/packaging-projects/), push the project to PyPI:
# │ +Then, following [this guide](http://peterdowns.com/posts/first-time-with-pypi.html), push the project to PyPI:
# │
# │  ```bash
# │ -python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# │ +sudo python setup.py sdist upload -r pypi
# │  ```
# │   --- /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/github_wireless/setup.cfg
# ├── +++ /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/pypi_wireless/setup.cfg
# │ @@ -1,2 +1,8 @@
# │  [metadata]
# │  description-file = README.md
# │ +
# │ +[egg_info]
# │ +tag_build =
# │ +tag_date = 0
# │ +tag_svn_revision = 0
# │ +
# │   --- /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/github_wireless/setup.py
# ├── +++ /Users/oreofe/Projects/test/reproducibleTests/analysis/data/repos/wireless/pypi_wireless/setup.py
# │ @@ -12,24 +12,25 @@
# │
# │  setup(
# │      name='wireless',
# │      version='0.3.3',
# │      description='A dead simple, cross-platform Python library to connect to ' +
# │      'wireless networks.',
# │      long_description=long_description,
# │ +    long_description_content_type='text/markdown',
# │      url='https://github.com/joshvillbrandt/wireless',
# │      author='Josh Villbrandt',
# │      author_email='josh@javconcepts.com',
# │ -    license=open('LICENSE').read(),
# │ +    # license=open('LICENSE').read(),
# │      packages=['wireless'],
# │ -    setup_requires=[
# │ -        'tox',
# │ -        'nose',
# │ -        'flake8',
# │ -        'packaging'
# │ -    ],
# │ -    install_requires=[
# │ -    ],
# │ -    scripts=[],
# │ -    test_suite='tests',
# │ -    zip_safe=False
# │ +    # setup_requires=[
# │ +    #     # 'tox',
# │ +    #     # 'nose',
# │ +    #     # 'flake8',
# │ +    #     # 'packaging'
# │ +    # ],
# │ +    # install_requires=[
# │ +    # ],
# │ +    # scripts=[],
# │ +    # # test_suite='tests',
# │ +    # zip_safe=False
# │  )
#
# """
#
# parseDiffoscopeOutput(output)
