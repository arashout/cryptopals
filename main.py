import base64
import collections
from typing import List, Tuple, Dict
from utils import xor, xor_hex, ass, hex_to_base64
from scoring import messages_with_scores, build_english_frequency

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

    s1c3hs = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    with open('hamlet.txt', 'r') as f:
        doc = f.read()
        english_freq_doc = build_english_frequency(doc)
    ms = messages_with_scores([s1c3hs], english_freq_doc)
    print("output S1C3", ms[0])

    with open("S1C4.txt", "r") as f:
        hex_messages = f.readlines()
    ms = messages_with_scores(hex_messages, english_freq_doc)
    print("output S1C4", ms[0])
    

