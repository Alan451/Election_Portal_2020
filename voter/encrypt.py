import rsa
import base64
import time
import random
import json
from django.conf import settings
# users = ['SWC', 'EC', 'CC']

import os
# public_key = {
#     users[0]: "-----BEGIN RSA PUBLIC KEY-----\n\
# MIGJAoGBAIb1tsE1HzZVlk0UK7TqZBg2sCr1U1XzPavqE15ZQO53/hpxMAbL7TP4\n\
# f4S0YaZ5L9Zdou22qoAJMPmkuPEhkq6cjNpZv9xZMfQWN1VdXXVlxrcz19OyvDfx\n\
# 4C1afvNpb6mdXWtxS/c17a5KJ6NBatSuhrQhhBgd2wNLKVMlZ34BAgMBAAE=\n\
# -----END RSA PUBLIC KEY-----\n",
#     users[1]: "-----BEGIN RSA PUBLIC KEY-----\n\
# MIIBCgKCAQEAhG6ZCby/gDDlOZTe7iDl6/gdNGjDwz2hYrKU+ehqIYBLdIllwlh0\n\
# tzw0r1+7HX1K3LXbhyNrQusLq+cvSuxQu+cvPIKonPUVld7OJltOcyvE2Ch6eGQp\n\
# Tgd7imBHI6OKP6pcAD1QJM9I2bbuFxkg5uGq7q7PWiZ8L9VTgXtawRRP+zfc/wcO\n\
# v4hPFwXqSGgJuYVDcEpNClhn7rwu6w31Cixnokv1dvuU8k1incUY3tSthSN5v72Q\n\
# WwiiEGDktUwLChVZ1BflRuPf+B2UyiSe/ke/y0vufqfuR2inc2R+4h6n7IU8XOXn\n\
# ZyTPa1Yy7gbLGAmepHNOYknZVTA1voUqCwIDAQAB\n\
# -----END RSA PUBLIC KEY-----\n",
#     users[2]: "-----BEGIN RSA PUBLIC KEY-----\n\
# MIICCgKCAgEAulCclPDSCexNrRxCNmK5oSGCRni245KxZwJXh6EJG2l//xYDJ/ba\n\
# ERGQKxkZHQGtBeT5dUGwr/kopOLudC9M7EvoDhMEVXYEWNsYp4eWK6UFULTS5g0u\n\
# BdHFdF+/C0yhgEgFQXUlNB6o3ZE/X8aAbxDxR6X96TnVzRMNVVZZ+RAk53C08d04\n\
# caP0fCa1lD1Si1UerP8flpAgtmD4ijAofmZbC3HTjn1v4Omf8+Q4nfUkbV4rMB6V\n\
# KJiHwqCaqm3cL0KwoiaCx9UmoPF1m0Z1fOfVuNrJP4uj1GBF1hWAtnMLEOn5iBGz\n\
# +YgXyClR4vEuxFMlqRegb0WY6xeSay4seAhBMTo99m8C3zUTqNeScqGQg03rhVo9\n\
# VA1axzCfXhUVeyVNxVybbs6jVxxkduq8xz7nH7yT+R5wWIjSgBeGkHz/ImuPm54a\n\
# 5K655dXBHTh4/ngOgnWOnZfFptot45lLxkol6pstGy43TISCgeookzwMOSHa8IPC\n\
# w/N8rF60yJ92rd6boi0CwJ5anhNEYt6QQ674SLhs+O3wyVb/ePtJ/VF08DyZ9WTy\n\
# 2NehG/yJIAQnpHSDi6KEWa5JlFSodqu9gEHNJrXVT4hMS7da7utvNN/QQZbCEFMU\n\
# 683xFY/2o9wGmPuxL/VB5//lSViDjVYXCtUE/tcqdyw0tvuj2DbyehsCAwEAAQ==\n\
# -----END RSA PUBLIC KEY-----\n"
# }

def xor(byte_text, vote_time):
    random.seed(vote_time)
    n = len(byte_text)
    arr = [random.randint(0, 127) for i in range(n)]
    key = bytearray(arr)
    byte_text = bytes(a ^ b for (a, b) in zip(byte_text, key))
    return byte_text


def encryptMessage(key,message, vote_time):
    message = str.encode(message)
    # users = ['SWC', 'EC', 'CC']
    # print(key)
    for i in range(3):
        with open(settings.MEDIA_ROOT+'/'+str(key[i].public_key), 'rb') as fr:
            pu = rsa.PublicKey.load_pkcs1(fr.read())
        message = rsa.encrypt(message, pu)
    message = xor(message, vote_time)
    return base64.b64encode(message).decode()