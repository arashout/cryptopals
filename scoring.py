from typing import List, Dict, Tuple
from utils import xor_single_char
import collections
from utils import ass

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

def messages_with_scores(hex_messages: List[str], english_freq_doc: Dict[str, float]) -> List[Tuple[str, float]]:
    decoded_messages = []
    for hs in hex_messages:
        for i in range(256): # 1 byte
            b = xor_single_char(bytes.fromhex(hs), i)
            try:
                msg = b.decode()
                decoded_messages.append( (msg, score_message(msg, english_freq_doc ) ) )
            except Exception as e:
                pass
    decoded_messages.sort(key=lambda x: x[1], reverse=True)
    return decoded_messages

def hamming_distance(a: bytes, b: bytes) -> int:
    # Drop the 0b
    ab = bin(int.from_bytes(a, 'big'))[2:]
    bb = bin(int.from_bytes(b, 'big'))[2:]
    total_diff = abs(len(ab) - len(bb))
    for i in range(min(len(ab), len(bb))):
        total_diff += int(ab[i]) ^ int(bb[i])
    return total_diff

ass(37, hamming_distance('this is a test'.encode(),'wokka wokka!!!'.encode()), 'hamming distance function is wrong')