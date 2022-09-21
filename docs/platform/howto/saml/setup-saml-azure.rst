Set up SAML with Microsoft Azure Active Directory
=================================================

SAML ( *Security Assertion Markup Language* ) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. To read more about SAML check the :doc:`dedicated page <saml-authentication>`.

The following is the procedure to setup SAML with `Microsoft Azure Active Directory <https://azure.microsoft.com/en-us/services/active-directory/>`_.

Prerequisite steps in Aiven
----------------------------

1. Login to the `Aiven Console <https://console.aiven.io>`_

2. Under **Projects** in the top left, click the drop down arrow and then on **See All Accounts**

3. Click on the Account you want to edit or create a new one

4. Select the **Authentication** tab

5. Create a new Authentication Method, call it `Active Directory` (or similar) and then
choose the team to add invited people to (or leave it blank)

Setup on Microsoft Azure
-------------------------

1. Log in to Microsoft Azure
2. Navigate to **Enterprise applications** either by using the tiles or the search bar
3. Use the left column navigation to go to **All applications** and click **New application**
4. Select the **Add from the gallery** search bar to search and use the **Azure AD SAML Toolkit** 

   .. Note:: 
  
      You can use anything you like for the App name, such as `Aiven SAML`

5. Click the **Add** button
6. Use the navigation to go back the **Enterprise applications** list 

   .. Warning::

    The newly created application might not be visible yet. In this case, select the **All applications** filter and apply it to be able to see the new application in the list. 
    
7. Click on the new application name (as example `Aiven SAML`) to enter the configuration
8. Navigate to the **Single sign-on** configuration using the left column
9. Select **SAML** when ask to select a single sign-on method
10. You'll need to edit the **Basic SAML Configuration** settings with the following data:

.. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Identifier (Entity ID)``
        - ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/metadata``
      * - ``Reply URL (Assertion Consumer Service URL)``
        - ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/acs``
      * - ``Sign on URL``
        - ``https://console.aiven.io``


11. Once edited, click **Save** on top of the edition zone
12. Edit the **User Attributes & Claims** section
13. Click **Add a new claim** and create an attribute with the following data:

.. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Name``
        - ``email``
      * - ``Source``
        - Select ``Attribute``
      * - ``Source Attribute``
        - ``user.email``

14. Download the **Certificate (Base64)** from the **SAML Signing Certificate** section

15. Assign users to be able to access the login method using the left column navigation to go to **Users and groups** and click **Add user** on top of the list

16. Select the users that will be able to log in to Aiven with your Microsoft Azure Active Directory and click on the **Assign** button at the bottom of the page when you're done

Finish the configuration in Aiven
----------------------------------

The data you need to finish the setup on Aiven is found in the **Single sign-on** settings. We are interested in the **Set up Aiven SAML** section

1. In the Aiven Console, edit your authentication method and provide the ``SAML IDP URL`` to the ``Login URL`` from Microsoft Azure

2. Set the ``SAML Entity ID`` to the ``Azure AD Identifier`` from Microsoft Azure

3. Paste the certificate you downloaded earlier into ``SAML Certificate``

4. Click on Save 

5. Make sure the authentication method is **enabled**, then use the: 

   * **Signup URL** to invite new people
   * **Account link URL** for people already having an Aiven login


Troubleshooting
---------------

Contact your administrator
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get an error message suggesting to "contact your administrator", check the following:

1. Navigate to the Microsoft Azure Active Directory user profile for the users
2. Check whether the **Contact Info** => **Email** field is populated or blank
3. If it is blank, there are two possible solutions:

   * If the field **Identity** => **User Principal Name** is an email address.
     
     Change the **User Attributes & Claims** to be ``email = user.userprincipalname`` and try the login/registration flows again.

   * If all user accounts have the **Contact Info** => **Alternate email** populated
  
     Change the **User Attributes & Claims** to be ``email = user.othermail``

If you still have login issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to  check the process step by step. The errors shown in the tracker should help you to debug the issues. If it does not work, you can request help by sending an email at support@Aiven.io.
