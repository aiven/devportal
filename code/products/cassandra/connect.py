import argparse
import logging
import os

import ssl
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy


def cassandra_example(args):
    auth_provider = PlainTextAuthProvider(args.USER, args.PASSWORD)
    ssl_options = {"ca_certs": args.SSL_CERTFILE, "cert_reqs": ssl.CERT_REQUIRED}
    with Cluster([args.HOST], port=args.PORT, ssl_options=ssl_options, auth_provider=auth_provider,
                 load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='aiven')) as cluster:
        with cluster.connect() as session:
            # Create a keyspace
            session.execute("""
                CREATE KEYSPACE IF NOT EXISTS example_keyspace
                WITH REPLICATION = {'class': 'NetworkTopologyStrategy', 'aiven': 3}
            """)

            # Create a table
            session.execute("""
                CREATE TABLE IF NOT EXISTS example_keyspace.example_python (
                    id int PRIMARY KEY,
                    message text
                )
            """)

            # Insert some data
            session.execute("""
                INSERT INTO example_keyspace.example_python (id, message)
                VALUES (%s, %s)
            """, (1, "hello world"))

            # Read it back
            for row in session.execute("SELECT id, message FROM example_keyspace.example_python"):
                print("Row: id = {}, message = {}".format(row.id, row.message))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--HOST', help="Cassandra host", required=True)
    parser.add_argument('--PORT', help="Cassandra port", required=True, type=int)
    parser.add_argument('--USER', help="Cassandra username", default='avnadmin')
    parser.add_argument('--PASSWORD', help="Cassandra password", required=True)
    parser.add_argument('--SSL-CERTFILE', help="Path to cluster CA certificate", default='ca.pem')
    args = parser.parse_args()

    if not os.path.isfile(args.SSL_CERTFILE):
        logging.error("Could not locate CA certificate at path: %s. \n"
                      "You can download it from the Overview tab in the Aiven console, "
                      "or retrieve it with the Aiven command line client (https://github.com/aiven/aiven-client): \n"
                      "'avn project ca-get --project <project-name> --target-filepath ./ca.pem'" % args.SSL_CERTFILE)
        exit(1)

    cassandra_example(args)


if __name__ == '__main__':
    main()