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

1. When logged in to Microsoft Azure, go to **Enterprise applications** (either by using the tiles or the search bar), the use the left column navigation to go to **All applications** and click **New application**.
2. Then use the **Add from the gallery** search bar to search and use the **Azure AD SAML Toolkit**. You can use anything you like for the App name, such as `Aiven SAML`, and click the **Add** button.
3. Use the navigation to go back the Enterprise applications list. The application might not be visible yet, and it's possible you have to select the **All applications** filter and apply it to be able to see it in the list. Once it's visible in the list, click it to go to its configuration.
4. Go to the **Single sign-on** configuration using the left column and select **SAML** when ask to select a single sign-on method.

You'll need to edit the **Basic SAML Configuration** settings with the following data:

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

Then click **Save** on top of the edition zone.

5. Next, edit the **User Attributes & Claims** section, click **Add a new
claim** and create an attribute with the following data:

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

6. Download the **Certificate (Base64)** from the **SAML Signing
Certificate** section.

7. Now you need to assign users to be able to access the login method. Use the left column
navigation to go to **Users and groups** and click **Add user** on top of
the list. You can then select the users that will be able to log in to
Aiven with your Microsoft Azure Active Directory and click on the **Assign** button at the bottom
of the page when you're done.

Finish the configuration in Aiven
----------------------------------

1. The data you need to finish the setup on Aiven is found in the **Single sign-on** settings. We are interested in the **Set up Aiven SAML** section

2. In the Aiven Console, edit your authentication method and provide the ``SAML IDP URL`` to the ``Login URL`` from Microsoft Azure

3. Set the ``SAML Entity ID`` to the ``Azure AD Identifier`` from Microsoft Azure

4. Paste the certificate you downloaded earlier into ``SAML Certificate``

5. Save that and you are good to go! Make sure the authentication method is enabled and you can then use the **Signup URL** to invite new people and **Account link URL** for those that already have an Aiven login.


Troubleshooting
---------------

Contact your administrator
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get an error message saying contact your administrator, try the
following:

Check the Microsoft Azure Active Directory user profile for the users and see if the **Contact
Info** => **Email** field is populated or blank? If it is blank, there are two possible solutions:

#. Is the **Identity** => **User Principal Name** field an email address? If so, try the solution below. If not, check case
    **Solution:** change the **User Attributes & Claims** to be ``email = user.userprincipalname``. Try the login/registration flows again.

#. Do you know if all of you user accounts will have the **Contact Info** => **Alternate email** populated?
    **Solution:** change the **User Attributes & Claims** to be ``email = user.othermail``

Still stuck?
~~~~~~~~~~~~

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to  check the process step by step. The errors shown in the tracker should help you to debug the issues. If it does not work, you can request help by sending an email at support@Aiven.io.
