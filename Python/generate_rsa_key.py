from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_key():
    key_size = [512, 1024, 2048, 4096]
    print(key_size)

    size_choice = input("Choose key size: ")

    try:
        result_size = int(size_choice)

        if result_size in key_size:

            private_key = rsa.generate_private_key(
                backend=default_backend(),
                public_exponent=65537, key_size=result_size
            )

            public_key = private_key.public_key().public_bytes(
                serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH
            )

            pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()
            )

            private_key_result = pem.decode('utf-8')
            public_key_result = public_key.decode('utf-8')

            return private_key_result, public_key_result

        else:
            return str("The choice of size does not fit.")

    except Exception as error:
        print(error)
        return str("This is not a number.")
