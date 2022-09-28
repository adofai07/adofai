import copy
import os
import random

import numpy
import pyperclip

code = [[] for _ in range(10)]

code[0] = input()
os.system("cls")

# 글자 1글자당 0 or 1 12자리로 바꾸기
for i in range(len(code[0])):
    code[1].append(bin(ord(code[0][i]))[2:].zfill(18))
code[1] = "".join(code[1])

# 홀수 번째 숫자 바꾸기
for i in range(len(code[1])):
    if i%2 == 0:
        if code[1][i] == "0": code[2].append("1")
        else: code[2].append("0")
    else: code[2].append(code[1][i])
code[2] = "".join(code[2])

# 뒤집기
for i in range(len(code[2])-1, -1, -1):
    code[3].append(code[2][i])
code[3] = "".join(code[3])

for i in range(0, len(code[3]), 3):
    code[4].append({
        "000": "6",
        "001": "4",
        "010": "8",
        "011": "3",
        "100": "5",
        "101": "2",
        "110": "1",
        "111": "9",
    }["".join(code[3][i:i+3])])
    if random.randrange(0, 10) == 0: code[4].append("0")
    if random.randrange(0, 10) == 0: code[4].append("7")
code[4] = "".join(code[4])
code[4] += "0"*(6-len(code[4])%6 if len(code[4])%6 != 0 else 0)

for i in range(0, len(code[4]), 6):
    code[5].append(numpy.base_repr(int("".join(code[4][i:i+6])), 36).zfill(4))
code[5] = "".join(code[5])

for i in range(0, len(code[5]), 2):
    code[6].append(code[5][i+1])
    code[6].append(code[5][i])
code[6] = "".join(code[6])

for j in range(len(code[6])):
    if code[6][len(code[6])-j-1] != "0": break
code[7] = code[6][:-1*j] + str(j)
if j == 0: code[7] = copy.deepcopy(code[6]) + "0"

code[8].append(code[7][0])
for i in range(len(code[7])-1):
    code[8].append(numpy.base_repr(ord(code[7][i]) - ord(code[7][i+1]), 36))
code[8] = " ".join(code[8])

temp = list(code[8].split())
two = []
for i in range(len(temp)):
    t = copy.deepcopy(temp[i])
    if t[0] == "-":
        a = [str(i) for i in range(10)]
        b = [")", "!", "@", "#", "$", "%", "^", "&", "*", "("]
        for i in range(10):
            t = t.replace(a[i], b[i])
        for i in range(65, 91):
            t = t.replace(chr(i), chr(i+32))
        code[9].append(t[1:])
    else: code[9].append(t)
for i in range(len(code[9])):
    if len(code[9][i]) >= 2: code[9][i] = ["[", "]", ";", ".", "/", "<", ">"][random.randrange(7)] + code[9][i]
code[9] = "".join(code[9])

print(code[9])
pyperclip.copy(code[9])