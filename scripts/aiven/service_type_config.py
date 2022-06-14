import requests
import argparse

# Save generated files in the includes
PATH = "includes/"


def print_row(param, value_type, title, desc, indent=0):
    row = ""
    preamble = "" + "  " * indent

    row += f"{preamble}{param} => *{value_type}*"
    row += "\n"
    row += f"{preamble}  **{title}** {desc}"
    return row


def print_service_type_docs(service_type, data):
    result = ""
    schema = data["service_types"][service_type]["user_config_schema"]

    # Rows
    for key, value in schema["properties"].items():
        result += "\n"
        result += print_row(
            f"``{key}``",
            value.get("type", ""),
            value.get("title", ""),
            value.get("description", ""),
        )

        # handle any nested properties
        if value.get("type", "") == "object":
            for nested_key, nested_value in value.get("properties").items():
                result += "\n" * 2
                result += print_row(
                    f"``{nested_key}``",
                    nested_value.get("type", ""),
                    nested_value.get("title"),
                    nested_value.get("description"),
                    1,
                )

        result += "\n" * 3
        pass
    # Empty row to end
    result += "\n"
    return result


def generate_file(service_type, data):
    FILE_NAME = PATH + f"config-{str(service_type)}.rst"
    with open(FILE_NAME, "w") as text_file:
        text_file.write(print_service_type_docs(service_type, data))
        print(f"Generated Advanced params: {FILE_NAME}")


def main():
    parser = argparse.ArgumentParser(description="Get config for service type.")
    parser.add_argument(
        "service_type",
        metavar="service_type",
        help="which service type to get config for",
    )
    args = parser.parse_args()
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    for service_type in data["service_types"]:
        if service_type == args.service_type:
            generate_file(service_type, data)


if __name__ == "__main__":
    main()
