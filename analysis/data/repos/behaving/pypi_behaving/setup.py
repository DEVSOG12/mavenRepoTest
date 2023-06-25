# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['behaving',
 'behaving.mail',
 'behaving.notifications',
 'behaving.notifications.gcm',
 'behaving.personas',
 'behaving.sms',
 'behaving.web',
 'behaving.web.steps']

package_data = \
{'': ['*']}

install_requires = \
['behave>=1.2.6,<2.0.0',
 'parse>=1.19.0,<2.0.0',
 'selenium>=4,<5',
 'splinter>=0.18.1,<0.19.0']

entry_points = \
{'console_scripts': ['gcmmock = behaving.notifications.gcm.mock:main',
                     'mailmock = behaving.mail.mock:main',
                     'smsmock = behaving.sms.mock:main']}

setup_kwargs = {
    'name': 'behaving',
    'version': '3.1.5',
    'description': 'BDD Behavior-Driven-Development testing',
    'long_description': '# behaving\n\n[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ggozad/behaving/ci.yml)](https://github.com/ggozad/behaving/actions/workflows/ci.yml)\n[![PyPI](https://img.shields.io/pypi/v/behaving)](https://pypi.org/project/behaving/)\n[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/behaving/behaving)](https://hub.docker.com/repository/docker/behaving/behaving)\n\n_behaving_ is a web application testing framework for\nBehavior-Driven-Development, based on\n[behave](http://pypi.python.org/pypi/behave) and\n[splinter](https://github.com/cobrateam/splinter).\n\n_behave_ is written in Python and is similar to\n[Cucumber](http://cucumber.io/).\n_behaving_ adds the step-libraries for multi-user web/email/sms/gcm\ninteractions, and provides the Python _behaving_ namespace so that\nindependent step-libraries can work together.\n\nPlease refer to _behave_\'s excellent\n[documentation](http://behave.readthedocs.io/en/latest/) for a guide on\nhow to use it, how to write your custom steps and make it possible to\nextend _behaving_.\n\n## Hello world\n\nStarting to use _behaving_ is pretty easy. Inside some python module,\nadd your _features_ consisting each of one or more scenarios. These\nfeatures are Gherkin language files with an extension of `.feature`. In\nthe same directory you should have a steps module which imports the\n_behaving_ steps as well as your own custom steps (more on that later in\nthe setup\\_ section) . Here\'s a basic example:\n\n```gherkin\nFeature: Text presence\n\n    Background:\n        Given a browser\n\n    Scenario: Search for BDD\n        When I visit "http://www.wikipedia.org/"\n        And I fill in "search" with "BDD"\n        And I press "go"\n        Then I should see "Behavior-driven development" within 5 seconds\n```\n\n## Email, SMS & GCM (Google Cloud Messaging)\n\nWhile the web is the focus of _behaving_, it also includes simple mocks\nfor a mail, SMS and a GCM server. These come with a small collection of\nsteps allowing you to do things like:\n\n```gherkin\nFeature: Email & SMS\n\n    Scenario: Click link in an email\n        Given a browser\n        When I send an email to "foo@bar.com" with subject "Hello" and body "Try out this website at http://google.com"\n        And I click the link in the email I received at "foo@bar.com"\n        Then the browser\'s URL should be "http://google.com/"\n\n    Scenario: Receive SMS with body\n        When I send an sms to "+4745690001" with body "Hello world"\n        Then I should receive an sms at "+4745690001" containing "world"\n\n    Scenario: Receive GCM Notification\n        When I send a gcm message "{"to":"deviceID", "data": {"message": "Foo Bar", "badge": 6}}"\n        Then I should receive a gcm notification at "deviceID" containing "{\'data\': {\'message\': \'Foo Bar\'}}"\n```\n\nTypically, it will be your web application that sends\nemail/sms/notifications and testing it comes down to configuring the\napplication to send email/sms/notifications to the mock servers.\n\n## Personas & state\n\nA lot of web apps today rely on multi-user interactions. To help you\nwith those interactions, _behaving_ uses the notion of _personas_. A\npersona within a test runs in its own instance of a browser and you can\nhave more than one persona (and its browser instance) running\nconcurrently. You switch among personas by calling\n\n```gherkin\nGiven "PersonaName" as the persona\n```\n\nPersonas are also typically implemented as simple dictionaries allowing\nthem to carry state, save and reuse variables inside a scenario. When a\npersona is first invoked it is created as an empty dictionary. You can\npredefine personas though with set values.\n\nLet\'s take the familiar LOTR characters as our test users. On setting up\nthe test environment (details later in the setup\\_ section), we set up\nthe characters basic variables we might be needing in the tests as such:\n\n```python\nPERSONAS = {\n    \'Frodo\': dict(\n        fullname=u\'Frodo Baggins\',\n        email=u\'frodo@shire.com\',\n        password=u\'frodopass\',\n        mobile=\'+4745690001\',\n        address: {\n            street: "The Shire",\n            zip: "4321"\n        }\n    ),\n    \'Gandalf\': dict(\n        fullname=u\'Gandalf the Grey\',\n        email=u\'gandalf@wizardry.com\',\n        password=u\'gandalfpass\',\n        mobile=\'+4745690004\',\n        address: {\n            street: "Rivendell street 1",\n            zip: "1234"\n        }\n  ),\n  ...\n}\ndef before_scenario(context, scenario):\n    ...\n    context.personas = PERSONAS\n```\n\nWithin a test and given a persona, you can now use `$var_name` to access\na variable of a persona. You can also set new variables on personas. So\nthe following,\n\n```gherkin\nGiven "Gandalf" as the persona\nWhen I fill in "name" with "$fullname"\nAnd I fill in "street" with "$address.street"\nAnd I set "title" to the text of "document-title"\nAnd I fill in "delete" with "$title"\nAnd I set "address.country" to the text of "country"\nAnd I set "postaddress" to:\n"""\n$fullname\n$address.street, $address.zip, $address.country\n"""\n```\n\nwould fill in the field with id `name` with `Gandalf the Grey`, `street`\nwith `Rivendell street 1` set the variable `title` to the text of the\nelement with id `document-title` and reuse the variable `title` to fill\nin the field with id `delete`. It would also store the value of the\nfield with id "country" in address[`country`]. The `$var_name` pattern\nis also usable in the text received by steps that expect a body of text,\nwhich means that the `postaddress` persona variable will contain\nGandalf\'s complete snail-mail postage address nicely formatted on\nmultiple lines.\n\n## Hello Persona example\n\nLet us assume the following (coming from a real example) scenario.\n[Crypho](https://crypho.com), is an online messaging/sharing site that\nprovides users with end-to-end encrypted real-time communications.\n_behaving_ was written to help test Crypho.\n\nIn Crypho, teams collaborate in _spaces_. To invite somebody in a\n_space_ the invitee has to share a token with an invitor, so both can\nverify each other\'s identity.\n\n```gherkin\nFeature: Frodo invites Gandalf to The Shire space\n\n    Given state "the-shire"\n\n    Scenario: Frodo invites Gandalf to The Shire\n\n        Given "Gandalf" as the persona\n        When I log in\n```\n\nBefore the scenarios start, the custom step `Given state "the-shire"`\nexecutes. This preloads the db with data, sets up the server etc. Then\nthe scenario executes:\n\nFirst Gandalf logs in. The step `Given "Gandalf" as the persona`, fires\nup a browser that belongs to the persona Gandalf. The following step,\n`When I log in` is a custom step defined as follows:\n\n```python\n@when(\'I log in\')\ndef log_in(context):\n\n    assert context.persona\n    context.execute_steps(u"""\n        When I go to Home\n            Then I should see an element with id "email" within 2 seconds\n        When I fill in "email" with "$email"\n        And I press "send-sms"\n            Then I should see "We have sent you an SMS with a security code" within 2 seconds\n            And I should receive an sms at "$mobile"\n            And "token" should be enabled\n        When I parse the sms I received at "$mobile" and set "Your Crypho code is {token}"\n        And I fill in "token" with "$token"\n        And I fill in "password" with "$password"\n        And I press "login"\n            Then I should see "Crypho" within 5 seconds\n    """)\n```\n\nObserve above how the current persona (Gandalf) parses the sms it\nreceives and saves it as "token". Later Gandalf reuses it to fill in the\ntwo-factor authentication field.\n\nNow that Gandalf is logged in, the test proceeds with Frodo. Frodo will\nlog in, and invite Gandalf to a private space.\n\n```gherkin\nGiven "Frodo" as the persona\nWhen I log in\nAnd I click the link with text that contains "My spaces"\nAnd I click the link with text that contains "The Shire"\nAnd I press "invite-members"\n    Then I should see "Invite members" within 1 seconds\nWhen I fill in "invitees" with "gandalf@wizardry.com"\nAnd I fill in "invitation-message" with "Come and join us!"\nAnd I press "send-invitations"\n    Then I should see "Your invitations have been sent" within 2 seconds\n```\n\nOnce the invitations are sent we switch back to Gandalf\'s browser, who\nshould have received a notification in his browser, as well as an email.\nHe then proceeds to send an sms to Frodo with the token who completes\nthe invitation.\n\n```gherkin\nGiven "Gandalf" as the persona\nThen I should see "Your invitations have been updated" within 2 seconds\nAnd I should receive an email at "gandalf@wizardry.com" containing "Frodo Baggins has invited you to join a private workspace in Crypho"\nWhen I click the link with text that contains "Invitations"\nAnd I click the link with text that contains "Pending invitations"\n    Then I should see "Come and join us!"\nWhen I set "token" to the text of "invitation-token"\nAnd I send an sms to "45699900" with body "$token"\n\nGiven "Frodo" as the persona\n    Then I should receive an sms at "45699900"\nWhen I set "FrodoToken" to the body of the sms I received at "45699900"\nAnd I click the link with text that contains "Invitations"\nAnd I click the link with text that contains "Enter authorization token"\nAnd I fill in "auth-token" with "$FrodoToken"\nAnd I press "Submit"\n    Then I should see "The invitation has been accepted." within 5 seconds\n    And I should see "Gandalf the Grey has joined the space, invited by Frodo Baggins" within 10 seconds\n```\n\nYou can see the test in action on video\n[here](http://vimeo.com/63672466/).\n\n## Setting up a test environment\n\nStart by installing _behaving_ by using either `pip` or `easy_install`.\nThis will also install dependencies and create the `behave` script with\nwhich you invoke your tests. If you prefer using buildout, clone the\npackage itself from its repository, it contains already a buildout\nconfiguration.\n\nTypically you will be having a folder containing all your features and\nsteps. For example a directory structure like the following:\n\n```\nfeatures/\nfeatures/mytest.feature\nfeatures/myothertest.feature\nfeatures/environment.py\nfeatures/steps/\nfeatures/steps/steps.py\n```\n\nIn the steps directory you will need to import the _behaving_ steps you\nneed. You can also define your own steps. So `steps.py` might look like:\n\n```python\nfrom behave import when\nfrom behaving.web.steps import *\nfrom behaving.sms.steps import *\nfrom behaving.mail.steps import *\nfrom behaving.notifications.gcm.steps import *\nfrom behaving.personas.steps import *\n\n@when(\'I go to home\')\ndef go_to_home(context):\n    context.browser.visit(\'https://web/\')\n```\n\nIn `environment.py` you specify settings as well the things that need to\nhappen at various stages of testing, i.e. before and after everything, a\nfeature run, or a scenario run. For convenience you can import and reuse\n`behaving.environment` which will perform default actions like closing\nall browsers after a scenario, clean the email folder etc.\n\nIt is also possible to use `behaving.web.environment`,\n`behaving.mail.environment`, `behaving.sms.environment` and\n`behaving.personas.environment` on their own, if you don\'t have need for\nSMS for example.\n\nAn example of an environment that does simply set some variables and\nthen rely on default actions for the various stages, might look like the\nfollowing:\n\n```python\nimport os\nfrom behaving import environment as benv\n\nPERSONAS = {}\n\ndef before_all(context):\n    import mypackage\n    context.attachment_dir = os.path.join(os.path.dirname(mypackage.__file__), \'tests/data\')\n    context.sms_path = os.path.join(os.path.dirname(mypackage.__file__), \'../../var/sms/\')\n    context.gcm_path = os.path.join(os.path.dirname(mypackage.__file__), \'../../var/gcm/\')\n    context.mail_path = os.path.join(os.path.dirname(mypackage.__file__), \'../../var/mail/\')\n    benv.before_all(context)\n\n\ndef after_all(context):\n    benv.after_all(context)\n\n\ndef before_feature(context, feature):\n    benv.before_feature(context, feature)\n\n\ndef after_feature(context, feature):\n    benv.after_feature(context, feature)\n\n\ndef before_scenario(context, scenario):\n    benv.before_scenario(context, scenario)\n    context.personas = PERSONAS\n\ndef after_scenario(context, scenario):\n    benv.after_scenario(context, scenario)\n```\n\nThe following variables are supported and can be set to override\ndefaults:\n\n- `screenshots_dir` (the path where screenshots will be saved. If it\n  is set, any failure in a scenario will result in a screenshot of the\n  browser at the time when the failure happened.)\n- `attachment_dir` (the path where file attachments can be found)\n- `sms_path` (the path to be used by `smsmock` to save sms. Defaults\n  to `current_dir/sms` )\n- `gcm_path` (the path to be used by `gcmmock` to save gcm\n  notifications. Defaults to `current_dir/gcm` )\n- `mail_path` (the path to be used by `mailmock` to save mail.\n  Defaults to `current_dir/mail` )\n- `default_browser`\n- `default_browser_size` (tuple (width, height), applied to each\n  browser as it\'s created)\n- `max_browser_attempts` (how many times to retry creating the browser\n  if it fails)\n- `remote_webdriver_url` (points to your selenium hub url or remote\n  webdriver. Defaults to `None`)\n- `browser_args` (a dict of additional keyword arguments used when\n  creating a browser)\n- `base_url` (the base url for a browser, allows you to use relative\n  paths)\n- `accept_ssl_certs` (setting to `True` will accept self-signed/invalid\n  certificates. Defaults to `None`)\n\nYou can run the tests simply by issuing\n\n```sh\n./bin/behave ./features\n```\n\nFor chrome and docker issues, the code below is useful\n\n```python\nfrom selenium.webdriver.chrome.options import Options\nchrome_options = Options()\nchrome_options.add_argument(\'--no-sandbox\')\ncontext.browser_args = {\n    \'options\': chrome_options\n}\n```\n\n## Mail, GCM and SMS mock servers\n\nWhen _behaving_ is installed, it creates three scripts to help you test\nmail, gcm and sms, `mailmock`, `gcmmock` and `smsmock` respectively. You\ncan directly invoke them before running your tests, they all take a port\nas well as the directory to output data as parameters. For example,\n\n```sh\n./bin/smsmock -p 8081 -o ./var/sms\n./bin/gcmmock -p 8082 -o ./var/notifications/gcm\n./bin/mailmock -p 8083 -o ./var/mail [--no-stdout]\n```\n\n## `behaving.web` Supported matchers/steps\n\n- Browsers\n\n  - Given a browser [opens the default browser, i.e. Firefox]\n  - Given `brand` as the default browser [sets the default browser to be `brand`, this is the browser name when using the remote webdriver or Firefox, Chrome, Safari]\n  - Given the electron app "`app_path`" [for use with electron-based desktop apps]\n  - Given browser "`name`" [opens the browser named `name`]\n  - When I reload\n  - When I go back\n  - When I go forward\n  - When I resize the browser to `width`x`height`\n  - When I resize the viewport to `width`x`height`\n  - When I take a screenshot [will save a screenshot of the browser if `screenshots_dir` is set on the environment. Also, if `screenshots_dir` is set, all failing tests will result in a screenshot.]\n  - When I execute the script "`script`"\n  - When I set the cookie "`key`" to "`value`"\n  - When I delete the cookie "`key`"\n  - When I delete all cookies\n  - When I close the browser "`name`"\n\n- Frames\n\n  - When I switch to frame with css "`css`"\n  - When I switch back to the main page\n\n- Windows\n\n  - When I open a new window named "`name`" at "`url`"\n  - When I name the current window "`name`"\n  - When I switch to the window named "`name`"\n\n- URLs\n\n  - Given the base url "`url`" [sets the base url to `url`, alternatively set `context.base_url` directly in `environment.py`]\n  - When I visit "`url`"\n  - When I go to "`url`"\n  - When I parse the url path and set "`{expression}`"\n  - Then the browser\'s URL should be "`url`"\n  - Then the browser\'s URL should contain "`text`"\n  - Then the browser\'s URL should not contain "`text`"\n\n- Links\n\n  - When I click the link to "`url`"\n  - When I click the link to a url that contains "`url`"\n  - When I click the link with text "`text`"\n  - When I click the link with text that contains "`text`"\n\n- Text, element & class presence\n\n  - When I wait for `timeout` seconds\n  - When I show the element with id "`id`"\n  - When I hide the element with id "`id`"\n\n  - Text\n\n    - Then I should see "`text`"\n    - Then I should not see "`text`"\n    - Then I should see "`text`" within `timeout` seconds\n    - Then I should not see "`text`" within `timeout` seconds\n\n  - ID\n    - Then I should see an element with id "`id`"\n    - Then I should not see an element with id "`id`"\n    - Then I should see an element with id "`id`" within `timeout` seconds\n    - Then I should not see an element with id "`id`" within `timeout` seconds\n\n- CSS\n\n  - Existence\n    - Then I should see an element with the css selector "`selector`"\n    - Then I should not see an element with the css selector "`selector`"\n    - Then I should see an element with the css selector "`selector`" within `timeout` seconds\n    - Then I should not see an element with the css selector "`selector`" within `timeout` seconds\n    - Then I should see `n` elements with the css selector "`css`"\n    - Then I should see at least `n` elements with the css selector "`css`" within `timeout` seconds\n  - Visibility\n    - Then the element with the css selector "`css`" should be visible\n    - Then the element with the css selector "`css`" should be visible within `timeout` seconds\n    - Then the element with the css selector "`css`" should not be visible\n    - Then the element with the css selector "`css`" should be visible within `timeout` seconds\n    - Then {n:d} elements with the css selector "`css`" should be visible\n    - Then {n:d} elements with the css selector "`css`" should be visible within `timeout` seconds\n    - Then at least {n:d} elements with the css selector "`css`" should be visible\n    - Then at least {n:d} elements with the css selector "`css`" should be visible within `timeout` seconds\n  - Existence of a class on an element\n    - Then the element with xpath "`xpath`" should have the class "`cls`"\n    - Then the element with xpath "`xpath`" should not have the class "`cls`"\n    - Then the element with xpath "`xpath`" should have the class "`cls`" within `timeout` seconds\n    - Then the element with xpath "`xpath`" should not have the class "`cls`" within `timeout` seconds\n    - Then "`name`" should have the class "`cls`"\n    - Then "`name`" should not have the class "`cls`"\n    - Then "`name`" should have the class "`cls`" within `timeout` seconds\n    - Then "`name`" should not have the class "`cls`" within `timeout:d` seconds\n  - XPath\n    - Then I should see an element with xpath "`xpath`"\n    - Then I should not see an element with xpath "`xpath`"\n    - Then I should see an element with xpath "`xpath`" within `timeout` seconds\n    - Then I should not see an element with xpath "`xpath`" within `timeout` seconds\n\n- Forms\n\n  - When I fill in "`name|id`" with "`value`"\n  - When I clear field "`name|id`"\n  - When I type "`value`" to "`name|id`" [same as fill, but happens slowly triggering keyboard events]\n  - When I choose "`value`" from "`name`"\n  - When I check "`name|id`"\n  - When I uncheck "`name|id`"\n  - When I toggle "`name|id`"\n  - When I select "`value`" from "`name`""\n  - When I select by text "`text`" from "`name`""\n  - When I press "`name|id|text|innerText`"\n  - When I press the element with xpath "`xpath`"\n  - When I attach the file "`path`" to "`name`"\n  - When I set the innner HTML of the element with id "`id`" to "`contents`" [Sets html on a `contenteditable` element with id `id` to `contents`]\n  - When I set the innner HTML of the element with class "`class`" to "`contents`"\n  - When I set the innner HTML of the element with class "`class`" to "`contents`"\n  - When I send "`KEY`" to "`name`"\n  - When I focus on "`name`"\n  - Then field "`name`" should have the value "`value`"\n  - Then field "`name`" should have the value "`value`" within `timeout` seconds\n  - Then the selection "`name`" should have the options "`valueA, valueB`" selected\n  - Then "`name`" should be enabled\n  - Then "`name`" should be disabled\n  - Then "`name`" should not be enabled\n  - Then "`name`" should be valid\n  - Then "`name`" should be invalid\n  - Then "`name`" should not be valid\n  - Then "`name`" should be required\n  - Then "`name`" should not be required\n\n- HTML tables\n\n  - Then the table with id "`id`" should be  \n    | header1 | header2 | ... | header(m) |  \n    | cell00 | cell01 | ... | cell0m |  \n    | cell10 | cell11 | ... | cell1m |  \n    ...  \n    | celln0 | celln1 | ... | cellnm |\n\n  - Then the table with xpath "`xpath`" should be  \n    | header1 | header2 | ... | header(m) |  \n    | cell00 | cell01 | ... | cell0m |  \n    | cell10 | cell11 | ... | cell1m |  \n    ...  \n    | celln0 | celln1 | ... | cellnm |\n\n  - Then the table with id "`id`" should contain the rows  \n    | cell00 | cell01 | ... | cell0m |  \n    | cell10 | cell11 | ... | cell1m |\n\n  - Then the table with xpath "`xpath`" should contain the rows  \n    | cell00 | cell01 | ... | cell0m |  \n    | cell10 | cell11 | ... | cell1m |\n\n  - Then the table with id "`id`" should not contain the rows  \n    | cell00 | cell01 | ... | cell0m |  \n    | cell10 | cell11 | ... | cell1m |\n\n  - Then the table with xpath "`xpath`" should not contain the rows  \n    | cell00 | cell01 | ... | cell0m |  \n    | cell10 | cell11 | ... | cell1m |\n\n  - Then row `row_no` in the table with id "`id`" should be  \n    | cell00 | cell01 | ... | cell0m |\n\n  - Then row `row_no` in the table with xpath "`xpath`" should be  \n    | cell00 | cell01 | ... | cell0m |\n\n  - Then the value of the cell in row `row_no`, column `col_no` in the table with id "`id`" should be "`value`"\n\n  - Then the value of the cell in row `row_no`, column `col_no` in the table with xpath "`xpath`" should be "`value`"\n\n  - Then the value of the cell in row `row_no`, column "`col_header`" in the table with id "`id`" should be "`value`"\n\n  - Then the value of the cell in row `row_no`, column "`col_header`" in the table with xpath "`xpath`" should be "`value`"\n\n- Alerts & prompts\n\n  - When I enter "`text`" to the alert - When I accept the alert - When I dismiss the alert - Then I should see an alert - Then I should see an alert within `timeout` seconds - Then I should see an alert containing "`text`" - Then I should see an alert containing "`text`" within `timeout` seconds\n\n- Mouse\n\n  - When I mouse over the element with xpath "`xpath`"\n  - When I mouse out of the element with xpath "`xpath`"\n\n- Downloads\n\n  - Then the file "`filename`" with contents "`text`" should have been downloaded within `timeout` seconds\n  - Then the file "`filename`" should have been downloaded within `timeout` seconds\n\n- Persona interaction & variables\n\n  - When I set "`key`" to the text of "`id|name`"\n  - When I set "`key`" to the attribute "`attr`" of the element with xpath "`xpath`"\n  - When I evaluate the script "`script`" and assign the result to "`key`"\n\n## `behaving.mail` Supported matchers/steps\n\n- When I click the link in the email I received at "`address`"\n- When I parse the email I received at "`address`" and set "`expression`"\n- When I clear the email messages\n- Then I should receive an email at "`address`"\n- Then I should receive an email at "`address`" with subject "`subject`"\n- Then I should receive an email at "`address`" containing "`text`"\n- Then I should receive an email at "`address`" with attachment "`filename`"\n- Then I should not have received any emails at "`address`"\n\n## `behaving.sms` Supported matchers/steps\n\n- When I set "`key`" to the body of the sms I received at "`number`"\n- When I parse the sms I received at "`number`" and set "`expression`"\n- Then I should receive an sms at "`number`"\n- Then I should receive an sms at "`number`" containing "`text`"\n\n## `behaving.notifications.gcm` Supported matchers/steps\n\n- When I send a gcm message "{"to":"deviceID", "data": {"message":"Foo Bar", "badge": 6}}"\n- Then I should receive a gcm notification at "deviceID" containing "{\'data\': {\'message\': \'Foo Bar\'}}"\n- Then I should have received any gcm notifications at "deviceID"\n\n## `behaving.personas` Supported matchers/steps\n\n- Given "`name`" as the persona\n- When I set "`key`" to "`value`"\n- When I set "`key`" to:  \n  """ `some longer body of text`  \n   `usually multiline`  \n  """\n- When I clone persona "`source`" to "`target`"\n- Then "`key`" is set to "`value`"\n\n## Debugging\n\n- When I pause the tests\n\n## Docker integration\n\nA `Dockerfile` as well as a complete setup using `docker-compose` are provided to help you create selenium grid configurations that run your tests. In addition dev container configuration is included if VSCode is your thing.\n\nIn addition we provide pre-build images on docker hub for the `linux/amd64` and `linux/arm64` platforms. Use\n\n```bash\ndocker pull behaving/behaving:latest\n```\n\nto pull the image.\n\n## Running behaving tests\n\nYou can run all behaving tests as follows:\n\nStart docker compose:\n\n```\ndocker-compose up\n```\n\nOpen a shell in the behaving container:\n\n```\ndocker-compose exec behaving bash\n```\n\nRun behaving tests:\n\n```\nbehave tests/features\n```\n',
    'author': 'Yiorgis Gozadinos',
    'author_email': 'ggozadinos@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ggozad/behaving',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
