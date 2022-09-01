Recover a deleted service
=========================

For active or suspended services, the related backups can be directly restored by the user through the Aiven web console or CLI through a couple of clicks of the mouse or a command line invocation.

However, once a service is deleted then the backups will no longer be visible or restorable by the user. Several safeguards are in place to avoid accidental deletion of a service, but it can still happen, e.g. through human error or a malicious user that has gained administrative access credentials. 

To address this concern we store the backups and encryption keys for all deleted services for **30 days**. Therefore, as a disaster recovery option, the backups can be restored by contacting support@Aiven.io.

.. note::
   As this is a manual operation from our operations team and intended for disaster recovery only, the recovery of a deleted service may incur an additional cost to your project.
