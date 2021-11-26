Accessing Aiven for OpenSearch Dashboards from Chrome
=====================================================

Access to Aiven for OpenSearch Dashboards requires a valid username and password (HTTP Basic Authentication.)  The service overview page in the `Aiven console <https://console.aiven.io>`_ includes a link directly to OpenSearch Dashboards which embeds the username and password in the URL, allowing one-click access to Kibana from the Aiven console.

Unfortunately Chrome has removed support for URLs including a username and password in its version 59 (released in June 2017), causing Chrome to display a network error when such a link is accessed.  See https://www.chromestatus.com/feature/5669008342777856 and https://bugs.chromium.org/p/chromium/issues/detail?id=731618 for more information about the change in behavior.

To access your Aiven for OpenSearch Dashboards using Chrome please copy the Dashboards URL to your browser's URL bar and manually enter the username and password that are shown on your Aiven service overview page.