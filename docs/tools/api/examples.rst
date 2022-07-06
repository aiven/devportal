API examples
============

Here is an example to get you started with the Aiven API using curl. Replace ``{TOKEN}`` with your own value of the authentication token.

List of cloud regions
---------------------

.. code::

  curl -H "Authorization: Bearer TOKEN" https://api.aiven.io/v1/clouds

The response looks something like this

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

For most endpoints where a cloud is used as an input, the `cloud_name` from this result is the field to use.


