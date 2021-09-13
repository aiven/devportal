Aiven Operator for Kubernetes
=============================

    Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications. Kubernetes Operators are software extensions to Kubernetes that make use of custom resources to manage applications and their components. `Kubernetes website <https://kubernetes.io/>`_.

Aiven Operator for Kubernetes allows users to manage Aiven services through the Kubernetes API by using `Custom Resource Definitions <https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/>`_.

For now, only Aiven for PostgreSQL and Aiven for Kafka are supported.

Getting started
---------------
Let's get started by configuring the Aiven Operator and deploying a PostgreSQL database.

Requirements
''''''''''''
First, you will need access to a Kubernetes cluster. To try the operator locally, we recommend using `kind <https://kind.sigs.k8s.io/>`_. You can install it by following their `official documentation <https://kind.sigs.k8s.io/docs/user/quick-start/#installation>`_.

We will be installing the operator with Helm. Follow their `official instructions <https://helm.sh/docs/intro/install/>`_ to install it.

You'll also need an Aiven account. If you don't have one yet, `sign up <https://console.aiven.io/signup?utm_source=&utm_medium=organic&utm_campaign=k8s-operator&utm_content=post>`_ and enjoy our free trial! Once you have your account set, please generate and note down the `authentication token <https://help.aiven.io/en/articles/2059201-authentication-tokens>`_ and your project name, they will be used to authenticate the Kubernetes operator with Aiven's API.

Install the operator
''''''''''''''''''''
Once you have a Kubernetes cluster and an Aiven authentication token, we can proceed to install the operator.

Install the cert-manager with the command below. It is used to manage the webhook TLS certificates used by our operator.

.. Tip::
    You use the operator without ``cert-manager`` and the admission webhooks, just take a look at the last step.

.. code:: bash

    kubectl apply -f https://github.com/jetstack/cert-manager/releases/latest/download/cert-manager.yaml

Verify the ``cert-manager`` installation by checking if their pods are up and running:

.. code:: bash

    kubectl get pod -n cert-manager

    NAME                                      READY   STATUS    RESTARTS   AGE
    cert-manager-848f547974-w5xj7             1/1     Running   0          8s
    cert-manager-cainjector-54f4cc6b5-vdksm   1/1     Running   0          8s
    cert-manager-webhook-7c9588c76-pll96      1/1     Running   0          8s

Add the `Aiven Helm chart repository <https://github.com/aiven/aiven-charts/>`_ and update your local Helm information:

.. code:: bash

  helm repo add aiven https://aiven.github.io/aiven-charts
  helm repo update

Now let's install the CRDs and them the operator itself:

.. code:: bash

    helm install aiven-operator-crds aiven/aiven-operator-crds
    helm install aiven-operator aiven/aiven-operator

.. Tip::
    You can use ``helm install aiven-operator aiven/aiven-operator --set webhooks.enabled=false`` to disable the admission webhooks.

You can verify the installation by making sure the operator pod is running with the command below:

.. code:: bash

    kubectl get pod -l app.kubernetes.io/name=aiven-operator

    NAME                              READY   STATUS    RESTARTS   AGE
    aiven-operator-576d944499-ggttj   1/1     Running   0          12m

Authenticating
''''''''''''''
Before creating a service, we need to authenticate the operator with Aiven's API. To do so, create the Kubernetes secret with the command below, substituting the ``<your-token-here>`` with the authentication token generated in the prerequisites section.

.. code:: bash

    kubectl create secret generic aiven-token --from-literal=token="<your-token-here>"

Deploying Aiven for PostgreSQL
''''''''''''''''''''''''''''''
It's showtime! Let's create an Aiven for PostgreSQL service using the Custom Resource provided by the operator. Create a file named ``pg-sample.yaml`` with the content below, substituting the ``<your-project-name>`` with your Aiven project name. Take a look at the commented lines to understand better what each field represents.

.. code:: yaml

    apiVersion: aiven.io/v1alpha1
    kind: PostgreSQL
    metadata:
      name: pg-sample
    spec:
    
      # gets the authentication token from the `aiven-token` secret
      authSecretRef:
        name: aiven-token
        key: token
    
      # outputs the PostgreSQL connection on the `pg-connection` secret
      connInfoSecretTarget:
        name: pg-connection
    
      # add your Project name here
      project: <your-project-name> 
    
      # cloud provider and plan of your choice
      # you can check all of the possibilities here https://aiven.io/pricing
      cloudName: google-europe-west1
      plan: startup-4
    
      # general Aiven configuration
      maintenanceWindowDow: friday
      maintenanceWindowTime: 23:00:00
    
      # specific PostgreSQL configuration
      userConfig:
        pg_version: '11'

Apply the resource with the command below:

.. code:: bash

    kubectl apply -f pg-sample.yaml

You can verify the status of your service with the following command. Once the ``STATE`` field has the value ``RUNNING`` we will proceed to connect to the service.

.. code:: bash

    kubectl get pgs.aiven.io pg-sample

    NAME        PROJECT        REGION                PLAN       STATE
    pg-sample   your-project   google-europe-west1   hobbyist   RUNNING

Using the service
'''''''''''''''''
Once the output of the command below is ``RUNNING``, we can connect and test our PostgreSQL service.

The connection information – in this case, the PostgreSQL service URI – is automatically created by the operator within a Kubernetes secret named after the value from the ``connInfoSecretTarget.name`` field.

You can take a look at the information available with the following command:

.. code:: bash

    kubectl describe secret pg-connection

    [...]
    Type:  Opaque

    Data
    ====
    PGSSLMODE:     7 bytes
    PGUSER:        8 bytes
    DATABASE_URI:  112 bytes
    PGDATABASE:    9 bytes
    PGHOST:        43 bytes
    PGPASSWORD:    16 bytes
    PGPORT:        5 bytes

Lastly, let's deploy a pod to test the connection to PostgreSQL from Kubernetes. Create a file named ``pod-psql.yaml`` with the content below:

.. code:: yaml

    apiVersion: v1
    kind: Pod
    metadata:
      name: psql-test-connection
    spec:
      restartPolicy: Never
      containers:
        - image: postgres:11-alpine
          name: postgres
          command: ['psql', '$(DATABASE_URI)', '-c', 'SELECT version();']
          
          # the pg-connection secret becomes environment variables 
          envFrom:
          - secretRef:
              name: pg-connection

Apply it with:

.. code:: bash

    kubectl apply -f pod-psql.yaml

It will run, output the PostgreSQL version and terminate. We can see the logs with the following command:

.. code:: bash

    kubectl logs psql-test-connection

Managing and using a database through Kubernetes has never been so easy!

Clean up
''''''''
To destroy the resources created, execute the following commands:

.. code:: bash

    kubectl delete pod psql-test-connection
    kubectl delete postgresqls.aiven.io pg-sample

To remove the operator and ``cert-manager`` (if installed), use the following:

.. code:: bash

    helm uninstall aiven-operator
    helm uninstall aiven-operator-crds
    kubectl delete -f https://github.com/jetstack/cert-manager/releases/latest/download/cert-manager.yaml

Learn more
----------
Check out these resources to learn more about Kubernetes and our operator:

* `Aiven Operator for Kubernetes documentation <https://aiven.github.io/aiven-operator>`_
* `Kubernetes Basics <https://kubernetes.io/docs/tutorials/kubernetes-basics/>`_

Get involved
------------
If you have any comments or want to contribute to the tool, please join us on the `GitHub repository <https://github.com/aiven/aiven-operator>`_.