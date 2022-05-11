def repeating_xor(msg: bytes, key: bytes) -> bytes:
    j = 0
    res = bytearray([0]*len(msg))
    for i in range(len(msg)):    
        res[i] = msg[i] ^ key[j]
        j = (j + 1) % len(key) # sequentially apply key byte

    return bytes(res)