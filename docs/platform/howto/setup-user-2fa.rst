Set it up 2FA Authentication
============================

Two-Factor Authentication (also known as 2-Step Verification or 2FA) in Aiven allows further securing logins by requiring a second authentication code in addition to the user password. 

Currently, Aiven supports Two-Factor Authentication using the `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`_ mobile application.

Setting up Two-Factor Authentication
Install the Google Authenticator application to your mobile device (install instructions)

Login to the Aiven web dashboard and your user profile page by clicking your name at the top toolbar


Click the button next to "Disabled" and enter your current password


Open the Google Authenticator application on your mobile device and add a new entry by selecting the Scan a barcode option. Point the camera to the QR code visible on the Aiven web dashboard. It should be recognized automatically by Google Authenticator and a new "Aiven" entry is added to its list of applications.


Enter the Aiven number sequence from the Google Authenticator app to the Confirmation code field in the above dialog and press the Enable Two-Factor Auth button

Two-Factor Authentication is now enabled

Authentication status of project members
The Two-Factor Authentication status for project members can be viewed under the project members view:

