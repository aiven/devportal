import requests
import datetime


def print_cloud_entry(cloud):
    print("  * - {}".format(cloud['geo_region'].title()))
    print("    - ``{}``".format(cloud['cloud_name']))
    prefix = cloud['cloud_description'][0: cloud['cloud_description'].find('-')]
    print("    - {}".format(prefix))


def main():
    response = requests.get("https://api.aiven.io/v1/clouds")
    data = response.json()["clouds"]

    # Sorting the data by vendor and region
    data = sorted(data, key=lambda k: k["cloud_name"][0: k["cloud_name"].find('-')] + " " + k['geo_region'] + k["cloud_name"])

    prevCloud = None
    for cloud in data:
        currCloud = cloud["cloud_description"][cloud["cloud_description"].find('-')+2: cloud["cloud_description"].find(':')]
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

    print("")
    print("List of clouds retrieved at **{}**".format(datetime.datetime.now()))


if __name__ == '__main__':
    main()
