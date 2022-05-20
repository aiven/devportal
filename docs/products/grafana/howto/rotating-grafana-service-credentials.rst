Rotating Grafana® service credentials
====================================

In the interests of security, it is best practice to rotate credentials from time-to-time.

For Grafana®, a few steps need to be performed manually to do this. You will need to have access to a web browser and need to have `aiven-client (avn) <https://developer.aiven.io/docs/tools/cli.html>`_ installed.

1. Login with the avnadmin credentials via the web browser to the Grafana instance from the Service URI displayed on the Aiven Console.

2. In the bottom-left of Grafana is a small avatar displayed above the help icon. Hover over it, and click Change password.

.. image:: /images/products/grafana/grafana-credentials.png

3. Change the password and make a note of it somewhere safe.

4. Login to aiven-client and then run the following command to update the stored password in the console :: 
    
    avn service user-password-reset \
    --username avnadmin \
    --new-password <new password noted above> \
    <service name>
    
For example ::

    avn service user-password-reset \
    --username avnadmin \
    --new-password my_super_secure_password \
    my-grafana-service

5. Refresh the Aiven Console and the new password should now be displayed for the avnadmin user.