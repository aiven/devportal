Aiven CLI
=========

Aiven offers an installable CLI (command line interface) tool. You can find it `on GitHub <https://github.com/aiven/aiven-client>`_.

Getting started
---------------

The ``avn`` client is an ideal way to use Aiven's services in a scriptable way. This tool accesses the same API that powers the web console.

Install
'''''''

The ``avn`` utility is a Python package, so you can install using ``pip``::

    pip install aiven-client

Check your install by running ``avn`` and looking for usage output.


Authenticate
''''''''''''

There are two options for authenticating. The first is to use your username, and then enter your password when prompted::

  avn user login <you@example.com>

You can also use an access token (this is the recommended route if you use SSO), with a command like::

  avn user login <you@example.com> --token

This command will prompt you for a token rather than a password.

Commands
--------

Top-level commands for the Aiven CLI are listed here, along with some information about the features found in each section.

``account``
'''''''''''

Handle the accounts you have access to, and also configure the teams for the accounts.

Find more info on the help article about `Accounts, Teams, Members and Roles <https://help.aiven.io/en/articles/4206498-accounts-teams-members-and-roles>`_


``billing-group``
'''''''''''''''''

A set of administrative commands to set up billing groups and manage which projects should be linked to which billing group. Find more information in the `User Guide for Billing Groups <https://help.aiven.io/en/articles/4720981-using-billing-groups-via-cli>`_.

The billing group command also enables access to the credit code features, and detailed invoice line data.


``card``
''''''''

Manage the payment cards on your account.

:doc:`See detailed command information <cli/card>`.


``cloud``
'''''''''

Use ``avn cloud list`` to see all the currently-available clouds on Aiven. This is useful for looking up the cloud name to use with ``service`` commands.


``credits``
'''''''''''

Claim or view the history of credit codes.

:doc:`See detailed command information <cli/credits>`.

``events``
''''''''''

Inspect the events on your account such as the services created/deleted, and which users triggered each event.

:doc:`See detailed command information <cli/events>`.

``help``
''''''''

Detailed help on using the CLI.

``mirrormaker``
'''''''''''''''

Manage the replication flows for MirrorMaker2.


``project``
'''''''''''

Manage all the projects on your Aiven account, and switch which one is the default option for ``avn`` commands. Manage project invitations for all users.

Download the CA cert for this project (CA certs are common for all services in a project).

``service``
'''''''''''

The kitchen sink! All the commands specific to a service are available here.


``ticket``
''''''''''

An alternative support ticket interface to either email or the chat widget found on our web console. Create or list tickets.

``user``
''''''''

Log in/out and manage your user tokens here. You can also create other users.

``vpc``
'''''''

Manage your VPC configuration including user/peer networks.

General usage
-------------

Try the ``--json`` switch to any command to get more information, in a JSON format.
