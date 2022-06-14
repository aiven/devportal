import requests
from io import StringIO
from service_type_config import print_service_type_docs, generate_file


def main():
    SERVICES = ["flink", "grafana", "kafka", "m3db", "redis", "opensearch", "mysql"]
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    for service_type in SERVICES:
        if service_type in data["service_types"]:
            generate_file(service_type, data)


if __name__ == "__main__":
    main()
