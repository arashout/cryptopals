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

def good_message(msg: str, counter: Dict[str, int]) -> bool:
    bad_chars = [chr(i) for i in range(32)] # The first 32 are weird characters
    most_common = [x[0] for x in counter.most_common(10)]

    for bc in bad_chars:
        if bc in most_common:
            return False

    return True

# TODO: Need a better way to score decoded messages
# According to Google I should use English Letter frequency
def possible_candidates(decoded_messages: List[str]) -> List[Tuple[str, Dict[str, int]]]:
    res = []
    for msg in decoded_messages:
        counter = collections.Counter(msg)
        if good_message(msg, counter):
            res.append((msg, counter.most_common(10)))

    return res


if __name__ == "__main__":
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    ass("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",hex_to_base64(s), "S1C1")
    print(str(bytes.fromhex(s)))
    
    a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b = bytes.fromhex("686974207468652062756c6c277320657965")
    print(a.decode('ascii'), b.decode())
    ass("746865206b696420646f6e277420706c6179", xor(a, b).hex() , "S1C2")
    ass("0x746865206b696420646f6e277420706c6179", xor_hex("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") , "S1C2_kris")

    hs = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decoded_messages = []
    for i in range(256):
        b = xor_single_char(bytes.fromhex(hs), i)
        try:
            decoded_messages.append(b.decode())
        except Exception as e:
            pass
    for pc in possible_candidates(decoded_messages):
        print(pc)

