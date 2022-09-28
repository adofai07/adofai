import os
import copy
from itertools import *
from datetime import datetime
import time
import sys

def calc_list(a, b):
    global minimum, maximum, cnt, printed

    if (a, b) in printed: return
    else: printed.append((a, b))

    if abs(len(a) - len(b)) >= 2: return
    if len(a) == len(b) == 1: return

    tprint(f"\\color 255, 255, 255 Names : {a} {b}", filename = "C:/combination_log.txt")

    numbers = []

    if len(b) == len(a) + 1:
        temp = a
        a = b
        b = temp

    if len(a) != len(b) or a == b:
        for i in range(len(b)):
            numbers.append(kor_to_eng(a[i]))
            numbers.append(kor_to_eng(b[i]))
        numbers.append(kor_to_eng(a[-1]))

        result = print_number(a, b, numbers)
        if result < minimum[0]:
            minimum = [result]
        if result == minimum[0]:
            minimum.append((a, b))

        if result > maximum[0]:
            maximum = [result]
        if result == maximum[0]:
            maximum.append((a, b))

        cnt += 1

    elif len(a) == len(b):
        for i in range(len(a)):
            numbers.append(kor_to_eng(a[i]))
            numbers.append(kor_to_eng(b[i]))
        
        result = print_number(a, b, numbers)
        if result < minimum[0]:
            minimum = [result]
        if result == minimum[0]:
            minimum.append((a, b))

        if result > maximum[0]:
            maximum = [result]
        if result == maximum[0]:
            maximum.append((a, b))

        numbers = []

        for i in range(len(a)):
            numbers.append(kor_to_eng(b[i]))
            numbers.append(kor_to_eng(a[i]))

        result = print_number(b, a, numbers)
        if result < minimum[0]:
            minimum = [result]
        if result == minimum[0]:
            minimum.append((b, a))

        if result > maximum[0]:
            maximum = [result]
        if result == maximum[0]:
            maximum.append((b, a))
        cnt += 2

    tprint(filename = "C:/combination_log.txt")
    print()

def print_number(a, b, numbers):
    while len(numbers) >= 4 and not numbers == [1, 0, 0]:
        temp = []
        for i in range(len(numbers)-1):
            temp.append((numbers[i] + numbers[i+1])%10)
        numbers = copy.deepcopy(temp)
    
    if numbers == [1, 0, 0]: tprint(f"{a} \\color 255, 0, 0 >> \\color 255, 255, 255 {b} \\color 255, 0, 0 >> 100", filename = "C:/combination_log.txt")
    elif numbers == [0, 0, 0] or numbers[0] == numbers[2] == 10 - numbers[1]: tprint(f"{a} \\color 0, 0, 255 >> \\color 255, 255, 255 {b} \\color 0, 0, 255 >> 00", filename = "C:/combination_log.txt")
    else: tprint(f"{a} \\color {int((((numbers[0] + numbers[1])%10)*10 + (numbers[1] + numbers[2])%10)*2.55)}, 0, {255 - int(((((numbers[0] + numbers[1])%10)*10 + (numbers[1] + numbers[2])%10))*2.55)} >> \\color 255, 255, 255 {b} \\color {int((((numbers[0] + numbers[1])%10)*10 + (numbers[1] + numbers[2])%10)*2.55)}, 0, {255 - int(((((numbers[0] + numbers[1])%10)*10 + (numbers[1] + numbers[2])%10))*2.55)} >> \\color 255, 255, 255 " + str("".join(map(str, [(numbers[0] + numbers[1])%10, (numbers[1] + numbers[2])%10]))), filename = "C:/combination_log.txt")
    return ((numbers[0] + numbers[1])%10)*10 + (numbers[1] + numbers[2])%10 if numbers != [1, 0, 0] else 100

def kor_to_eng(text):
    first = {"r" : 2, "R" : 4, "s" : 2, "e" : 3, "E" : 6, "f" : 5, "a" : 4, "q" : 4, "Q" : 8, "t" : 2, "T" : 4, "d" : 1, "w" : 3, "W" : 6, "c" : 4, "z" : 3, "x" : 4, "v" : 4, "g" : 3}
    second = {"k" : 2, "o" : 3, "i" : 3, "O" : 4, "j" : 2, "p" : 3, "u" : 3, "P" : 4, "h" : 2, "hk" : 4, "ho" : 5, "hl" : 3, "y" : 3, "n" : 2, "nj" : 4, "np" : 5, "nl" : 3, "b" : 3, "m" : 1, "ml" : 2, "l" : 1}
    third = {"" : 0, "r" : 2, "R" : 4, "rt" : 4, "s" : 2, "sw" : 5, "sg" : 5, "e" : 3, "f" : 5, "fr" : 7, "fa" : 9, "fq" : 9, "ft" : 7, "fx" : 9, "fv" : 9, "fg" : 8, "a" : 4, "q" : 4, "qt" : 6, "t" : 2, "T" : 4, "d" : 1, "w" : 3, "c" : 4, "z" : 3, "x" : 4, "v" : 4, "g" : 3}

    for i in range(len(text)):
        first1, second1, third1 = (ord(text[i])-44032)//588, ((ord(text[i])-44032)%588)//28, ((ord(text[i])-44032)%588)%28
        first1, second1, third1 = list(first.keys())[first1] , list(second.keys())[second1] , list(third.keys())[third1]
        first1, second1, third1 = first[first1], second[second1], third[third1]
    return first1 + second1 + third1

def tprint(message = "\0", end = "\0", delay = 0, pause = 0, blank_pause = 0, color = (255, 255, 255), filename = "\0"):
    message = str(message)
    file_input = ""
    start = time.time()
    i = -1
    while i < len(message) - 1:
        i += 1
        if message[i:i+6] == r"\color":
            for j in range(i+7, len(message)):
                if message[j] == " " and message[j-1] != ",": break

            temp = message[i+7:j]
            for k in range(len(temp)):
                if temp[k] == ",": temp = temp[:k] + " " + temp[k+1:]

            color = tuple(map(int, "".join(temp).split()))
            i = j
            continue
        sys.stdout.write(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{message[i]}")
        file_input += message[i]
        if message[i] == " " and blank_pause: time.sleep(blank_pause)
        while time.time() - start < delay / len(message): pass
        start = time.time()
    while time.time() - start < pause: pass
    if end == "\0": end = "\n"
    if message != "\0": sys.stdout.write(end)
    if filename != "\0":
        for i in range(len(filename)-1, -1, -1):
            if filename[i] in ["/", "\\"]: os.makedirs(filename[:i], exist_ok = True); break
        with open(filename, "a") as f:
            if message not in  ["\0", "", " "]: f.write(f"[{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}] {file_input}{end}")
            else: f.write(f"{end}")

while True:
    tprint("\nEnter names >> ", end = "", delay = 1.5, blank_pause = 0.15)
    userinput = list(input().split())
    os.system("cls")
    if not len(userinput): continue
    tprint(filename = "C:/combination_log.txt")
    tprint(filename = "C:/combination_log.txt")
    minimum, maximum, cnt = [100], [0], 0
    printed = []
    tprint("Names: " + " ".join(userinput) + "\n", filename = "C:/combination_log.txt")
    if userinput[0][0] == "/":
        for i in range(1, len(userinput)):
            if i == int(userinput[0][1:]): continue
            calc_list(userinput[int(userinput[0][1:])], userinput[i])
    else:
        for i in combinations(userinput, 2):
            calc_list(i[0], i[1])
    if cnt: tprint("min : {0} ({1}) / max : {2} ({3}) / count : {4}".format(minimum[0], " & ".join([str(minimum[i][0]) + ">>" + str(minimum[i][1]) for i in range(1, len(minimum))]), maximum[0], " & ".join([str(maximum[i][0]) + ">>" + str(maximum[i][1]) for i in range(1, len(maximum))]), cnt), delay = 1.5, blank_pause = 0.15, filename = "C:/combination_log.txt")
    else: os.system("cls")