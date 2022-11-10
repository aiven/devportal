Restrict network access to your service
========================================

It is possible to restrict access to your service to a single IP, and address block, or any combination of both. By default the service is publicly accessible.

1. Go to your **Services**, and open the service you want to restrict.
2. On the **Overview** tab, scroll down to **Allowed IP Addresses** and click **Change**. 
3. Enter your address or address block using the CIDR notation. You can specify several addresses or blocks or combination of both in a single change.
4. Click **Save Changes**.

You can also use the :ref:`dedicated service update function <avn-cli-service-update>` to create or update the IP filter for your service via the :doc:`Aiven CLI </docs/tools/cli>`.
