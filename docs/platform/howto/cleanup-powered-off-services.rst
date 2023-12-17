Periodic cleanup of powered-off services
========================================

The Aiven platform provides a way to power-off services to stop accumulating usage costs when not in use. However, leaving them powered-off for an extended period of time comes with disadvantages.

The Aiven platform receive regular maintenance updates to keep the services updated with the latest supported versions upstream, including fixes to bugs, security vulnerabilities, and overall improvements to performance and memory consumption.

Keeping services in powered-off state for a long time lowers the feasibility of a smooth upgrade path, making it harder for Aiven to continue supporting your needs.

.. note:: 
  
    * It is recommended that you regularly review your services and delete those that are no longer needed. This allows Aiven to focus on supporting the services that you actively use and better utilize platform resources.
    
    * If a service has been powered off for 90 days, you will receive email notifications reminding you that the service has been inactive for a prolonged period. If the service remains powered off for 180 consecutive days, it is subject to automatic deletion.


Delete a powered-off service
------------------------------

1. In `Aiven Console <https://console.aiven.io/>`_, select **Services** in the left navigation bar to display a list of all services.
2. On the **Services** page, use the search bar to locate a specific powered off service or the filter to display a list of services with status **Powered off**.
3. Select the powered off service to access its **Overview** page, and select **Delete service** from the meatballs menu in the top right corner.
4. In the **Delete confirmation** window, enter the name of the service to delete and select **Delete** to confirm the action.
