Aiven API
=========

Use the Aiven API to programmatically perform any task that you can do through the web interface. This is an ideal way to automate tasks involving Aiven at every stage of your workflow.

Common use cases for the Aiven API:

* Use with CI (Continuous Integration) to spin up data platforms on Aiven for use during test runs.

* Integrate with other parts of your existing automation setup to achieve complex tasks.

* Deploy and tear down development or demo platforms on a schedule.

We make the API available to all Aiven users. It is also the engine behind the Aiven Console, so you should find that all operations are also available through the API.


API quickstart
--------------

* **Postman**: Try `Aiven on Postman <https://www.postman.com/aiven-apis/workspace/aiven/documentation/21112408-1f6306ef-982e-49f8-bdae-4d9fdadbd6cd>`_ and start working with your data platform programmatically.
* **API documentation**: Check the `API documentation and OpenAPI description <https://api.aiven.io/doc/>`_ to work with the API directly.

Authentication
--------------

Most (but not all) endpoints require authentication. You'll need an authentication token from the `profile section of your Aiven console <https://console.aiven.io/profile/auth>`_.

Send this token in the header, using a structure like this, and replacing ``TOKEN`` with your actual API token:

.. code::

   Authorization: aivenv1 TOKEN

Read more about :doc:`authentication tokens </docs/platform/concepts/authentication-tokens>`.

Handling JSON responses
-----------------------

The `Aiven API <https://api.aiven.io/doc/>`_ returns information in JSON format, sometimes a lot of
information. This is perfect for machines but not ideal for humans. Try a tool
like ``jq`` (https://stedolan.github.io/jq/) to make things easier to read and
manipulate.

API examples
------------

In the following examples, replace ``{TOKEN}`` with your own value of the authentication token.

List your projects
++++++++++++++++++

.. code::

  curl -H "Authorization: aivenv1 {TOKEN}" https://api.aiven.io/v1/project

The following is a sample response: 

.. code:: json

    {
      "project_membership": {
        "my-best-demo": "admin",
        "aiven-sandbox": "admin"
      },
      "project_memberships": {
        "my-best-demo": [
          "admin"
        ],
        "aiven-sandbox": [
          "admin"
        ]
      },
      "projects": [
        {
          "account_id": "a225dad8d3c4",
          "account_name": "Aiven Accounts",
          "address_lines": [],
          "available_credits": "0.00",
          "billing_address": "",
          "billing_currency": "USD",
          "billing_emails": [],
          "billing_extra_text": null,
          "billing_group_id": "588a8e63-fda7-4ff7-9bff-577debfee604",
          "billing_group_name": "Billing",
          "card_info": null,
          "city": "",
          "company": "",
          "country": "",
          "country_code": "",
          "default_cloud": "google-europe-north1",
          "end_of_life_extension": {},
          "estimated_balance": "4.11",
          "estimated_balance_local": "4.11",
          "payment_method": "no_payment_expected",
          "project_name": "my-best-demo",
          "state": "",
          "tags": {},
          "tech_emails": [],
          "tenant_id": "aiven",
          "trial_expiration_time": null,
          "vat_id": "",
          "zip_code": ""
        },
        {
          "account_id": "a225dad8d3c4",
          "account_name": "Aiven Accounts",
          "address_lines": [],
          "available_credits": "0.00",
          "billing_address": "",
          "billing_currency": "USD",
          "billing_emails": [],
          "billing_extra_text": null,
          "billing_group_id": "588a8e63-fda7-4ff7-9bff-577debfee604",
          "billing_group_name": "Billing",
          "card_info": null,
          "city": "",
          "company": "",
          "country": "",
          "country_code": "",
          "default_cloud": "google-europe-north1",
          "end_of_life_extension": {},
          "estimated_balance": "4.11",
          "estimated_balance_local": "4.11",
          "payment_method": "no_payment_expected",
          "project_name": "aiven-sandbox",
          "state": "",
          "tags": {},
          "tech_emails": [],
          "tenant_id": "aiven",
          "trial_expiration_time": null,
          "vat_id": "",
          "zip_code": ""
        }
      ]
    }



List of cloud regions
---------------------

This endpoint does not require authorization; if you aren't authenticated then the standard set of clouds will be returned.

.. code::

  curl https://api.aiven.io/v1/clouds

The following is a sample response: 

.. code:: json

  {
    "clouds": [
      {
        "cloud_description": "Africa, South Africa - Amazon Web Services: Cape Town",
        "cloud_name": "aws-af-south-1",
        "geo_latitude": -33.92,
        "geo_longitude": 18.42,
        "geo_region": "africa"
      },
      {
        "cloud_description": "Africa, South Africa - Azure: South Africa North",
        "cloud_name": "azure-south-africa-north",
        "geo_latitude": -26.198,
        "geo_longitude": 28.03,
        "geo_region": "africa"
      },

For most endpoints where a cloud is used as an input, the ``cloud_name`` from this result is the field to use.

Further reading
---------------

Here are some more resources for you:

* Some `API examples on the Aiven blog <https://aiven.io/blog/your-first-aiven-api-call>`_. This post also includes information about importing our OpenAPI description into Postman.
* Learn more about the :doc:`Aiven CLI </docs/tools/cli>`.
