from datetime import datetime

from influxdb import InfluxDBClient


def main():
    client = InfluxDBClient(host="SERVICE_HOST",
                            port="SERVICE_PORT",
                            username="avnadmin",
                            password="AVNADMIN_PASS",
                            database="default",
                            ssl=True,
                            verify_ssl=True,
                            path='/api/v1/influxdb')

    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "testnode",
            },
            "time": datetime.utcnow().isoformat(),
            "fields": {
                "value": 0.96
            }
        }
    ]
    print(client.write_points(json_body))


if __name__ == "__main__":
    main()
