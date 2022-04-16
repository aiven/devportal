Resource capability of Aiven for PostgreSQL® plans
==================================================

When creating or updating an Aiven service, the plan that you choose will drive the specific resources (CPU / memory / disk IOPS / etc) powering your service.  Aiven is a cloud data platform, so the underlying instance types are chosen appropriately for the type of service - elements like local NVMe SSDs, sufficient memory for the expected workloads, fast access to backup storage, ability to encrypt the disks, etc all contribute to the choice of which instance types to use on which cloud platforms.  In addition, particular instance types are sometimes not available in a specific cloud region.  There is no one-size-fits-all when it comes to choosing the optimal instance type, so Aiven takes all of these things into account to select the right instance type for a given service.

This still leaves the question of how much work can my PostgreSQL® service actually do?  The only way to answer this definitively is to benchmark it with your specific workload, in a representative setup.  It will be affected by more than just the instance type: network throughput, latency to your applications, number of connections active at the time, type of TLS encryption in use, and a whole range of things specific to the cloud environment can contribute to a service's expected performance.

Aiven uses `industry-standard benchmarks <https://aiven.io/blog/aiven-for-postgresql-13-performance-on-gcp-aws-and-azure-benchmark>`_ to offer guidance about the right plan for your workload, but the best way to know how your application will work is to benchmark it in your setup.  You can move between plans, scaling up and down, without any downtime in order to try different sizes.

