Troubleshooting DNS names pointing to Private IPs not resolving
===============================================================

When an Aiven service is placed in a VPC, the DNS hostname of the
service will resolve to a private IP address within the VPC's network
address range. This can cause problems resolving the service hostname
with some DNS resolvers used in office and home networks if they have
`DNS-rebinding
protection <https://en.wikipedia.org/wiki/DNS_rebinding#Protection>`__
enabled. This protection blocks the resolution of external hostnames
pointing to private IPs normally used in office and home networks, to
prevent a class of attack which involves external hostnames pointing to
IPs on the local network.

The symptoms of this are: hostnames of Aiven services in a VPC not
resolving, while if public access is enabled, the corresponding
``public-`` prefixed hostname for the services resolve OK when using the
same DNS resolver.

You can test if this is caused by DNS-rebinding protection by requesting
the name from another known resolver e.g. Google Public DNS at 8.8.8.8
which has no rebinding protection:

::

   $ dig +short myservice-myproject.aivencloud.com @8.8.8.8 
   192.168.0.1

and compare this with the response from your default DNS resolver:

::

   $ dig +short myservice-myproject.aivencloud.com

If the response from your default DNS resolver / server does not return
the expected IP returned from Google Public DNS, it indicates your
default DNS resolver is blocking the resolution.

The recommended fix for this issue is to configure your DNS resolver
(normally a server for offices, or a home router for home networks) to
allow the resolution of hostnames in the Aiven service domain,
```aivencloud.com`` <http://aivencloud.com>`__ , to bypass the
DNS-rebinding protection. If your DNS resolver allows this configuration
it is preferable to allow one domain to bypass it instead of disabling
DNS-rebinding protection entirely.
