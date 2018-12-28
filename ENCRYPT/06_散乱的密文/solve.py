#!usr/bin/python
# coding: utf-8

cipher = "lf5{ag024c483549d7fd@@1}"
cipher = list(cipher)
order = [2, 1, 6, 5, 3, 4]

for _ in range(10):
    result = []
    _len = len(cipher)
    result = []
    for i in range(4):
        for j in range(6):
            result.append(cipher[order[j] + 6 * i - 1])
    print(''.join(result))
    cipher = result

