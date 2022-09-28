import copy
import os

import pyperclip

code = [[] for _ in range(10)]

code[0] = input()
os.system("cls")

i = -1
while True:
    i += 1
    try:
        if code[0][i] not in ["[", "]", ";", ".", "/", "<", ">"]:
            code[1].append(code[0][i])
        else:
            code[1].append(code[0][i+1:i+3])
            i += 2
    except: break
code[1] = " ".join(code[1])

temp = list(code[1].split())
for i in range(1, len(temp)):
    if temp[i] in [chr(i) for i in range(65, 91)] or "1" in temp[i]:
        code[2].append(str(int(temp[i], 36)))
    elif temp[i] in [chr(i) for i in range(97, 123)]:
        code[2].append("-" + str(int(temp[i].upper(), 36)))
    elif temp[i].isdigit():
        code[2].append(temp[i])
    else:
        t = copy.deepcopy(temp[i])
        a = [str(i) for i in range(10)]
        b = [")", "!", "@", "#", "$", "%", "^", "&", "*", "("]
        for j in range(10):
            t = t.replace(b[j], a[j])
        code[2].append("-" + str(int(t, 36)))
code[2] = " ".join(code[2])

temp = list(map(int, code[2].split()))
code[3].append(code[0][0])
for i in range(len(temp)):
    code[3].append(chr(ord(code[3][-1]) - temp[i]))
code[3] = "".join(code[3])
code[3] = code[3][:-1] + "0"*int(code[3][-1])

for i in range(0, len(code[3]), 2):
    code[4].append(code[3][i+1])
    code[4].append(code[3][i])
code[4] = "".join(code[4])

for i in range(0, len(code[4]), 4):
    code[5].append(str(int(code[4][i:i+4], 36)).zfill(6))
code[5] = "".join(code[5])

while code[5][-1] == "0":
    code[5] = code[5][:-1]

for i in range(len(code[5])):
    if code[5][i] in ["0", "7"]: continue
    
    if code[5][i] == "1": code[6].append("110")
    if code[5][i] == "2": code[6].append("101")
    if code[5][i] == "3": code[6].append("011")
    if code[5][i] == "4": code[6].append("001")
    if code[5][i] == "5": code[6].append("100")
    if code[5][i] == "6": code[6].append("000")
    if code[5][i] == "8": code[6].append("010")
    if code[5][i] == "9": code[6].append("111")
code[6] = "".join(code[6])

for i in range(len(code[6])-1, -1, -1):
    code[7].append(code[6][i])
code[7] = "".join(code[7])

for i in range(len(code[7])):
    if i%2 == 0:
        if code[7][i] == "0": code[8].append("1")
        else: code[8].append("0")
    else: code[8].append(code[7][i])
code[8] = "".join(code[8])

for i in range(0, len(code[8]), 18):
    code[9].append(chr(int(code[8][i:i+18], 2)))
code[9] = "".join(code[9])

print(code[9])
pyperclip.copy(code[9])
