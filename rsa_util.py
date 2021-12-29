# import cryptography
import argparse
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def rsa_gen_key(keysize:int):
    priv= rsa.generate_private_key(public_exponent=65537, key_size=keysize)
    return(priv)
def rsa_serialize_keys(private, public):
    priv_serial = private.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption())
    pub_serial = private.public_key().public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return(priv_serial,pub_serial)

def rsa_enc(cyphertext:str,pub_key):


    print("rsa_enc")

def rsa_dec():
    print("rsa_dec")

def main():
    # Das ist die Main Routine
    print("MAIN")
    print(rsa_serialize_keys(rsa_gen_key(2048), rsa_gen_key(2048).public_key()))


if __name__ == '__main__':
    main()