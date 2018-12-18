#!usr/bin/python
# coding: utf-8

# This problem is related to rail fence cipher

import math

def rail_fence_encode(plain, n):
    """
    @param cipher: cipher text\n
    @param n: number of letters per block (for encryption phrase)\n
    """
    plain = list(plain)
    _len = len(plain)
    _num_block = math.ceil(_len / n)
    _block = [[] for _ in range(_num_block)]
    for i in range(_num_block):
        for j in range(n):
            if plain:
                _block[i].append(plain.pop(0))

    result = []
    for i in range(n):
        for j in range(_num_block):
            if _block[j]:
                result.append(_block[j].pop(0))
    return ''.join(result)

def rail_fence_decode(cipher, n):
    """
    @param cipher: cipher text\n
    @param n: number of letters per block (for encryption phrase)\n
    """
    cipher = list(cipher)
    _len = len(cipher)
    _num_block = math.ceil((_len + 1) / n)
    _num_perline = n
    _rest = _len % n
    _block = [[] for _ in range(_num_block)]
    for i in range(_num_perline):
        for j in range(_num_block - 1):
            _block[j].append(cipher.pop(0))
        if _rest:
            _rest -= 1
            _block[_num_block - 1].append(cipher.pop(0))
            
    result = []
    for i in range(_num_block):
        result.extend(_block[i])
    return ''.join(result)



def decode(cipher):
    _len = len(cipher)
    for i in range(_len):
        print("%d: %s" % ((i + 1), rail_fence_decode(cipher, i + 1)))
    return


if __name__ == "__main__":
    cipher = "KYsd3js2E{a2jda}"
    decode(cipher)
    # Result is:
    # 2: KEY{sad23jjdsa2}

    