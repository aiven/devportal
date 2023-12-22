import argparse
import jinja2
import re
import requests
from dataclasses import dataclass
from typing import cast, Self
from natsort import natsorted

CLOUD_ENTRIES_TEMPLATE = """\
{% set state = namespace(prev_cloud_vendor_code=None) %}
{%- for cloud_entry in cloud_entries -%}
{% if cloud_entry.vendor_code != state.prev_cloud_vendor_code %}
{% set state.prev_cloud_vendor_code = cloud_entry.vendor_code %}
{{ cloud_entry.vendor_name }}
-----------------------------------------------------
.. list-table::
  :header-rows: 1

  * - Region
    - Cloud
    - Description
{%- endif %}
  * - {{ cloud_entry.geo_region }}
    - ``{{ cloud_entry.name }}``
    - {{ cloud_entry.description }}
  {%- endfor -%}
"""


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
            for description_part in re.split(
                r"[,:-]", cast(str, cloud["cloud_description"])
            )
        ]
        vendor_name = description_parts.pop(2)
        description = (
            f"{description_parts[0]}, {description_parts[1]}: {description_parts[2]}"
        )
        cloud_name = cast(str, cloud["cloud_name"])
        vendor_code = cloud_name[0 : cloud_name.index("-")]
        return cls(
            description=description,
            geo_region=cast(
                str, cloud["geo_region"]
            ).title(),  # Printing in title case to make it look better
            name=cloud_name,
            vendor_code=vendor_code,
            vendor_name=vendor_name,
        )


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

    res = jinja2.Template(CLOUD_ENTRIES_TEMPLATE).render(cloud_entries=cloud_entries)

    with open(filename, "w") as text_file:
        text_file.write(res)
        print(f"Generate 'List of Available Cloud Region': {filename}")


if __name__ == "__main__":
    main()
