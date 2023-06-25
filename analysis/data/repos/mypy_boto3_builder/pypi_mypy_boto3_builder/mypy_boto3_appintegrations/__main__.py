"""
Main CLI entrypoint.
"""
import sys


def print_info() -> None:
    """
    Print package info to stdout.
    """
    print(
        "Type annotations for boto3.AppIntegrationsService 1.26.90\nVersion:        "
        " 1.26.90\nBuilder version: 7.13.0\nDocs:           "
        " https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations//\nBoto3 docs:     "
        " https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService\nOther"
        " services:  https://pypi.org/project/boto3-stubs/\nChangelog:      "
        " https://github.com/youtype/mypy_boto3_builder/releases"
    )


def print_version() -> None:
    """
    Print package version to stdout.
    """
    print("1.26.90")


def main() -> None:
    """
    Main CLI entrypoint.
    """
    if "--version" in sys.argv:
        return print_version()
    print_info()


if __name__ == "__main__":
    main()
