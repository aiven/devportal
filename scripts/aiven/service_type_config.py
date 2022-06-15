import requests
import argparse


def create_row(parameter, value_type, title, desc, indent=0) -> str:
    """Creates content's row.

    :param parameter: parameter described
    :param value_type: parameter type
    :param title: paramete's title
    :param desc: parameter description
    :returns: formatted string with parameter info
    :rtype: str
    """
    row = ""
    preamble = "" + "  " * indent

    row += f"{preamble}{parameter} => *{value_type}*"
    row += "\n"
    row += f"{preamble}  **{title}** {desc}"
    return row


import sys
from typing import Dict


def create_service_type_docs(service_type: str, data: Dict) -> str:
    """Creates information to be used to write service type docs.

    :param service_type: parameter described
    :param data: parameters data to extract needed info
    :param title: paramete's title
    :param desc: parameter description
    :returns: formatted string with parameter info
    :rtype: str
    """
    content = ""
    try:
        schema = data["service_types"][service_type]["user_config_schema"]
    except KeyError:
        print(f"Invalid service_type: {service_type}")
        sys.exit(1)

    # Rows
    for key, value in schema["properties"].items():
        content += "\n"
        content += create_row(
            f"``{key}``",
            value.get("type", ""),
            value.get("title", ""),
            value.get("description", ""),
        )

        # handle any nested properties
        if value.get("type", "") == "object":
            for nested_key, nested_value in value.get("properties").items():
                content += "\n" * 2
                content += create_row(
                    f"``{nested_key}``",
                    nested_value.get("type", ""),
                    nested_value.get("title", ""),
                    nested_value.get("description", ""),
                    1,
                )

        content += "\n" * 3
        pass
    # Empty row to end
    content += "\n"
    return content


def main():
    parser = argparse.ArgumentParser(description="Get config for service type.")
    parser.add_argument(
        "service_type",
        metavar="service_type",
        help="which service type to get config for",
    )
    parser.add_argument(
        "filename",
        metavar="filename",
        help="file to save content to",
    )
    args = parser.parse_args()
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    for service_type in data["service_types"]:
        if service_type == args.service_type:
            filename = args.filename
            with open(filename, "w") as text_file:
                file_content = create_service_type_docs(service_type, data)
                text_file.write(file_content)
                print(f"Updated Advanced params saved on {filename}")


if __name__ == "__main__":
    main()
