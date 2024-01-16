
``additional_backup_regions``
-----------------------------
*array*

**Additional Cloud Regions for Backup Replication** 



``custom_domain``
-----------------
*['string', 'null']*

**Custom domain** Serve the web frontend using a custom CNAME pointing to the Aiven DNS name



``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``service_log``
---------------
*['boolean', 'null']*

**Service logging** Store logs for the service so that they are available in the HTTP API and console.



``static_ips``
--------------
*boolean*

**Static IP addresses** Use static public IP addresses



``external_image_storage``
--------------------------
*object*

**External image store settings** 

``provider``
~~~~~~~~~~~~
*string*

**Provider type** 

``bucket_url``
~~~~~~~~~~~~~~
*string*

**Bucket URL for S3** 

``access_key``
~~~~~~~~~~~~~~
*string*

**S3 access key. Requires permissions to the S3 bucket for the s3:PutObject and s3:PutObjectAcl actions** 

``secret_key``
~~~~~~~~~~~~~~
*string*

**S3 secret key** 



``smtp_server``
---------------
*object*

**SMTP server settings** 

``host``
~~~~~~~~
*string*

**Server hostname or IP** 

``port``
~~~~~~~~
*integer*

**SMTP server port** 

``skip_verify``
~~~~~~~~~~~~~~~
*boolean*

**Skip verifying server certificate. Defaults to false** 

``username``
~~~~~~~~~~~~
*['string', 'null']*

**Username for SMTP authentication** 

``password``
~~~~~~~~~~~~
*['string', 'null']*

**Password for SMTP authentication** 

``from_address``
~~~~~~~~~~~~~~~~
*string*

**Address used for sending emails** 

``from_name``
~~~~~~~~~~~~~
*['string', 'null']*

**Name used in outgoing emails, defaults to Grafana** 

``starttls_policy``
~~~~~~~~~~~~~~~~~~~
*string*

**Either OpportunisticStartTLS, MandatoryStartTLS or NoStartTLS. Default is OpportunisticStartTLS.** 



``auth_basic_enabled``
----------------------
*boolean*

**Enable or disable basic authentication form, used by Grafana built-in login** 



``oauth_allow_insecure_email_lookup``
-------------------------------------
*boolean*

**Enforce user lookup based on email instead of the unique ID provided by the IdP** 



``auth_generic_oauth``
----------------------
*object*

**Generic OAuth integration** 

``allow_sign_up``
~~~~~~~~~~~~~~~~~
*boolean*

**Automatically sign-up users on successful sign-in** 

``allowed_domains``
~~~~~~~~~~~~~~~~~~~
*array*

**Allowed domains** 

``allowed_organizations``
~~~~~~~~~~~~~~~~~~~~~~~~~
*array*

**Require user to be member of one of the listed organizations** 

``api_url``
~~~~~~~~~~~
*string*

**API URL** 

``auth_url``
~~~~~~~~~~~~
*string*

**Authorization URL** 

``auto_login``
~~~~~~~~~~~~~~
*boolean*

**Allow users to bypass the login screen and automatically log in** 

``client_id``
~~~~~~~~~~~~~
*string*

**Client ID from provider** 

``client_secret``
~~~~~~~~~~~~~~~~~
*string*

**Client secret from provider** 

``name``
~~~~~~~~
*string*

**Name of the OAuth integration** 

``scopes``
~~~~~~~~~~
*array*

**OAuth scopes** 

``token_url``
~~~~~~~~~~~~~
*string*

**Token URL** 



``auth_google``
---------------
*object*

**Google Auth integration** 

``allow_sign_up``
~~~~~~~~~~~~~~~~~
*boolean*

**Automatically sign-up users on successful sign-in** 

``client_id``
~~~~~~~~~~~~~
*string*

**Client ID from provider** 

``client_secret``
~~~~~~~~~~~~~~~~~
*string*

**Client secret from provider** 

``allowed_domains``
~~~~~~~~~~~~~~~~~~~
*array*

**Domains allowed to sign-in to this Grafana** 



``auth_github``
---------------
*object*

**Github Auth integration** 

``allow_sign_up``
~~~~~~~~~~~~~~~~~
*boolean*

**Automatically sign-up users on successful sign-in** 

``auto_login``
~~~~~~~~~~~~~~
*boolean*

**Allow users to bypass the login screen and automatically log in** 

``client_id``
~~~~~~~~~~~~~
*string*

**Client ID from provider** 

``client_secret``
~~~~~~~~~~~~~~~~~
*string*

**Client secret from provider** 

``team_ids``
~~~~~~~~~~~~
*array*

**Require users to belong to one of given team IDs** 

``allowed_organizations``
~~~~~~~~~~~~~~~~~~~~~~~~~
*array*

**Require users to belong to one of given organizations** 

``skip_org_role_sync``
~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Stop automatically syncing user roles** 



``auth_gitlab``
---------------
*object*

**GitLab Auth integration** 

``allow_sign_up``
~~~~~~~~~~~~~~~~~
*boolean*

**Automatically sign-up users on successful sign-in** 

``api_url``
~~~~~~~~~~~
*string*

**API URL. This only needs to be set when using self hosted GitLab** 

``auth_url``
~~~~~~~~~~~~
*string*

**Authorization URL. This only needs to be set when using self hosted GitLab** 

``client_id``
~~~~~~~~~~~~~
*string*

**Client ID from provider** 

``client_secret``
~~~~~~~~~~~~~~~~~
*string*

**Client secret from provider** 

``allowed_groups``
~~~~~~~~~~~~~~~~~~
*array*

**Require users to belong to one of given groups** 

``token_url``
~~~~~~~~~~~~~
*string*

**Token URL. This only needs to be set when using self hosted GitLab** 



``auth_azuread``
----------------
*object*

**Azure AD OAuth integration** 

``allow_sign_up``
~~~~~~~~~~~~~~~~~
*boolean*

**Automatically sign-up users on successful sign-in** 

``client_id``
~~~~~~~~~~~~~
*string*

**Client ID from provider** 

``client_secret``
~~~~~~~~~~~~~~~~~
*string*

**Client secret from provider** 

``auth_url``
~~~~~~~~~~~~
*string*

**Authorization URL** 

``token_url``
~~~~~~~~~~~~~
*string*

**Token URL** 

``allowed_groups``
~~~~~~~~~~~~~~~~~~
*array*

**Require users to belong to one of given groups** 

``allowed_domains``
~~~~~~~~~~~~~~~~~~~
*array*

**Allowed domains** 



``private_access``
------------------
*object*

**Allow access to selected service ports from private networks** 

``grafana``
~~~~~~~~~~~
*boolean*

**Allow clients to connect to grafana with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access``
----------------------
*object*

**Allow access to selected service components through Privatelink** 

``grafana``
~~~~~~~~~~~
*boolean*

**Enable grafana** 



``public_access``
-----------------
*object*

**Allow access to selected service ports from the public Internet** 

``grafana``
~~~~~~~~~~~
*boolean*

**Allow clients to connect to grafana from the public internet for service nodes that are in a project VPC or another type of private network** 



``recovery_basebackup_name``
----------------------------
*string*

**Name of the basebackup to restore in forked service** 



``service_to_fork_from``
------------------------
*['string', 'null']*

**Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from``
------------------------
*['string', 'null']*

**Name of another project to fork a service from. This has effect only when a new service is being created.** 



``user_auto_assign_org``
------------------------
*boolean*

**Auto-assign new users on signup to main organization. Defaults to false** 



``user_auto_assign_org_role``
-----------------------------
*string*

**Set role for new signups. Defaults to Viewer** 



``google_analytics_ua_id``
--------------------------
*string*

**Google Analytics ID** 



``metrics_enabled``
-------------------
*boolean*

**Enable Grafana /metrics endpoint** 



``cookie_samesite``
-------------------
*string*

**Cookie SameSite attribute: 'strict' prevents sending cookie for cross-site requests, effectively disabling direct linking from other sites to Grafana. 'lax' is the default value.** 



``alerting_error_or_timeout``
-----------------------------
*string*

**Default error or timeout setting for new alerting rules** 



``alerting_nodata_or_nullvalues``
---------------------------------
*string*

**Default value for 'no data or null values' for new alerting rules** 



``alerting_enabled``
--------------------
*boolean*

**Enable or disable Grafana legacy alerting functionality. This should not be enabled with unified_alerting_enabled.** 



``alerting_max_annotations_to_keep``
------------------------------------
*integer*

**Max number of alert annotations that Grafana stores. 0 (default) keeps all alert annotations.** 



``dashboards_min_refresh_interval``
-----------------------------------
*string*

**Minimum refresh interval** Signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s, 1h



``dashboards_versions_to_keep``
-------------------------------
*integer*

**Dashboard versions to keep per dashboard** 



``dataproxy_timeout``
---------------------
*integer*

**Timeout for data proxy requests in seconds** 



``dataproxy_send_user_header``
------------------------------
*boolean*

**Send 'X-Grafana-User' header to data source** 



``dashboard_previews_enabled``
------------------------------
*boolean*

**Enable browsing of dashboards in grid (pictures) mode** This feature is new in Grafana 9 and is quite resource intensive. It may cause low-end plans to work more slowly while the dashboard previews are rendering.



``viewers_can_edit``
--------------------
*boolean*

**Users with view-only permission can edit but not save dashboards** 



``editors_can_admin``
---------------------
*boolean*

**Editors can manage folders, teams and dashboards created by them** 



``disable_gravatar``
--------------------
*boolean*

**Set to true to disable gravatar. Defaults to false (gravatar is enabled)** 



``allow_embedding``
-------------------
*boolean*

**Allow embedding Grafana dashboards with iframe/frame/object/embed tags. Disabled by default to limit impact of clickjacking** 



``date_formats``
----------------
*object*

**Grafana date format specifications** 

``full_date``
~~~~~~~~~~~~~
*string*

**Moment.js style format string for cases where full date is shown** 

``interval_second``
~~~~~~~~~~~~~~~~~~~
*string*

**Moment.js style format string used when a time requiring second accuracy is shown** 

``interval_minute``
~~~~~~~~~~~~~~~~~~~
*string*

**Moment.js style format string used when a time requiring minute accuracy is shown** 

``interval_hour``
~~~~~~~~~~~~~~~~~
*string*

**Moment.js style format string used when a time requiring hour accuracy is shown** 

``interval_day``
~~~~~~~~~~~~~~~~
*string*

**Moment.js style format string used when a time requiring day accuracy is shown** 

``interval_month``
~~~~~~~~~~~~~~~~~~
*string*

**Moment.js style format string used when a time requiring month accuracy is shown** 

``interval_year``
~~~~~~~~~~~~~~~~~
*string*

**Moment.js style format string used when a time requiring year accuracy is shown** 

``default_timezone``
~~~~~~~~~~~~~~~~~~~~
*string*

**Default time zone for user preferences. Value 'browser' uses browser local time zone.** 



``unified_alerting_enabled``
----------------------------
*boolean*

**Enable or disable Grafana unified alerting functionality. By default this is enabled and any legacy alerts will be migrated on upgrade to Grafana 9+. To stay on legacy alerting, set unified_alerting_enabled to false and alerting_enabled to true. See https://grafana.com/docs/grafana/latest/alerting/set-up/migrating-alerts/ for more details.** 



