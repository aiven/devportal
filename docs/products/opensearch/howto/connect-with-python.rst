Connect to OpenSearch cluster with Python
=========================================

One nice way to interact with your cluster is by using the `Python OpenSearch client <https://github.com/opensearch-project/opensearch-py>`_. 
It provides an easy syntax to send commands to your OpenSearch cluster. Follow its ``README`` file for installation instructions.

In order to connect with the cluster, it is necessary to have the **Service URI** setting listed on the **Overview** page or can be accessed via the Aiven command line interface `service command <https://developer.aiven.io/docs/tools/cli/service.html#avn-service-get>`_. ``service_uri`` contains credentials, therefore should be treated with care.

The **Service URI** has information in the following format:

.. code:: bash

    <https://<user>:<password>@<host>:<port>

As you can see it contains sensitive information; therefore, 
for security reasons is recommended to use environment variables for your credential information. You can use the ``dotenv`` `Python library <https://pypi.org/project/python-dotenv/>`_ to help to manage with your environment variables. Follow its ``README`` file for installation instructions.

After is installed, you need to create ``.env`` file in the root directory of your project with the ``SERVICE_URI`` on it::

    SERVICE_URI=<https://<user>:<password>@<host>:<port>

And import it in your Python script.

.. code:: python

    import os
    from dotenv import load_dotenv
    load_dotenv()
    SERVICE_URI = os.getenv("SERVICE_URI")

Now, you can use it as a string variable saved in the ``SERVICE_URI``.

To connect with your cluster, you can import OpenSearch and create an instance of the class. In this example, we will be giving the full path and enabling the ``use_ssl`` to secure our connection. 

.. code:: python

    from opensearchpy import OpenSearch
    opensearch = OpenSearch(SERVICE_URI, use_ssl=True)

.. note::
    There are other ways that you can create your OpenSearch instance configuring parameters such as ``verify_certs``, ``ssl_assert_hostname`` and others authentication details that can be configured. 
    
    Check `documentation <https://github.com/opensearch-project/opensearch-py>`_ for more details.

Congrats 🥳, you have a Python OpenSearch client class instance ready to be used to perform request operations and send responses in an easy way. 

Enjoy it!
