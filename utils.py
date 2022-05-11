import base64
import collections
from typing import List, Tuple, Dict

def ass(expected, actual, message_pass):
    if expected == actual:
        print(message_pass)
    else:
        raise Exception("{0} != {1}".format(expected, actual))

def hex_to_base64(hex_string: str) -> str:
    b64 = base64.b64encode(bytes.fromhex(hex_string))
    return b64.decode("utf-8")

def xor_hex(h1, h2):
    i1 = int(h1, 16)
    i2 = int(h2, 16)
    return hex(i1 ^ i2)

def xor(one: bytes, two: bytes) -> bytes:
    if len(one) != len(two):
        raise ValueError("not equal sized")
    
    return bytes(a ^ b for (a, b) in zip(one, two))

def xor_single_char(message: bytes, key: int) -> bytes:
    return bytes(a ^ key for a in message) 
