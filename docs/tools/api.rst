Aiven API overview
==================

The Aiven API allows you to perform any tasks on Aiven from a client of your choice.

API quickstart
--------------

* You will need an authentication token from the `profile section of your Aiven console <https://console.aiven.io/profile/auth>`_.

* Check the `API docs and OpenAPI spec <https://api.aiven.io/doc/>`_ for the available endpoints.


Calling the Aiven API
---------------------

The `Aiven API <https://api.aiven.io/doc/>`_ is a traditional HTTP API. All our own tools, such as the `web console <https://console.aiven.io>`_ and ``avn`` CLI use this API.

.. mermaid::

    sequenceDiagram
        participant Client
        participant Aiven

        Client->>Aiven: Request with access token
        Aiven->>Client: Response {JSON}

Authorization
'''''''''''''

Obtain an authentication token from your `Aiven console <https://console.aiven.io/profile/auth>`_. This will be sent as an ``Authorization`` header, like this::

    Authorization: Bearer <TOKEN>

Handling JSON responses
'''''''''''''''''''''''

The `Aiven API <https://api.aiven.io/doc/>`_ returns information in JSON format, sometimes a lot of
information. This is perfect for machines but not ideal for humans. We like to
use a tool like ``jq`` (https://stedolan.github.io/jq/) to make things easier to read and manipulate.

Aiven API and Postman
'''''''''''''''''''''''

If you prefer an even more friendly tool, we have a blog post about `using Postman with Aiven's API <https://aiven.io/blog/your-first-aiven-api-call>`_ including how to import a Postman collection and spin up Aiven services with Postman.

