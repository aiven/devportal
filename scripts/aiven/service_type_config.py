import requests
import argparse


def print_row(param, value_type, title, desc, indent=0):
    preamble = ''
    for i in range(indent):
        preamble = preamble + '  '

    print(f"{preamble}{param}  *{value_type}*")
    print(f"{preamble}  - **{title}** {desc}")
    print("")


def print_service_type_docs(service_type, data):
    schema = data['service_types'][service_type]['user_config_schema']

    print("")

    # Rows
    for key, value in schema['properties'].items():
        print_row(
            f"``{key}``",
            value.get('type', ''),
            value.get('title'),
            value.get("description", '')
            )

        # handle any nested properties
        if value.get('type', '') == "object":
            for nested_key, nested_value in value.get('properties').items():
                print_row(
                    f"``{nested_key}``",
                    nested_value.get('type', ''),
                    nested_value.get('title'),
                    nested_value.get('description'),
                    1
                    )

        print("")
        print("")
        pass
    # Empty row to end
    print("")


def main():
    parser = argparse.ArgumentParser(
                        description='Get config for service type.')
    parser.add_argument('service_type', metavar='service_type',
                        help='which service type to get config for')
    args = parser.parse_args()
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    for service_type in data['service_types']:
        if(service_type == args.service_type):
            print_service_type_docs(service_type, data)


if __name__ == '__main__':
    main()
