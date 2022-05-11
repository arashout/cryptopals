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

def score_message(msg: str, scoring_dict: dict) -> float:
    counter = collections.Counter()
    for c in msg:
        counter[c.lower()] += 1
    msg_counter = normalize_counter(counter) 
    all_keys = set().union(msg_counter.keys(), scoring_dict.keys())

    similarity = 0
    for k in all_keys:
        similarity += msg_counter[k] * scoring_dict[k]

    return similarity

def normalize_counter(x: Dict[str, int]) -> Dict[str, float]:
    total = sum(x.values(), 0.0)
    y = x.copy()
    for key in x:
        y[key] /= total
    return y

def build_english_frequency(doc: str) -> dict:
    counter = collections.Counter()
    for c in doc:
        counter[c.lower()] += 1
    return normalize_counter(counter)



if __name__ == "__main__":
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    ass("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",hex_to_base64(s), "S1C1")
    print(str(bytes.fromhex(s)))
    
    a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b = bytes.fromhex("686974207468652062756c6c277320657965")
    print('inputs to S1C2', a.decode('ascii'), b.decode())
    ass("746865206b696420646f6e277420706c6179", xor(a, b).hex() , "S1C2")
    res = xor_hex("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") 
    ass("0x746865206b696420646f6e277420706c6179", res, "S1C2_kris")
    print('output S1C2', "hex:", res, "string:", bytes.fromhex(res[2:]) )

    print("Building English frequency map")
    with open('hamlet.txt', 'r') as f:
        doc = f.read()
        english_freq_doc = build_english_frequency(doc)

    hs = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decoded_messages = []
    for i in range(256): # 1 byte
        b = xor_single_char(bytes.fromhex(hs), i)
        try:
            msg = b.decode()
            decoded_messages.append( (msg, score_message(msg, english_freq_doc ) ) )
        except Exception as e:
           pass
    
    decoded_messages.sort(key=lambda x: x[1], reverse=True)
    for dm in decoded_messages[:10]:
        print(dm)
