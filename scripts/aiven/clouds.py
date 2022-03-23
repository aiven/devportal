import requests


def print_cloud_entry(cloud):
    print("  * - ``{}``".format(cloud['cloud_name']))
    print("    - {}".format(cloud['cloud_description']))


def main():
    response = requests.get("https://api.aiven.io/v1/clouds")
    data = response.json()
    print(".. list-table::")
    print("  :header-rows: 1")
    print("")

    print("  * - Cloud")
    print("    - Description")
    for cloud in data['clouds']:
        print_cloud_entry(cloud)


if __name__ == '__main__':
    main()
