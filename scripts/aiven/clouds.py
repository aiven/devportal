import argparse
import re
import requests
from dataclasses import dataclass
from typing import Dict, Self
from natsort import natsorted


@dataclass
class CloudEntry:
    description: str
    geo_region: str
    name: str
    vendor_code: str
    vendor_name: str

    @classmethod
    def from_dict(cls: type[Self], cloud: dict[str, str | float], /) -> Self:
        """Create cloud entry from dict

        :param cloud: contains relevant info about cloud
        :rtype: CloudEntry
        """

        description_parts = [
            description_part.strip()
            for description_part in re.split(r"[,:-]", cloud["cloud_description"])
        ]
        vendor_name = description_parts.pop(2)
        description = f"{description_parts[0]}, {description_parts[1]}: {description_parts[2]}"
        cloud_name = cloud["cloud_name"]
        vendor_code = cloud_name[0:cloud_name.index("-")]
        return cls(
            description=description,
            geo_region=cloud["geo_region"].title(),  # Printing in title case to make it look better
            name=cloud_name,
            vendor_code=vendor_code,
            vendor_name=vendor_name,
        )

    def to_str(self) -> str:
        """Creates cloud entry with formatted info.

        :returns: formatted string with cloud info
        :rtype: str
        """
        result = ""
        result += f"  * - {self.geo_region}\n"
        result += f"    - ``{self.name}``\n"
        result += f"    - {self.description}"
        return result


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

    cloud_entries = natsorted(
        (CloudEntry.from_dict(cloud) for cloud in data),
        key=lambda cloud: (cloud.vendor_code, cloud.geo_region, cloud.name),
    )

    # This helps creating a new section every time there is a change in the Cloud vendor
    prev_cloud_vendor_code = None
    res = ""
    for cloud_entry in cloud_entries:
        res += "\n"
        # If current_cloud is different than  the previous cloud, let's create a new title, section, table
        if cloud_entry.vendor_code != prev_cloud_vendor_code:
            prev_cloud_vendor_code = cloud_entry.vendor_code
            res += "\n"
            res += cloud_entry.vendor_name
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

        res += cloud_entry.to_str()

    with open(filename, "w") as text_file:
        text_file.write(res)
        print(f"Generate 'List of Available Cloud Region': {filename}")


if __name__ == "__main__":
    main()
