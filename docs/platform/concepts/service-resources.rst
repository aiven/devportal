Service resources
=================
You may have noticed that services in Aiven have different resources than the virtual machine (VM) it runs on. A number of Aiven plans, particularly low-end ones, do not exactly match the resources virtual machines provide in all clouds. The most significant differences are with the **Hobbyist**, and **Startup-4** plans on **DigitalOcean**, where the droplets typically have more resources (CPU, RAM, disk space) than we advertise for our plans.

The reason is that our plans are defined in a way that allows us to offer the same plans in all clouds, making it possible to migrate workloads between the different clouds providers.

Resources available in each of the clouds vary, especially on the smaller virtual machine sizes. Therefore we have defined our plans with resources that we can provide for all clouds. Some plans may offer more resources than advertised, but we reserve the right to scale down the VMs used to implement the services in case the cloud providers introduce more suitable VM types. 
