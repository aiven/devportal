Grafana® authentication plugins
##############################

Configure Google, GitHub or GitLab authentication integration to Aiven for Grafana®.
-------------------------------

Grafana supports multiple different authentication plugins, in addition to built-in username and password authentication.

Aiven Grafana has support for Google, GitHub and GitLab authentication. Configuring authentication integration is currently available in Aiven console, or can be configured either with the API or with `Aiven command-line client <https://github.com/aiven/aiven-client>`_ (``avn``).

Please note that enabling this feature requires applying a maintenance upgrade for Grafana services created before September 2018.

Google authentication
---------------------

First, create your Google OAuth keys by following `this article <http://docs.grafana.org/auth/google/>`_ and make a note of your client ID and client secret. Then open your Aiven for Grafana service and navigate to `Advanced Configuration <https://help.aiven.io/en/articles/3601906-advanced-configuration-in-aiven-console>`_ at the bottom of the page. Configure the following options in the advanced configuration:

* ``auth_google.allowed_domains``: set to your G-suite domain

* ``auth_google.client_id``: client ID from Google developer console

* ``auth_google.client_secret``: client secret from Google developer console

Optional:

* ``auth_google.allow_sign_up``: set to true to allow users to sign up via Google authentication. If enabled, each new user is created with "viewer" permission and added to their own newly-created organizations

* ``user_auto_assign_org_role``: specify different permissions (Editor, Admin)

* ``user_auto_assign_org``: set to true to add all new users to the main organization

.. image:: /images/products/grafana/aiven_add_google_oauth.png
    
After setting up authentication integration, it will take a short moment - typically less than a minute - before plugin is enabled in Aiven for Grafana.

GitHub authentication
---------------------

First, create your GitHub application by following `this article <https://grafana.com/docs/grafana/latest/auth/github/>`_ and make note of your application client ID and client secret. Then open your Aiven for Grafana service and navigate to `Advanced Configuration <https://help.aiven.io/en/articles/3601906-advanced-configuration-in-aiven-console>`_ at the bottom of the page. Configure the following options in the advanced configuration:

* ``auth_github.client_id``: client ID from GitHub OAuth apps console

* ``auth_github.client_secret``: client secret from GitHub OAuth apps console

Optional:

* ``auth_github.allow_sign_up``: set to true to allow users to sign up via GitHub authentication. If enabled, each new user is created with "viewer" permission and added to their own newly-created organizations

* ``auth_github.allowed_organizations``: Require an active organization membership for at least one of the given organizations on GitHub.

* ``auth_github.team_ids``: Require an active team membership for at least one of the given teams on GitHub

* ``user_auto_assign_org_role``: specify different permissions (Editor, Admin)

* ``user_auto_assign_org``: set to true to add all new users to the main organization

.. image:: /images/products/grafana/aiven_github_configuration.png

GitLab authentication
---------------------
First, create your GitLab application by following this article and make note of your application client ID and client secret. Then open your Aiven for Grafana service and navigate to Advanced Configuration at the bottom of the page. Configure the following options in the advanced configuration:

* ``auth_gitlab.client_id``: client ID from GitLab OAuth apps console

* ``auth_gitlab.client_secret``: client secret from GitLab OAuth apps console

* ``auth_gitlab.allowed_groups``: limit access to only members of a given group or list of groups

Optional:

* ``auth_gitlab.allow_sign_up``: set to true to allow users to sign up via GitLab authentication. If enabled, each new user is created with "viewer" permission and added to their own newly-created organizations

* ``user_auto_assign_org_role``: specify different permissions (Editor, Admin)

* ``user_auto_assign_org``: set to true to add all new users to the main organization

If you use your own instance of GitLab instead of gitlab.com, then set the following

* ``auth_gitlab.api_url``

* ``auth_github.auth_url``

* ``auth_github.token_url``

.. image:: /images/products/grafana/aiven_gitlab_configuration.png

Configure authentication using Aiven Client
-------------------------------------------

After installing ``avn``, use ``avn service types -v`` to see all available options.

For example, to set-up Google authentication, use::
    
        avn service update -c auth_google.allowed_domains=<your G-suite domain> -c auth_google.client_id=<client ID from Google developer console> -c auth_google.client_secret=<client secret from Google developer console> <name of your Aiven for Grafana service> 

If you allow sign-ups with ``-c auth_google.allow_sign_up=true`` option, by default each new user is created with "viewer" permission and added to their own newly-created organizations. If you want to specify different permissions, use ``-c user_auto_assign_org_role=Editor`` (or ``Admin``). If you want to add all new users to the main organization, use ``-c user_auto_assign_org=true`` option.

For instructions about setting up integrations on Google, Github or GitLab, refer to Grafana's help pages:

* `Google <http://docs.grafana.org/auth/google/>`_

* `GitHub <http://docs.grafana.org/auth/github/>`_

* `GitLab <http://docs.grafana.org/auth/gitlab/>`_

After setting up authentication integration, it will take a short moment - typically less than a minute - before a plugin is enabled in Aiven for Grafana.