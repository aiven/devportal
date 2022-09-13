Aiven API
=========

Use the Aiven API to programmatically perform any task that you can do through the web interface. This is an ideal way to automate tasks involving Aiven at every stage of your workflow.

Common use cases for the Aiven API:

* Use with CI (Continuous Integration) to spin up data platforms on Aiven for use during test runs.

* Integrate with other parts of your existing automation setup to achieve complex tasks.

* Deploy and tear down development or demo platforms on a schedule.

We make the API available to all Aiven users. It is also the engine behind our web console, so you should find that all operations are also available via API.


API quickstart
--------------

* Try `Aiven on Postman <https://www.postman.com/aiven-apis/workspace/aiven/documentation/21112408-1f6306ef-982e-49f8-bdae-4d9fdadbd6cd>`_ and start working with your data platform programmatically.

* Check the `API documentation and OpenAPI description <https://api.aiven.io/doc/>`_ to work with the API directly.

Authentication
--------------

Some endpoints (but not quite all) require authentication. You will need an authentication token from the `profile section of your Aiven console <https://console.aiven.io/profile/auth>`_.

Send this token in the header, using a structure like this, and replacing ``TOKEN`` with your actual API token::

    Authorization: aivenv1 TOKEN

Read more about :doc:Working with API tokens.

Handling JSON responses
-----------------------

The `Aiven API <https://api.aiven.io/doc/>`_ returns information in JSON format, sometimes a lot of
information. This is perfect for machines but not ideal for humans. We like to
use a tool like ``jq`` (https://stedolan.github.io/jq/) to make things easier to read and manipulate.


