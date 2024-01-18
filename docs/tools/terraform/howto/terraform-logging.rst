Enable debug logging for Terraform
==================================

If you are encountering issues when deploying your Aiven service via Terraform, enabling debugging for Terraform can help you to get more information about the problem. This information is also helpful if you need to contact our support team for help.

1. Set the environment variable ``TF_LOG`` to define the level of logging that should be enabled.

   Enable debugging on Linux:

   .. code:: Shell

       export TF_LOG="DEBUG"

   Enable debugging for PowerShell:

   .. code:: Powershell 

       $env:TF_LOG="DEBUG"

   The standard logging levels are available: ``FATAL``, ``ERROR``, ``WARN``, ``INFO``, ``DEBUG``, ``TRACE``, ``ALL``, and ``OFF``.

   .. tip:: Lean more about `how to choose logging levels <https://www.section.io/engineering-education/how-to-choose-levels-of-logging/>`_
   

2.  Configure your debug log output to any directory with any file name (i.e. ``terraform-debug.log``) by setting the environment variable ``TF_LOG_PATH``.


    In the example below, we are sending output logs to the temporary folder with the name terraform-debug.log.

    Configure log location on Linux:

    .. code:: Shell 

        export TF_LOG_PATH=”/tmp/terraform-debug.log

    Configure log location for PowerShell:

    .. code:: Powershell 

        $env:TF_LOG_PATH="C:\tmp\terraform-debug.log"

    This additional output helps you to trace where the error occurred in more detail when applying your terraform resources.


3.  To generate an example of the core and provider logs,run: 

    .. code:: Shell

       terraform refresh

