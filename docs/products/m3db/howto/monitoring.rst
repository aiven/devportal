Monitor Aiven services with M3DB
================================

M3DB is a perfect fit for a monitoring platform. It is designed to handle large volumes of metrics, and it's very good at that. Whether you are already working at scale or just curious about M3DB and monitoring, setting up an M3DB to monitor your existing Aiven services (or new ones if you like) is a really nice way to get started with this platform.

Start from the **Service Overview** page of the service you would like to monitor with M3. So if you're going to track the metrics of your PostgreSQL® service on Aiven, then start on the PostgreSQL® service overview page.

1. Under "Manage Integrations", look for "Metrics" (not available on all services yet).

2. Choose either a new or existing M3DB service.

   - When creating a new service you will need to select the cloud, region and plan to use. You should also give your service a name. The service overview page shows the nodes rebuilding, and then indicates when they are ready.
   - If you're already using M3DB on Aiven, you can use your M3DB service as a destination for your metrics data. 
   
     .. Note::
     
      If you are a member of multiple Aiven projects with *operator* or *admin* access right, you need to choose the project first then your target M3DB services.

That's it! Were you expecting something more complicated?

A good way to see the metrics being collected is in Grafana®. We have an article for that too: :doc:`grafana`.
