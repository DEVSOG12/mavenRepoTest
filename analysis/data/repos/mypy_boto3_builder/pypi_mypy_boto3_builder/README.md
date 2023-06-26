<a id="mypy-boto3-customer-profiles"></a>

# mypy-boto3-customer-profiles

[![PyPI - mypy-boto3-customer-profiles](https://img.shields.io/pypi/v/mypy-boto3-customer-profiles.svg?color=blue)](https://pypi.org/project/mypy-boto3-customer-profiles)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-customer-profiles.svg?color=blue)](https://pypi.org/project/mypy-boto3-customer-profiles)
[![Docs](https://img.shields.io/readthedocs/boto3-stubs.svg?color=blue)](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-customer-profiles?color=blue)](https://pypistats.org/packages/mypy-boto3-customer-profiles)

![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)

Type annotations for
[boto3.CustomerProfiles 1.26.149](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles)
service compatible with [VSCode](https://code.visualstudio.com/),
[PyCharm](https://www.jetbrains.com/pycharm/),
[Emacs](https://www.gnu.org/software/emacs/),
[Sublime Text](https://www.sublimetext.com/),
[mypy](https://github.com/python/mypy),
[pyright](https://github.com/microsoft/pyright) and other tools.

Generated by
[mypy-boto3-builder 7.14.5](https://github.com/youtype/mypy_boto3_builder).

More information can be found on
[boto3-stubs](https://pypi.org/project/boto3-stubs/) page and in
[mypy-boto3-customer-profiles docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/).

See how it helps to find and fix potential bugs:

![boto3-stubs demo](https://github.com/youtype/mypy_boto3_builder/raw/main/demo.gif)

- [mypy-boto3-customer-profiles](#mypy-boto3-customer-profiles)
  - [How to install](#how-to-install)
    - [VSCode extension](#vscode-extension)
    - [From PyPI with pip](#from-pypi-with-pip)
  - [How to uninstall](#how-to-uninstall)
  - [Usage](#usage)
    - [VSCode](#vscode)
    - [PyCharm](#pycharm)
    - [Emacs](#emacs)
    - [Sublime Text](#sublime-text)
    - [Other IDEs](#other-ides)
    - [mypy](#mypy)
    - [pyright](#pyright)
  - [Explicit type annotations](#explicit-type-annotations)
    - [Client annotations](#client-annotations)
    - [Paginators annotations](#paginators-annotations)
    - [Literals](#literals)
    - [Typed dictionaries](#typed-dictionaries)
  - [How it works](#how-it-works)
  - [What's new](#what's-new)
    - [Implemented features](#implemented-features)
    - [Latest changes](#latest-changes)
  - [Versioning](#versioning)
  - [Thank you](#thank-you)
  - [Documentation](#documentation)
  - [Support and contributing](#support-and-contributing)

<a id="how-to-install"></a>

## How to install

<a id="vscode-extension"></a>

### VSCode extension

Add
[AWS Boto3](https://marketplace.visualstudio.com/items?itemName=Boto3typed.boto3-ide)
extension to your VSCode and run `AWS boto3: Quick Start` command.

Click `Modify` and select `boto3 common` and `CustomerProfiles`.

<a id="from-pypi-with-pip"></a>

### From PyPI with pip

Install `boto3-stubs` for `CustomerProfiles` service.

```bash
# install with boto3 type annotations
python -m pip install 'boto3-stubs[customer-profiles]'


# Lite version does not provide session.client/resource overloads
# it is more RAM-friendly, but requires explicit type annotations
python -m pip install 'boto3-stubs-lite[customer-profiles]'


# standalone installation
python -m pip install mypy-boto3-customer-profiles
```

<a id="how-to-uninstall"></a>

## How to uninstall

```bash
python -m pip uninstall -y mypy-boto3-customer-profiles
```

<a id="usage"></a>

## Usage

<a id="vscode"></a>

### VSCode

- Install
  [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Install
  [Pylance extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- Set `Pylance` as your Python Language Server
- Install `boto3-stubs[customer-profiles]` in your environment:

```bash
python -m pip install 'boto3-stubs[customer-profiles]'
```

Both type checking and code completion should now work. No explicit type
annotations required, write your `boto3` code as usual.

<a id="pycharm"></a>

### PyCharm

Install `boto3-stubs-lite[customer-profiles]` in your environment:

```bash
python -m pip install 'boto3-stubs-lite[customer-profiles]'`
```

Both type checking and code completion should now work. Explicit type
annotations **are required**.

Use `boto3-stubs` package instead for implicit type discovery.

<a id="emacs"></a>

### Emacs

- Install `boto3-stubs` with services you use in your environment:

```bash
python -m pip install 'boto3-stubs[customer-profiles]'
```

- Install [use-package](https://github.com/jwiegley/use-package),
  [lsp](https://github.com/emacs-lsp/lsp-mode/),
  [company](https://github.com/company-mode/company-mode) and
  [flycheck](https://github.com/flycheck/flycheck) packages
- Install [lsp-pyright](https://github.com/emacs-lsp/lsp-pyright) package

```elisp
(use-package lsp-pyright
  :ensure t
  :hook (python-mode . (lambda ()
                          (require 'lsp-pyright)
                          (lsp)))  ; or lsp-deferred
  :init (when (executable-find "python3")
          (setq lsp-pyright-python-executable-cmd "python3"))
  )
```

- Make sure emacs uses the environment where you have installed `boto3-stubs`

Type checking should now work. No explicit type annotations required, write
your `boto3` code as usual.

<a id="sublime-text"></a>

### Sublime Text

- Install `boto3-stubs[customer-profiles]` with services you use in your
  environment:

```bash
python -m pip install 'boto3-stubs[customer-profiles]'
```

- Install [LSP-pyright](https://github.com/sublimelsp/LSP-pyright) package

Type checking should now work. No explicit type annotations required, write
your `boto3` code as usual.

<a id="other-ides"></a>

### Other IDEs

Not tested, but as long as your IDE supports `mypy` or `pyright`, everything
should work.

<a id="mypy"></a>

### mypy

- Install `mypy`: `python -m pip install mypy`
- Install `boto3-stubs[customer-profiles]` in your environment:

```bash
python -m pip install 'boto3-stubs[customer-profiles]'`
```

Type checking should now work. No explicit type annotations required, write
your `boto3` code as usual.

<a id="pyright"></a>

### pyright

- Install `pyright`: `npm i -g pyright`
- Install `boto3-stubs[customer-profiles]` in your environment:

```bash
python -m pip install 'boto3-stubs[customer-profiles]'
```

Optionally, you can install `boto3-stubs` to `typings` folder.

Type checking should now work. No explicit type annotations required, write
your `boto3` code as usual.

<a id="explicit-type-annotations"></a>

## Explicit type annotations

<a id="client-annotations"></a>

### Client annotations

`CustomerProfilesClient` provides annotations for
`boto3.client("customer-profiles")`.

```python
from boto3.session import Session

from mypy_boto3_customer_profiles import CustomerProfilesClient

client: CustomerProfilesClient = Session().client("customer-profiles")

# now client usage is checked by mypy and IDE should provide code completion
```

<a id="paginators-annotations"></a>

### Paginators annotations

`mypy_boto3_customer_profiles.paginator` module contains type annotations for
all paginators.

```python
from boto3.session import Session

from mypy_boto3_customer_profiles import CustomerProfilesClient
from mypy_boto3_customer_profiles.paginator import ListEventStreamsPaginator

client: CustomerProfilesClient = Session().client("customer-profiles")

# Explicit type annotations are optional here
# Types should be correctly discovered by mypy and IDEs
list_event_streams_paginator: ListEventStreamsPaginator = client.get_paginator("list_event_streams")
```

<a id="literals"></a>

### Literals

`mypy_boto3_customer_profiles.literals` module contains literals extracted from
shapes that can be used in user code for type checking.

```python
from mypy_boto3_customer_profiles.literals import (
    ConflictResolvingModelType,
    DataPullModeType,
    EventStreamDestinationStatusType,
    EventStreamStateType,
    FieldContentTypeType,
    GenderType,
    IdentityResolutionJobStatusType,
    JobScheduleDayOfTheWeekType,
    ListEventStreamsPaginatorName,
    MarketoConnectorOperatorType,
    OperatorPropertiesKeysType,
    OperatorType,
    PartyTypeType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    StatisticType,
    StatusType,
    TaskTypeType,
    TriggerTypeType,
    UnitType,
    WorkflowTypeType,
    ZendeskConnectorOperatorType,
    logicalOperatorType,
    CustomerProfilesServiceName,
    ServiceName,
    ResourceServiceName,
    PaginatorName,
    RegionName,
)


def check_value(value: ConflictResolvingModelType) -> bool:
    ...
```

<a id="typed-dictionaries"></a>

### Typed dictionaries

`mypy_boto3_customer_profiles.type_defs` module contains structures and shapes
assembled to typed dictionaries for additional type checking.

```python
from mypy_boto3_customer_profiles.type_defs import (
    AddProfileKeyRequestRequestTypeDef,
    ResponseMetadataTypeDef,
    AdditionalSearchKeyTypeDef,
    AddressTypeDef,
    BatchTypeDef,
    AppflowIntegrationWorkflowAttributesTypeDef,
    AppflowIntegrationWorkflowMetricsTypeDef,
    AppflowIntegrationWorkflowStepTypeDef,
    AttributeItemTypeDef,
    ConflictResolutionTypeDef,
    ConsolidationTypeDef,
    RangeTypeDef,
    ThresholdTypeDef,
    ConnectorOperatorTypeDef,
    CreateEventStreamRequestRequestTypeDef,
    DeleteCalculatedAttributeDefinitionRequestRequestTypeDef,
    DeleteDomainRequestRequestTypeDef,
    DeleteEventStreamRequestRequestTypeDef,
    DeleteIntegrationRequestRequestTypeDef,
    DeleteProfileKeyRequestRequestTypeDef,
    DeleteProfileObjectRequestRequestTypeDef,
    DeleteProfileObjectTypeRequestRequestTypeDef,
    DeleteProfileRequestRequestTypeDef,
    DeleteWorkflowRequestRequestTypeDef,
    DestinationSummaryTypeDef,
    DomainStatsTypeDef,
    EventStreamDestinationDetailsTypeDef,
    S3ExportingConfigTypeDef,
    S3ExportingLocationTypeDef,
    FieldSourceProfileIdsTypeDef,
    FoundByKeyValueTypeDef,
    GetCalculatedAttributeDefinitionRequestRequestTypeDef,
    GetCalculatedAttributeForProfileRequestRequestTypeDef,
    GetDomainRequestRequestTypeDef,
    GetEventStreamRequestRequestTypeDef,
    GetIdentityResolutionJobRequestRequestTypeDef,
    JobStatsTypeDef,
    GetIntegrationRequestRequestTypeDef,
    GetMatchesRequestRequestTypeDef,
    MatchItemTypeDef,
    GetProfileObjectTypeRequestRequestTypeDef,
    ObjectTypeFieldTypeDef,
    ObjectTypeKeyTypeDef,
    GetProfileObjectTypeTemplateRequestRequestTypeDef,
    GetWorkflowRequestRequestTypeDef,
    GetWorkflowStepsRequestRequestTypeDef,
    IncrementalPullConfigTypeDef,
    JobScheduleTypeDef,
    ListAccountIntegrationsRequestRequestTypeDef,
    ListIntegrationItemTypeDef,
    ListCalculatedAttributeDefinitionItemTypeDef,
    ListCalculatedAttributeDefinitionsRequestRequestTypeDef,
    ListCalculatedAttributeForProfileItemTypeDef,
    ListCalculatedAttributesForProfileRequestRequestTypeDef,
    ListDomainItemTypeDef,
    ListDomainsRequestRequestTypeDef,
    PaginatorConfigTypeDef,
    ListEventStreamsRequestRequestTypeDef,
    ListIdentityResolutionJobsRequestRequestTypeDef,
    ListIntegrationsRequestRequestTypeDef,
    ListProfileObjectTypeItemTypeDef,
    ListProfileObjectTypeTemplateItemTypeDef,
    ListProfileObjectTypeTemplatesRequestRequestTypeDef,
    ListProfileObjectTypesRequestRequestTypeDef,
    ListProfileObjectsItemTypeDef,
    ObjectFilterTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListWorkflowsItemTypeDef,
    ListWorkflowsRequestRequestTypeDef,
    MarketoSourcePropertiesTypeDef,
    PutProfileObjectRequestRequestTypeDef,
    S3SourcePropertiesTypeDef,
    SalesforceSourcePropertiesTypeDef,
    ScheduledTriggerPropertiesTypeDef,
    ServiceNowSourcePropertiesTypeDef,
    ZendeskSourcePropertiesTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAddressTypeDef,
    AddProfileKeyResponseTypeDef,
    CreateEventStreamResponseTypeDef,
    CreateIntegrationWorkflowResponseTypeDef,
    CreateProfileResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteProfileKeyResponseTypeDef,
    DeleteProfileObjectResponseTypeDef,
    DeleteProfileObjectTypeResponseTypeDef,
    DeleteProfileResponseTypeDef,
    GetAutoMergingPreviewResponseTypeDef,
    GetCalculatedAttributeForProfileResponseTypeDef,
    GetIntegrationResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MergeProfilesResponseTypeDef,
    PutIntegrationResponseTypeDef,
    PutProfileObjectResponseTypeDef,
    UpdateProfileResponseTypeDef,
    SearchProfilesRequestRequestTypeDef,
    CreateProfileRequestRequestTypeDef,
    WorkflowAttributesTypeDef,
    WorkflowMetricsTypeDef,
    WorkflowStepItemTypeDef,
    AttributeDetailsTypeDef,
    AutoMergingTypeDef,
    GetAutoMergingPreviewRequestRequestTypeDef,
    ConditionsTypeDef,
    TaskTypeDef,
    EventStreamSummaryTypeDef,
    GetEventStreamResponseTypeDef,
    ExportingConfigTypeDef,
    ExportingLocationTypeDef,
    MergeProfilesRequestRequestTypeDef,
    ProfileTypeDef,
    GetMatchesResponseTypeDef,
    GetProfileObjectTypeResponseTypeDef,
    GetProfileObjectTypeTemplateResponseTypeDef,
    PutProfileObjectTypeRequestRequestTypeDef,
    PutProfileObjectTypeResponseTypeDef,
    ListAccountIntegrationsResponseTypeDef,
    ListIntegrationsResponseTypeDef,
    ListCalculatedAttributeDefinitionsResponseTypeDef,
    ListCalculatedAttributesForProfileResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEventStreamsRequestListEventStreamsPaginateTypeDef,
    ListProfileObjectTypesResponseTypeDef,
    ListProfileObjectTypeTemplatesResponseTypeDef,
    ListProfileObjectsResponseTypeDef,
    ListProfileObjectsRequestRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    TriggerPropertiesTypeDef,
    SourceConnectorPropertiesTypeDef,
    UpdateProfileRequestRequestTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowStepsResponseTypeDef,
    CreateCalculatedAttributeDefinitionRequestRequestTypeDef,
    CreateCalculatedAttributeDefinitionResponseTypeDef,
    GetCalculatedAttributeDefinitionResponseTypeDef,
    UpdateCalculatedAttributeDefinitionRequestRequestTypeDef,
    UpdateCalculatedAttributeDefinitionResponseTypeDef,
    ListEventStreamsResponseTypeDef,
    MatchingRequestTypeDef,
    MatchingResponseTypeDef,
    GetIdentityResolutionJobResponseTypeDef,
    IdentityResolutionJobTypeDef,
    SearchProfilesResponseTypeDef,
    TriggerConfigTypeDef,
    SourceFlowConfigTypeDef,
    CreateDomainRequestRequestTypeDef,
    UpdateDomainRequestRequestTypeDef,
    CreateDomainResponseTypeDef,
    GetDomainResponseTypeDef,
    UpdateDomainResponseTypeDef,
    ListIdentityResolutionJobsResponseTypeDef,
    FlowDefinitionTypeDef,
    AppflowIntegrationTypeDef,
    PutIntegrationRequestRequestTypeDef,
    IntegrationConfigTypeDef,
    CreateIntegrationWorkflowRequestRequestTypeDef,
)


def get_structure() -> AddProfileKeyRequestRequestTypeDef:
    return {...}
```

<a id="how-it-works"></a>

## How it works

Fully automated
[mypy-boto3-builder](https://github.com/youtype/mypy_boto3_builder) carefully
generates type annotations for each service, patiently waiting for `boto3`
updates. It delivers drop-in type annotations for you and makes sure that:

- All available `boto3` services are covered.
- Each public class and method of every `boto3` service gets valid type
  annotations extracted from `botocore` schemas.
- Type annotations include up-to-date documentation.
- Link to documentation is provided for every method.
- Code is processed by [black](https://github.com/psf/black) and
  [isort](https://github.com/PyCQA/isort) for readability.

<a id="what's-new"></a>

## What's new

<a id="implemented-features"></a>

### Implemented features

- Fully type annotated `boto3`, `botocore`, `aiobotocore` and `aioboto3`
  libraries
- `mypy`, `pyright`, `VSCode`, `PyCharm`, `Sublime Text` and `Emacs`
  compatibility
- `Client`, `ServiceResource`, `Resource`, `Waiter` `Paginator` type
  annotations for each service
- Generated `TypeDefs` for each service
- Generated `Literals` for each service
- Auto discovery of types for `boto3.client` and `boto3.resource` calls
- Auto discovery of types for `session.client` and `session.resource` calls
- Auto discovery of types for `client.get_waiter` and `client.get_paginator`
  calls
- Auto discovery of types for `ServiceResource` and `Resource` collections
- Auto discovery of types for `aiobotocore.Session.create_client` calls

<a id="latest-changes"></a>

### Latest changes

Builder changelog can be found in
[Releases](https://github.com/youtype/mypy_boto3_builder/releases).

<a id="versioning"></a>

## Versioning

`mypy-boto3-customer-profiles` version is the same as related `boto3` version
and follows [PEP 440](https://www.python.org/dev/peps/pep-0440/) format.

<a id="thank-you"></a>

## Thank you

- [Allie Fitter](https://github.com/alliefitter) for
  [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/),
  this package is based on top of his work
- [black](https://github.com/psf/black) developers for an awesome formatting
  tool
- [Timothy Edmund Crosley](https://github.com/timothycrosley) for
  [isort](https://github.com/PyCQA/isort) and how flexible it is
- [mypy](https://github.com/python/mypy) developers for doing all dirty work
  for us
- [pyright](https://github.com/microsoft/pyright) team for the new era of typed
  Python

<a id="documentation"></a>

## Documentation

All services type annotations can be found in
[boto3 docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/)

<a id="support-and-contributing"></a>

## Support and contributing

This package is auto-generated. Please reports any bugs or request new features
in [mypy-boto3-builder](https://github.com/youtype/mypy_boto3_builder/issues/)
repository.