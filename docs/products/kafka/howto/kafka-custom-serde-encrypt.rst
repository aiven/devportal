Encrypt client-side with a custom serializer and deserializer
=============================================================

With the Aiven platform there are several deployment models available to meet your security and compliance needs. 

- VPC peering to securely peer the Aiven services to your cloud VPC

- Enhanced Compliance Environments (ECE) to satisfy addtional compliance needs such as HIPPA and PCI-DSS

- Bring your own account (BYOA) which allows deployment of Aiven services directly into your cloud account

In addition to the above, all data transmitted to the Aiven services is encrypted in transit and at rest. 

In some cases however, there are additional compliance and legal needs which require the data to be encrypted prior to entering the Aiven for Kafka service. This can be achieved using a custom serializer and deserializer (commonly referred to as a "custom serde") .


AES Encryption
--------------

In this example, we will use AES encryption. AES provides numerous benefits for streaming systems such as Apache Kafka. 

- Can configure it to use 128-bit, 192-bit or 256-bit keys giving a high level of security

- The algorithm is fast and efficient, making it well suited to real-time data processing use-cases

- As the algorithm relies on a symmetric key as it simplifies the key management. Asymmetrical algorithms require managing separate encryption/decryption keys for all the producers/consumers. 

In this example, we will simply hardcode the key. This should never be done in practise. Instead a secure vault service such as HashiVault or native cloud vendor solution should be used to manage the keys. 

.. Warning::
    You are responsible for the key. If the key is lost, it may be impossible to recover the data. 

Producer
--------

.. code:: python

        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import padding
        from kafka import KafkaProducer
        import base64, os
        import json
        from datetime import datetime

        # 128-bit encryption key
        # This must be stored securely elsewhere
        key = b"\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c"

        # Kafka server
        BOOTSTRAP_SERVER = os.environ.get("BOOTSTRAP_SERVER")


        def encrypt(plaintext):
            # Encrypt data using AES-128 in CBC mode
            cipher = Cipher(algorithms.AES(key), modes.CBC(key), backend=default_backend())
            encryptor = cipher.encryptor()
            padded_plaintext = pad(plaintext)
            ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
            return base64.b64encode(ciphertext)


        def pad(data):
            # Pad data to be encrypted
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(data) + padder.finalize()
            return padded_data


        class EncryptedValueSerializer:
            def __call__(self, msg):
                return encrypt(bytes(msg, "utf-8"))


        producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVER,
            security_protocol="SSL",
            ssl_cafile="ca.pem",
            ssl_certfile="service.cert",
            ssl_keyfile="service.key",
            value_serializer=EncryptedValueSerializer(),
        )

        for i in range(10):
            producer.send(
                "my-secrets", json.dumps({"msg": "this is a test", "time": str(datetime.now())})
            )

        producer.flush()


Consumer
--------

.. code:: python

        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import padding
        from kafka import KafkaConsumer
        import base64, os


        # 128-bit encryption key
        # This must be stored securely elsewhere
        key = b"\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c"

        # Kafka server
        BOOTSTRAP_SERVER = os.environ.get("BOOTSTRAP_SERVER")


        def decrypt(ciphertext):
            # Decrypt data using AES-128 in CBC mode
            ciphertext = base64.b64decode(ciphertext)
            cipher = Cipher(algorithms.AES(key), modes.CBC(key), backend=default_backend())
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            return unpad(plaintext)


        def unpad(data):
            # Unpad data that was encrypted
            unpadder = padding.PKCS7(128).unpadder()
            return unpadder.update(data) + unpadder.finalize()


        class EncryptedValueDeserializer:
            def __call__(self, value):
                return decrypt(value)


        consumer = KafkaConsumer(
            bootstrap_servers=BOOTSTRAP_SERVER,
            value_deserializer=EncryptedValueDeserializer(),
            security_protocol="SSL",
            ssl_cafile="ca.pem",
            ssl_certfile="service.cert",
            ssl_keyfile="service.key",
            group_id="group_id_1",
            auto_offset_reset="earliest",
        )

        consumer.subscribe(["my-secrets"])

        for message in consumer:
            print(message.value)
