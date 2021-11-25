Connect to OpenSearch cluster with NodeJS
=========================================

The most convenient way to work with the cluster when using NodeJS is to rely on `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_. Follow its ``README`` file for installation instructions.

To connect to the cluster, you'll need ``service_uri``, which you can find either in the service overview in the `Aiven console <https://console.aiven.io>`_ or get through the Aiven command line interface `service command <https://developer.aiven.io/docs/tools/cli/service.html#avn-service-get>`_. ``service_uri`` contains credentials, therefore should be treated with care.

We strongly recommend using environment variables for credential information. A good way to do this is to use ``dotenv``. You will find installation and usage instructions `on its library's project page <https://github.com/motdotla/dotenv>`_, but in short, you need to create ``.env`` file in the project and assign ``SERVICE_URI`` inside of this file.

Add the require line to the top of your file::

    require("dotenv").config()

Now you can refer to the value of ``service_uri`` as ``process.env.SERVICE_URI`` in the code.

Add the following lines of code to create a client and assign ``process.env.SERVICE_URI`` to the ``node`` property. This will be sufficient to connect to the cluster, because ``service_uri`` already contains credentials. Additionally, when creating a client you can also specify ``ssl configuration``, ``bearer token``, ``CA fingerprint`` and other authentication details depending on protocols you use.


.. code:: javascript

    const { Client } = require('@opensearch-project/opensearch')

    module.exports.client = new Client({
      node: process.env.SERVICE_URI,
    });

The client will perform request operations on your behalf and return the response in a consistent manner.