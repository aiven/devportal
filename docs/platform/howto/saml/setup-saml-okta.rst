Setting up SAML authentication with Okta
========================================

**Requirements**

You first need to create an Aiven account and an Aiven account
authentication method. Account is a top level concept that can be
associated with multiple different projects and with which you can make
corporate level configuration like the authentication setup. You can do
this in Aiven Console.

Creating the Aiven account
--------------------------

Once you have logged into the Aiven Console, you should see your
projects in the top left of your screen. Click the current project to
open the project select and click ``See all projects & accounts`` . This should
open a Projects & Accounts modal.

On the Projects & Accounts modal, click on ``Create account`` and you
will be taken to a page where you provide a **name** , **project(s)** to
link it to and the option to invite other admins.

Once created, you will see an overview of the account just created. A
tab, called ``Authentication`` , will let you add a new method (in this
case: **SAML** ) and configure them.

Clicking on ``Add Authentication Method`` creates a dialog where you can
**name** your ``Method Name``, specify the **SAML** for ``Method Type`` and a default **team** you
would want members to join.

Once you click ``Add`` , you will see the configuration URLs for your
Identity Provider (do not worry about making a note of these, you can
access them at any time).

For now, we are done with the Aiven side of this, let's move on to Okta
and create our application.

Okta integration
----------------

This is a two step process. We will first create the SAML SP-Initiated
authentication flow, then create a bookmark app that will redirect to
the Aiven console's login page.

Creating the SP-Initiated authentication application
----------------------------------------------------

Login to the ``Admin`` portal and navigate to the ``Applications`` tab.
Click on the ``Create a new app integration`` button. You
should see the ``Create SAML Integration`` form:

Select **SAML 2.0** for the ``Sign on method``, then click ``Next``.

In the following form, you can give the app a name (e.g. "Aiven SAML"),
logo and set it's visibility for your Okta users. Once this is done,
click ``Next``.

Next step comes the SAML configuration form. The following fields need to be
set:

-  ``Single sign on URL`` : This value is visible in Aiven Console on
   the newly created Authentication method page. The URL format is
   ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_auth_method_id}/acs``

-  ``Audience URI (SP Entity ID)`` : This value is visible in Aiven
   Console on the newly created Authentication method page. The URL
   format is
   ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_auth_method_id}/metadata``

-  | ``Default RelayState`` : This is the homepage of the Aiven Console
     and is important for IdP initiated sign-on to function correctly.
   | ``https://console.aiven.io/ - Aiven Console``
   | ``https://console.gcp.aiven.io/ - GCP Marketplace Console``
   | ``https://console.aws.aiven.io/ - AWS Marketplace Console``

-  ``Attribute statements`` should have an entry where ``name`` is ``email``
   and ``value`` ``user.email``

Once this is done, click ``Next`` then ``Finish``. You will be redirect to
your application in Okta.

Setting up the Okta application in Aiven
----------------------------------------

Once the application is created, you need to provide the application
data to Aiven. These data can be found in the ``Sign On`` tab of the
application on Okta, after clicking the ``View Setup Instructions``.

.. image:: /images/platform/howto/saml/okta-view-saml-instructions.png
   :alt: View SAML setup instructions in Okta

This will open a new tab where you will get the following required information to
finalize the setup to use Okta with Aiven in the next step.

* ``Identity Provider Signle Sign-On URL``
  
* ``Identity Provider Issuer``

* ``X.509 Certificate``

You can then go back to **Aiven Console** and finalize the configuration in
the **Authentication** method page.

Filled the following information with values from Okta SAML information from the previous step:

* ``SAML IDP Url`` -> ``Identity Provider Signle Sign-On URL``
   
* ``SAML Entity ID`` -> ``Identity Provider Issuer``

* ``SAML Certificate`` -> ``X.509 Certificate``

.. Important::
   Toggle ``Enable IdP login`` and ``Enable authentication method`` before clicking ``Edit Method`` to save the settings.

When this is done use the ``Account Link URL`` on the authentication
configuration page to link your Okta account and Aiven profile. You can also
invite other members of your team to login or signup to Aiven using Okta
via the Signup link shown in the Authentication method page. **Note:
Remember that they will need to be assigned to the Aiven application in
Okta for it to be possible.**

Assigning users to the Okta application
---------------------------------------

For your users to be able to login using SAML, you need to assign to the
Okta application you just created. To do that, go to the ``Assignments``
tab of the application. Then click on the ``Assign`` drop-down button and assign
individual users or groups to the application.

Troubleshooting
---------------

Authentication failed
~~~~~~~~~~~~~~~~~~~~~

When launching Aiven SAML application getting the following error.


   **Authentication Failed**
   
   Login failed.  Please contact your account administrator for more details.

Check Okta authentication in Aiven console if **Enable IdP login** and **Enable authentication method** are
enabled.


Invalid ``RelayState``
~~~~~~~~~~~~~~~~~~~~~~

If you get this error, it means that you are attempting an
IdP-initiated auth flow, i.e. you clicked the Aiven SAML app from the
Okta UI. Previously, Aiven did not support IdP-initiated flows, but
now it is possible if you set the Default ``RelayState`` in Okta to

|  ``https://console.aiven.io/ - Aiven Console``
| ``https://console.gcp.aiven.io/ - GCP Marketplace Console``
| ``https://console.aws.aiven.io/ - AWS Marketplace Console``

My Okta password does not work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure that you use the ``Account Link URL`` to add the Okta
Authentication method to your Aiven profile. Once linked, you should get
the choice of multiple sign-in methods as well as see the other
Authentication method in ``User Information`` -> ``Authentication``.

I need help
~~~~~~~~~~~

Thank you for your patience while we develop this feature (and many
others) for the Aiven platform. Our `support
team <https://help.aiven.io/>`__ is always on hand to help. When the
feature has been released, we will update this article but please
contact us if you would like to be alerted when this is available.