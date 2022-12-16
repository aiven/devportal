Troubleshoot Terraform
======================

If you are encountering issues when deploying your Aiven service via Terraform, enabling debugging for Terraform would help our support team to look into it further.

To do so, you would first need to enable debugging by setting the following environmental variable:

Linux:
.. code:: Shell
    export TF_LOG=”DEBUG”

PowerShell:

.. code:: Powershell 
    $env:TF_LOG="DEBUG"

You can then have the output of the debug log output to any directory with any file name (i.e. terraform-debug.log). 

Depending on your need, you can have other levels of loging. The most common logging levels include FATAL, ERROR, WARN, INFO, DEBUG, TRACE, ALL, and OFF. ALL < TRACE < DEBUG < INFO < WARN < ERROR < FATAL < OFF.

In the example below, we are sending output logs to the temporary folder with the name terraform-debug.log:

Linux:

.. code:: Shell 
    export TF_LOG_PATH=”/tmp/terraform-debug.log

PowerShell:

.. code:: Powershell 
    $env:TF_LOG_PATH="C:\tmp\terraform-debug.log"

Once done, you should be able to trace where the error occurred in more detail when applying your terraform resources.

To remove a log stream, unset the environment variable you do not need. When you close your terminal session, all environment variables unset.

To generate an example of the core and provider logs,run: 

.. code:: Shell
    terraform refresh

Extra Resources:

Logging Levels: <https://www.section.io/engineering-education/how-to-choose-levels-of-logging/>
