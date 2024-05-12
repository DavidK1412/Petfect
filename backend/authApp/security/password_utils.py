import os
import base64


def generate_salt():
    salt = os.urandom(32)
    return base64_encode(salt)


def base64_encode(data):
    return base64.b64encode(data).decode('utf-8')


def base64_decode(data):
    return base64.b64decode(data)
