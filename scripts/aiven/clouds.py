import requests
import argparse
from typing import Dict


def create_cloud_entry(cloud: Dict) -> str:
    """Creates cloud entry with formatted info.

    :param cloud: contains relevant info about cloud
    :returns: formatted string with cloud info
    :rtype: str
    """
    entry = ""
    # Printing in title case to make it look better
    entry += f'  * - {cloud["geo_region"].title()}'
    entry += "\n"
    entry += f'    - ``{cloud["cloud_name"]}``'
    entry += "\n"
    prefix = cloud["cloud_description"][0 : cloud["cloud_description"].find("-")]
    entry += f"    - {prefix}"
    return entry


def main():
    parser = argparse.ArgumentParser(description="List available cloud regions.")
    parser.add_argument(
        "filename",
        metavar="filename",
        help="which file to save content to",
    )
    args = parser.parse_args()
    filename = args.filename
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
    res = ""
    for cloud in data:
        # Extracting the cloud vendor information available in the cloud_description field between the `-` symbol and the `:` symbol
        curr_cloud = cloud["cloud_description"][
            cloud["cloud_description"].find("-")
            + 2 : cloud["cloud_description"].find(":")
        ]
        res += "\n"
        # If current_cloud is different than  the previous cloud, let's create a new title, section, table
        if curr_cloud != prev_cloud:
            prev_cloud = curr_cloud
            res += "\n"
            res += curr_cloud
            res += "\n"
            res += "-----------------------------------------------------"
            res += "\n"

            res += ".. list-table::"
            res += "\n"
            res += "  :header-rows: 1"
            res += "\n\n"

            res += "  * - Region"
            res += "\n"
            res += "    - Cloud"
            res += "\n"
            res += "    - Description"
            res += "\n"

        res += create_cloud_entry(cloud)

    with open(filename, "w") as text_file:
        text_file.write(res)
        print(f"Updated list of available cloud region: {filename}")


if __name__ == "__main__":
    main()
