Connect to Apache Kafka® with Franz
===================================

`Franz`_ is a native Mac and Windows desktop client for Apache Kafka.

Using Client Certificate Authentication
---------------------------------------

1. Visit the **Service Overview** page for your Aiven for Apache Kafka® service.
2. Download the **Access Key**, **Access Certificate** and **CA Certificate**.
3. Rename the **Access Key** from ``service.key`` to ``service.key.pem``:

::

   mv service.key service.key.pem

4. Combine the **Acess Certificate** and **CA Certificate** files into one:

::

   cat service.cert ca.pem > combined.pem

3. In Franz, choose **New Connection...** and

   * enter your cluster **Host** and **Port** under the **Bootstrap
     Host** and **Port** fields,
   * tick the **Enable SSL** checkbox,
   * click the **SSL Key...** button and select the ``service.key.pem`` file,
   * click the **SSL Cert...** button and select the ``combined.pem`` file.

.. image:: /images/products/kafka/franz-ssl-config.png
    :alt: Screenshot of the Franz connection configuration window.

4. Finally, click **Connect** to connect to your cluster.

Once connected, you can read the `Franz Manual`_ to learn more about using this tool.

.. _Franz: https://franz.defn.io/
.. _Franz Manual: https://franz.defn.io/manual/
