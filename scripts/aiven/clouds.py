import requests


def print_cloud_entry(cloud):
    # Printing in title case to make it look better
    print("  * - {}".format(cloud["geo_region"].title()))
    print("    - ``{}``".format(cloud["cloud_name"]))
    # Printing
    prefix = cloud["cloud_description"][0 : cloud["cloud_description"].find("-")]
    print("    - {}".format(prefix))


def main():
    response = requests.get("https://api.aiven.io/v1/clouds")
    data = response.json()["clouds"]

    # Sorting the data by vendor and region
    # * Vendor is contained in the cloud_name field, between the start and the '-' symbol
    # * geographical region is contained in the geo_region field
    # * the cloud name itself is contained in the cloud_name field
    data = sorted(
        data,
        key=lambda k: k["cloud_name"][0 : k["cloud_name"].find("-")]
        + " "
        + k["geo_region"]
        + k["cloud_name"],
    )

    # This helps creating a new section every time there is a change in the Cloud vendor
    prev_cloud = None
    for cloud in data:
        # Extracting the cloud vendor information available in the cloud_description field between the `-` symbol and the `:` symbol
        curr_cloud = cloud["cloud_description"][
            cloud["cloud_description"].find("-")
            + 2 : cloud["cloud_description"].find(":")
        ]

        # If currentCloud is different than  the previous cloud, let's create a new title, section, table
        if curr_cloud != prev_cloud:
            prev_cloud = curr_cloud
            print("")
            print(curr_cloud)
            print("-----------------------------------------------------")

            print(".. list-table::")
            print("  :header-rows: 1")
            print("")

            print("  * - Region")
            print("    - Cloud")
            print("    - Description")

        print_cloud_entry(cloud)


if __name__ == "__main__":
    main()
