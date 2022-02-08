Restricting access to your service
==================================

It is possible to restrict access to your service to a single IP, and address block, or any combination of both. By default the service is publicly accessible.


Restrict access to a service using the console
----------------------------------------------

1. Log in to the Aiven console. 
2. Go to your **Services**, and open the service you want to scale.
3. On the **Overview** tab, scroll down to **Allowed IP Addresses** and click **Change**. 
4. Enter your address or address block using the CIDR notation. You can specify several addresses or blocks or combination of both in a single change.
5. Click **Save Changes**.


Restrict access to a service using the Aiven client (CLI)
---------------------------------------------------------

1. Prepare the command to scale the service.


2. Add the ``service_to_restrict`` parameter to specify the service to which you want to restrict access, and the ``ip_addresses`` for the target plan. The ``ip_addresses`` parameter is a list of addresses or blocks using the CIDR notation separated by commas—``10.0.1.0/24,10.0.2.0/24,1.2.3.4/32``. An example command would be:

    avn service update -c ip_filter=ip_addresses service_to_restrict

The changes are applied immediately.
