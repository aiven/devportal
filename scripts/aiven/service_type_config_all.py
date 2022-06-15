import requests
from fileinput import filename
from service_type_config import create_service_type_docs

PATH = "includes/"


def main():
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    print("Generate advanced params files for...")
    for service_type in data["service_types"].copy():
        filename = PATH + f"config-{service_type}.rst"
        with open(filename, "w") as text_file:
            file_content = create_service_type_docs(service_type, data)
            text_file.write(file_content)
            print(f"- {service_type}")
    print(f"Files saved on {PATH} folder.")


if __name__ == "__main__":
    main()
