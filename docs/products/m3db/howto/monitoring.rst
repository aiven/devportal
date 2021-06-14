Monitor Aiven Services with M3DB
================================

M3DB is a perfect fit for a monitoring platform. It is designed to handle large volumes of metrics, and it's very good at that. Whether you are already working at scale or just curious about M3DB and monitoring, setting up an M3DB to monitor your existing Aiven services (or new ones if you like) is a really nice way to get started with this platform.

Start from the **Service Overview** page of the service you would like to monitor with M3. So if you're going to track the metrics of your PostgreSQL service on Aiven, then start on the PostgreSQL service overview page.

1. Under "Manage Integrations", look for "Metrics" (not available on all services yet).

2. Select whether to use an existing M3DB service if you already have one you want to use, or you create a new one here by giving the cloud and region to use, and supplying a name for the service.

That's it! Were you expecting something more complicated?

A good way to see the metrics being collected is in Grafana. We have an article for that too: :doc:`grafana`.
