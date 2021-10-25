import requests
from datetime import datetime
from tabulate import tabulate


def date_from_string(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').date()


if __name__ == "__main__":
    response = requests.get("https://api.aiven.io/v1/service_versions")
    data = response.json()
    versions = []
    for version in data['service_versions']:
        aiven_eol = version['aiven_end_of_life_time']
        aiven_eoa = version['availability_end_time']
        next_version = version['upgrade_to_version']
        next_service_type = version['upgrade_to_service_type']
        state = version['state']
        if aiven_eol:
            aiven_eol = date_from_string(aiven_eol)
        else:
            aiven_eol = ""

        if aiven_eoa:
            aiven_eoa = date_from_string(aiven_eoa)
        else:
            aiven_eoa = ""

        if next_version:
            upgrade_to = f"{next_service_type} v{next_version}"
        else:
            upgrade_to = ""

        versions.append([
            version['service_type'],
            version['major_version'],
            aiven_eol,
            aiven_eoa,
            state,
            upgrade_to
        ])
    print(tabulate(versions, headers=[
        "Service type",
        "Version",
        "EOL",
        "EOA",
        "Status",
        "Upgrade to"
    ], tablefmt='rst'))
