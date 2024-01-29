How to access Aiven services from Google Cloud Functions via VPC peering
========================================================================

Once you have created a :doc:`VPC on the Aiven platform <manage-vpc-peering>` and :doc:`set up VPC peering on GCP <vpc-peering-gcp>`, you can follow these instructions to create **Serverless VPC access connector** and **Google Cloud Function**.

By default, **Google Cloud Functions** can only access Internet and is not able to access your GCP VPC or Aiven VPC. For **Google Cloud Functions** to access VPC, **Serverless VPC access connector** is required. Under the hood, **serverless VPC access connector** consists of two or more Google-managed VM that forward requests (and perform NAT) from Cloud Functions to your GCP VPC and Aiven VPC.

.. mermaid::

    graph LR;

        GCF(Google Cloud Function) --TCP session--> Conn(Serverless VPC access connector) --TCP session--> VPC(Your GCP VPC and Aiven VPC)

First, create **Serverless VPC access connector**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open GCP console and under **Navigation menu**, **Networking** section, **VPC network** product, select `Serverless VPC access <https://console.cloud.google.com/networking/connectors/list>`_
2. Click **create connector**.

   * **Name**: the connector name of your choice, 25 characters maximum
   * **Region**: must be the region that you are intended to create Cloud Function
   * **Network**: your GCP VPC, which should be peered to Aiven VPC already
   * **Subnet**: select "custom IP range" and enter a /28 private subnet that is not in use.

3. If you have **allowed IP addresses** configured on your Aiven service, please ensure the subnet of **serverless VPC access connector** is listed there

Create **Cloud Function**
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open GCP console and under **Navigation menu**, **Serverless** section, select `Cloud Functions <https://console.cloud.google.com/functions/list>`_
2. Click **create function**

   * **Environment**: your choice, or leave it to the default (2nd gen)
   * **Function name**: the name of your choice, 63 characters maximum
   * **Region**: must be the region that you have the **serverless VPC access connector** created
   * Click and expand the **runtime, build connections and security settings** section, select **Connections** tab, and select the **serverless VPC access connector** you have created.
   * Click **Next**

3. Select the runtime you prefer.

   * **Pitfall**: if you click **test function** here, you will *not* able to access VPC.
   * Click **Deploy**

4. Wait for GCP to deploy the cloud function. Once deployed, use **source** tab to edit the function if needed. 

   * **Pitfall**: if you click **test function** under **source** tab, you will *not* able to access VPC.

5. Select **testing** tab and running test command in Cloud Shell *can* access VPC.


Troubleshooting
~~~~~~~~~~~~~~~

If you cannot access your VPC or Aiven VPC from the Cloud Function, please consider using the following example for troubleshooting purposes.

.. code-block:: python

   # Cound Function 2nd gen, Python 3.11
   import functions_framework
   import socket

   CLOUD_FUNCTION_KEY = 'gcf-aiven-test-CHANGE_ME_FOR_SECURITY_REASON'
   
   @functions_framework.http
   def hello_http(request):
       request_json = request.get_json(silent=True)
   
       if request_json and "cloud_function_key" in request_json and request_json["cloud_function_key"] == CLOUD_FUNCTION_KEY:
           result = ""
           try:
               host = request_json['host']
               port = request_json['port']
               timeout = request_json.get('timeout', 10)
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.settimeout(timeout)
               s.connect((host, port))
               result = "OK"
           except Exception as e:
               result = repr(e)
               pass
           return 'Result: {}\n'.format(result)
       return "HTTP 401\n", 401

The request body should contain

* **CLOUD_FUNCTION_KEY**: Change this to protect your Cloud Function endpoint, especially if it does not require authentication.
* **"host"**: FQDN or IP address if your Aiven service or VM in your GCP VPC.
* **"port"**: Destination TCP port number.

for example (e.g. in the **testing** tab in your **Cloud Function**)

.. code-block:: json

   {
     "cloud_function_key": "gcf-aiven-test-CHANGE_ME_FOR_SECURITY_REASON",
     "host": "fqdn-or-ip-to-your-aiven-service.a.aivencloud.com",
     "port": 12345
   }

It will return "OK" if it can establish TCP 3-way handshaking. "TimeoutError" if it cannot reach the port specified.

If you need help, please contact Aiven support. You can also provide your Cloud Function endpoint and CLOUD_FUNCTION_KEY so it would be more efficient for us to troubleshoot for you.

