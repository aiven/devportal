import requests


def print_cloud_entry(cloud):
    print("  * - {}".format(cloud['geo_region']))
    print("    - ``{}``".format(cloud['cloud_name']))
    print("    - {}".format(cloud['cloud_description']))


def main():
    response = requests.get("https://api.aiven.io/v1/clouds")
    data = response.json()["clouds"]

    # Sorting the data by vendor and region
    data = sorted(data, key=lambda k: k["cloud_name"][0: k["cloud_name"].find('-')] + " " + k['geo_region'] + k["cloud_name"])

    prevCloud = None
    for cloud in data:
        currCloud = cloud["cloud_name"][0: cloud["cloud_name"].find('-')]
        if currCloud != prevCloud:
            prevCloud = currCloud
            print("")
            print(currCloud)
            print("-----------------------------------------------------")

            print(".. list-table::")
            print("  :header-rows: 1")
            print("")

            print("  * - Region")
            print("    - Cloud")
            print("    - Description")

        print_cloud_entry(cloud)


if __name__ == '__main__':
    main()
