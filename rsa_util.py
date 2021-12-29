# import cryptography
import argparse
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
def rsa_gen_key(keysize:int):
    priv= rsa.generate_private_key(public_exponent=65537, key_size=keysize)
    return(priv)
def rsa_serialize_keys(private, public):
    priv_serial = private.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption())
    pub_serial = private.public_key().public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return(priv_serial,pub_serial)

def rsa_enc(input_stream,pub_key):
    ciphertext = pub_key.encrypt(input_stream,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

    return(ciphertext)

def rsa_dec(input_stream, priv_key):
    plaintext = priv_key.decrypt(input_stream,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    return(plaintext)

def main():
    # Das ist die Main Routine
    print("MAIN")
    key = rsa_gen_key(2048)
    pub_key = key.public_key()
    # print(rsa_serialize_keys(rsa_gen_key(2048), rsa_gen_key(2048).public_key()))
    encrypted = rsa_enc(b"HALLO_DAS_IST_EIN_TEST", pub_key)
    print(encrypted)
    decrypted = rsa_dec(encrypted, key)
    print(decrypted)


if __name__ == '__main__':
    main()