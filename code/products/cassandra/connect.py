import ssl
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

auth_provider = PlainTextAuthProvider(USER, PASSWORD)
ssl_options = {"ca_certs": SSL_CERTFILE, "cert_reqs": ssl.CERT_REQUIRED}
with Cluster([HOST], port=PORT, ssl_options=ssl_options, auth_provider=auth_provider, 
                    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='aiven')) as cluster:
        with cluster.connect() as session:
        # Here you can now read from or write to the database

