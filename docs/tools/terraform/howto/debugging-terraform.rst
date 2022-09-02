Logging terraform errors
================================

If you are encountering issues when deploying or configuring your Aiven service via Terraform, `enabling debugging for Terraform <https://www.terraform.io/internals/debugging>`_ would provide more details for why the deployment failed.

In order to gather more details, you would first need to enable debugging by setting the following environmental variable:

-------------------
Enabling debug mode
-------------------
Linux
^^^^^
.. code:: bash

    export TF_LOG="DEBUG"


Windows powershell
^^^^^^^^^^^^^^^^^^

.. code:: powershell

    $env:TF_LOG="DEBUG"

You can then have the output of the debug log output to any directory with any file name (i.e. terraform-debug.log).  In the example below, we’re sending the output logs to the temporary folder with the name ``terraform-debug.log``.

-----------
Output logs
-----------
Linux
^^^^^
.. code:: bash

    export TF_LOG_PATH="/tmp/terraform-debug.log"


Windows powershell
^^^^^^^^^^^^^^^^^^
.. code:: powershell

    $env:TF_LOG_PATH="C:\tmp\terraform-debug.log"

Once done, you should be able to trace where the error occurred in more detail when applying your terraform resources.  You can visit the `Terraform for Aiven Github Repository <https://github.com/aiven/terraform-provider-aiven>`_ for the source code.

If you are still encountering issues and unable to deploy your resources, you may contact support@aiven.io and provide the debugging log file created above for further investigation.

If you discovered a bug with the specific Terraform version and Aiven provider version, you may report the issue on the `official Github Issues page <https://github.com/aiven/terraform-provider-aiven/issues>`_.