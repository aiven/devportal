Aiven Command-line interface tips and tricks
============================================

While most of your Aiven service administration can be done straight
from the `console <https://console.aiven.io/>`__ , we've compiled a
`blog
post <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/>`__
containing tips and tricks for working with our Command Line Interface,
which we've linked and outlined below.

These are complimentary to what's available on `Aiven client's github
profile <https://github.com/aiven/aiven-client>`__ , so be sure to check
out both; both are linked in order below.

-  | `Installing the Aiven
     CLI <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/#installing-the-cli>`__
   | More on
     `Github <https://github.com/aiven/aiven-client#installation>`__

-  | `Logging in and logging
     out <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/#logging-in-and-out>`__
   | More on
     `Github <https://github.com/aiven/aiven-client#login-and-users>`__

-  `Working with
   projects <https://github.com/aiven/aiven-client#projects>`__

-  | `Viewing clouds, services, regions, and
     plans <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/#viewing-csrp>`__
   | More on Github:
     `Clouds <https://github.com/aiven/aiven-client#clouds>`__ and
     `Services <https://github.com/aiven/aiven-client#services>`__

-  | `Creating, viewing, powering on or off, and deleting
      services <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/#doing-services>`__
   | More on
     `Github <https://github.com/aiven/aiven-client#launching-services>`__

-  `Viewing and filtering service
   logs <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/#doing-logs>`__

-  `Using AVN CLI
   Help <https://aiven.io/blog/command-line-magic-with-the-aiven-cli/#help-misc>`__

.. _h_4002f0d977:

Enable ``aiven-cli`` Login when using “Sign in with Google”
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please note that if you are using Google OAuth Single Sign-On (“Sign in
with Google” in `Aiven’s console <https://console.aiven.io/>`__ ),
trying to login with the same credentials via the ``aiven-cli`` will
result in a failure with an ``Authentication failed`` message.

The **Aiven Password** login method used by ``aiven-cli`` needs to be
enabled in `Aiven’s Profile Authentication
page <https://console.aiven.io/profile/auth>`__

|image0|

Once enabled you’ll be able to login with your account email and the
defined Aiven’s password from ``aiven-cli`` .

.. |image0| image:: /images/tools/cli/tips-and-tricks.png