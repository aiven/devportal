Getting started with Aiven for MySQL
====================================

Aiven for MySQL services are managed from the `Aiven
Console <https://console.aiven.io/>`__ .

You can start an Aiven for MySQL service by following the steps laid out
in :doc:`this article </docs/platform/howto/create_new_service>`.

The view returns to the service list, where the new service is shown
with an indicator that it is being created.

Click the service name in the list to go to the " **Overview** " page.
This view shows the connection parameters for your MySQL service and its
current status. You can make changes to the service configuration here,
even while the service is being built. You can find the available
configuration options on the :doc:`reference page <reference/advanced_params>`.

The "Status" indicator says " **REBUILDING** " while the service is
being created. Once the service is up and running, the light changes to
green and the indicator says " **RUNNING** ".

Note that while typically services start in a couple of minutes, the
performance between clouds varies and it can take longer under some
circumstances.

Next steps with Aiven for MySQL
-------------------------------

* Learn how to connect to MySQL:
    - :doc:`from the command line <howto/connect-from-cli>`
    - :doc:`with MySQL workbench <howto/connect-from-mysql-workbench>`

* Connect from your own :doc:`Python application <howto/connect-with-python>`.

