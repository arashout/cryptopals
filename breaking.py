from typing import List
from scoring import hamming_distance

def into_chunks(b: bytes, block_size: int, max_chunks=4):
    count = 0
    chunks = []
    for i in range(0, len(b), block_size):
        if count >= max_chunks:
            break
        count+=1
        chunks.append( b[i:i+block_size])
    return chunks

def normalized_edit_distance(chunks: List[bytes], block_size: int):
    normalized_distance = []
    for i in range(len(chunks)-1):
        for j in range(len(chunks)-1):
            if i == j:
                continue
            a = chunks[i]
            b = chunks[j]
            normalized_distance.append( hamming_distance(chunks[i], chunks[i+1])/block_size )
    
    return sum(normalized_distance)/len(normalized_distance)
