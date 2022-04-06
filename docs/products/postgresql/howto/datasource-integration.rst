Connect two PostgreSQL® services via datasource integration
===========================================================

There are two types of datasource integrations you can use with Aiven for PostgreSQL®: :doc:`Aiven for Grafana® <visualize-grafana>`, and another Aiven for PostgreSQL® service.  If you are connecting two PostgreSQL® services together, perhaps to :doc:`query across them <use-dblink-extension>`, but still want to have a restricted IP allow-list, then you will need to use the ``Datasource`` service integration.

Whenever a service node needs to be recycled, e.g. for maintenance, a new node is created with a new IP address.  As the new IP address cannot be predicted, if you want to maintain a connection between two PostgreSQL services your choices are either to have a very broad IP allow-list (which might be acceptable in the private IP-range of a project VPC) or to use the ``Datasource`` service integration to dynamically create an IP allow-list entry for the other PostgreSQL service.

Integrate two PostgreSQL services
---------------------------------

1. On the service overview page for your PostgreSQL service, go to **Manage Integrations** and choose the **datasource** option.

2. Choose either a new or existing PostgreSQL service.

Now your PostgreSQL will allow IP traffic from the chosen PostgreSQL service, regardless of what its IP address is.

