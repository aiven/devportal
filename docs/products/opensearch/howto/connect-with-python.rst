Connect to OpenSearch cluster with Python
=========================================

You can interact with your cluster with the help of the `Python OpenSearch client <https://github.com/opensearch-project/opensearch-py>`_. 
It provides a convenient syntax to send commands to your OpenSearch cluster. Follow its ``README`` file for installation instructions.

To connect with your cluster, you need the **Service URI** of your OpenSearch cluster. You can find the connection details in the section **Overview** on `Aiven web console <https://console.aiven.io>`_.  Alternatively, you can retrieve it via the ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.  Notice that ``service_uri`` contains credentials; therefore, should be treated with care.


The **Service URI** has information in the following format:

.. code:: bash

    <https://<user>:<password>@<host>:<port>

For security reasons is recommended to use environment variables to save your credential information. You can use the ``dotenv`` `Python library <https://pypi.org/project/python-dotenv/>`_ to manage your environment variables. Follow its ``README`` file for installation instructions.

After is installed, you need to create ``.env`` file in the root directory of your project with the ``SERVICE_URI`` on it::

    SERVICE_URI=<https://<user>:<password>@<host>:<port>

And import it in your Python script.

.. code:: python

    import os
    from dotenv import load_dotenv
    load_dotenv()
    SERVICE_URI = os.getenv("SERVICE_URI")

Now, you can use it as a string variable saved in the ``SERVICE_URI``.

You can import OpenSearch and create an instance of the class to connect with your cluster. In this example, we will be giving the full path and enabling the ``use_ssl`` to secure our connection. 

.. code:: python

    from opensearchpy import OpenSearch
    opensearch = OpenSearch(SERVICE_URI, use_ssl=True)

.. note::
    There are other ways that you can create your OpenSearch instance configuring parameters such as ``verify_certs``, ``ssl_assert_hostname`` and others authentication details that can be configured. 
    
    Check `documentation <https://github.com/opensearch-project/opensearch-py>`_ for more details.

Those are the steps to create a Python OpenSearch client class instance that can be used to perform request operations and send responses to your cluster.
