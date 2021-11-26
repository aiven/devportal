import requests
import argparse


def print_row(param, value_type, desc):
    print(f"  * - {param}")
    print(f"    - {value_type}")
    print(f"    - {desc}")


def print_service_type_docs(service_type, data):
    schema = data['service_types'][service_type]['user_config_schema']

    print("")
    # Table header
    print(".. list-table::")
    print("  :header-rows: 1")
    print("")
    print_row("Parameter", "Value Type", "Description")

    # Rows
    for key, value in schema['properties'].items():
        print_row(
            f"``{key}``",
            value.get('type', ''),
            value.get('title') + " " + value.get("description", '')
            )
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
