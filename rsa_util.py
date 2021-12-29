# import cryptography
import argparse
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
def rsa_gen_key(keysize:int):
    priv= rsa.generate_private_key(public_exponent=65537, key_size=keysize)
    return(priv)
def rsa_serialize_keys(private):
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
    text = b'Hallo falls das geht geht es gut!'
    private_key = rsa_gen_key(2048)
    output_file_key = open("./key.txt","wb")
    encrypted_textfile = open("./text.enc", "wb")
    output_file_key.write(rsa_serialize_keys(private_key)[0])
    encrypted_textfile.write(rsa_enc(text, private_key.public_key()))
    output_file_key.close()
    encrypted_textfile.close()


if __name__ == '__main__':
    main()