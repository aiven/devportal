Connect to Aiven for Apache Kafka® with Go
=============================================

These examples show how to connect to an Aiven for Apache Kafka® service using two different Kafka libraries in Go: `Sarama <https://github.com/Shopify/sarama>`_ and `Kafka-go <https://github.com/segmentio/kafka-go>`_.

.. note::

    The examples in this article provide two different options for authentication: SSL and SASL-SSL. For more information on these  authentication methods read :doc:`our article on Kafka authentication types <../concepts/auth-types>`.


Pre-requisites
---------------

Go to the *Overview* page of your Aiven for Apache Kafka service.

* If you are going to connect with SSL authentication:

  * In the *Connection information* section:

    #. If **Authentication Method** is shown, choose **Client Certificate**
    #. Next to *Access Key*, click **Download** and save the ``service.key`` file.
    #. Next to *Access Certificate*, click **Download** and save the ``service.cert`` file.
    #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file.

* If you are going to connect using SASL authentication:

  #. Follow the instructions at `Use SASL Authentication with Apache Kafka® <https://developer.aiven.io/docs/products/kafka/howto/kafka-sasl-auth.html>`_ to enable SASL.

  #. In the *Connection Information* section

     #. Select **SASL** as the **Authentication Method**
     #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file
     #. Note the *Password* required for the SASL, we'll need it for authentication

* Created the keystore ``client.keystore.p12`` and truststore ``client.truststore.jks`` by following  :doc:`our article on configuring Java SSL to access Kafka <../howto/keystore-truststore>`

.. Warning::

  In the below examples, we just pass the name of the keystore and truststore files, but in actual use, the full path should be used.

Variables
---------

========================     =======================================================================================================
Variable                     Description
========================     =======================================================================================================
``HOST``                     Host name for the connection
``SSL_PORT``                 Port number to use for SSL
``SASL_PORT``                Port number to use for SASL
``SASL_USERNAME``            Name of the user for the connection
``SASL_PASSWORD``            Password required to connect using SASL
``CLIENT_ID``                Application-specific client id
========================     =======================================================================================================

With library ``sarama``
-------------------------
Install the library `Sarama <https://github.com/Shopify/sarama>`_ and use code snippet according to your preferred authentication method below.

With SSL authentication
***********************

Set up properties to connect to the cluster:

.. code:: go

    package main

    import (
        "crypto/tls"
        "crypto/x509"
        "io/ioutil"
        "log"
        "github.com/Shopify/sarama"
    )

    func main() {
        keypair, err := tls.LoadX509KeyPair("service.cert", "service.key")
        if err != nil {
            log.Println(err)
            return
        }

        caCert, err := ioutil.ReadFile("ca.pem")
        if err != nil {
            log.Println(err)
            return
        }
        caCertPool := x509.NewCertPool()
        caCertPool.AppendCertsFromPEM(caCert)

        tlsConfig := &tls.Config{
            Certificates: []tls.Certificate{keypair},
            RootCAs: caCertPool,
        }

        // init config, enable errors and notifications
        config := sarama.NewConfig()
        config.Producer.Return.Successes = true
        config.Net.TLS.Enable = true
        config.Net.TLS.Config = tlsConfig
        config.Version = sarama.V0_10_2_0

        brokers := []string{"{HOST}:{SSL_PORT}"}

        producer, err := sarama.NewSyncProducer(brokers, config)

        // add your logic
    }


With SASL-SSL authentication
*****************************

Set up properties to connect to the cluster:

.. code:: go

    package main

    import (
        "crypto/tls"
        "crypto/x509"
        "github.com/Shopify/sarama"
        "io/ioutil"
    )

    func main() {
        caCert, err := ioutil.ReadFile("ca.pem")
        if err != nil {
            panic(err)
        }
        caCertPool := x509.NewCertPool()
        caCertPool.AppendCertsFromPEM(caCert)

        tlsConfig := &tls.Config{
            RootCAs: caCertPool,
        }

        // init config, enable errors and notifications
        config := sarama.NewConfig()
        config.Metadata.Full = true
        config.ClientID = "{CLIENT_ID}"
        config.Producer.Return.Successes = true

        // Kafka SASL configuration
        config.Net.SASL.Enable = true
        config.Net.SASL.User = "{SASL_USERNAME}"
        config.Net.SASL.Password = "{SASL_PASSWORD}"
        config.Net.SASL.Handshake = true
        config.Net.SASL.Mechanism = sarama.SASLTypePlaintext

        // TLS configuration
        config.Net.TLS.Enable = true
        config.Net.TLS.Config = tlsConfig

        brokers := []string{"{HOST}:{SASL_PORT}"}
        producer, err := sarama.NewSyncProducer(brokers, config)

        // add your logic
    }

With library ``kafka-go``
--------------------------
Install the library `kafka-go <https://github.com/segmentio/kafka-go>`_ and use code snippet according to your preferred authentication method below.

With SSL authentication
***********************

.. code:: go

    package main

    import (
        "crypto/tls"
        "crypto/x509"
        "github.com/segmentio/kafka-go"
        "io/ioutil"
        "log"
        "time"
    )

    func main() {
        keypair, err := tls.LoadX509KeyPair("service.cert", "service.key")
        if err != nil {
            log.Fatalf("Failed to load Access Key and/or Access Certificate: %s", err)
        }

        caCert, err := ioutil.ReadFile("ca.pem")
        if err != nil {
            log.Fatalf("Failed to read CA Certificate file: %s", err)
        }

        caCertPool := x509.NewCertPool()
        ok := caCertPool.AppendCertsFromPEM(caCert)
        if !ok {
            log.Fatalf("Failed to parse CA Certificate file: %s", err)
        }

        dialer := &kafka.Dialer{
            Timeout:   10 * time.Second,
            DualStack: true,
            TLS: &tls.Config{
                Certificates: []tls.Certificate{keypair},
                RootCAs:      caCertPool,
            },
        }

        // init producer
        producer := kafka.NewWriter(kafka.WriterConfig{
            Brokers:  []string{"{HOST}:{SSL_PORT}"},
            Topic:    "kafka-go-ssl",
            Dialer:   dialer,
        })

        // add your logic
    }


With SASL authentication
*************************

.. code:: go

    package main

    import (
        "context"
        "crypto/tls"
        "crypto/x509"
        "log"
        "io/ioutil"
        "time"
        "github.com/segmentio/kafka-go"
        "github.com/segmentio/kafka-go/sasl/scram"
    )

    func main() {
        caCert, err := ioutil.ReadFile("ca.pem")
        if err != nil {
            log.Println(err)
            return
        }
        caCertPool := x509.NewCertPool()
        ok := caCertPool.AppendCertsFromPEM(caCert)
        if !ok {
            log.Println(err)
            return
        }
        tlsConfig := &tls.Config{
            RootCAs:      caCertPool,
        }
        scram, err := scram.Mechanism(scram.SHA512, "{SASL_USERNAME}", "{SASL_PASSWORD}")
        if err != nil {
            log.Println(err)
            return
        }
        dialer := &kafka.Dialer{
            Timeout:       10 * time.Second,
            DualStack:     true,
            TLS:           tlsConfig,
            SASLMechanism: scram,
        }
        w := kafka.NewWriter(kafka.WriterConfig{
            Brokers:  []string{"{HOST}:{SASL_PORT}"},
            Topic:    "your-topic-name",
            Balancer: &kafka.Hash{},
            Dialer:   dialer,
        })

        // add your logic
    }