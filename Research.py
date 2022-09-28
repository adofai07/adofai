import os
import sys
import time
import random
import math

# sys.stdout = open("Research.txt", "a+")
cout = sys.stdout.write

f = open("Research.txt", "w")
f.close()

f = open("Research2.txt", "w")
f.close()

f = open("Research3.txt", "w")
f.close()

def CountingSort(array):
    maximum = max(array)
    size = maximum + 1

    count = [0 for _ in range(size)]

    for i in array: 
        count[i] += 1

    for i in range(1, size):
        count[i] += count[i-1] 

    output = [0] * len(array)

    i = len(array) - 1

    while i >= 0:
        curr = array[i]
        count[curr] -= 1
        new = count[curr]
        output[new] = curr
        i -= 1

    return output

def QuickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left, mid, right = [], [], []

    for n in array:
        if n < pivot: left.append(n)
        elif n > pivot: right.append(n)
        else: mid.append(n)

    return QuickSort(left) + mid + QuickSort(right)

def MasterSort(array, integer) -> float:
    start_time = time.time()

    if integer%2 == 0: CountingSort(array)
    if integer%2 == 1: QuickSort(array)

    return time.time() - start_time

def GetFasterSort(N, K):
    array = [random.randrange(0, K) for _ in range(N)]

    integer = random.randrange(0, 2)

    Sort1 = MasterSort(array, integer)
    Sort2 = MasterSort(array, integer+1)

    return (
        "CQouuinctk"[(int(Sort1 < Sort2) + integer)%2::2],
        Sort1 if integer%2 == 0 else Sort2,
        Sort2 if integer%2 == 0 else Sort1
    )

def fprint(string, path = "Research.txt", auto_newline = False, to_terminal = True):
    f = open(path, "a+")
    f.write(string + ("\n" if auto_newline else ""))
    f.close()

    if to_terminal: sys.stdout.write(string + ("\n" if auto_newline else ""))

N, K = 100, 600

TRIES = 200
CHANGE = 0.04
BOUND = 1.01

VECTOR = [15, 80]

ACCSUM = 0
ACCCNT = 0

MEMORY = []
LAST_FASTER = None

while True:
    FasterCount = {
        "Count": 0,
        "Quick": 0
    }

    TimeCount = {
        "Count": 0,
        "Quick": 0
    }

    for i in range(TRIES // 100):
        for j in range(100):
            FasterSort, CountTime, QuickTime = GetFasterSort(N, K)

            FasterCount[FasterSort] += 1
            TimeCount["Count"] += CountTime
            TimeCount["Quick"] += QuickTime

        cout("{:02.0f}%\r".format(10000 * (i+1) / TRIES))
    
    if abs(TimeCount["Count"] - TimeCount["Quick"]) < 0.01:
        MEMORY.append((N, K))

    if TimeCount["Count"] < TimeCount["Quick"]:
        LAST_FASTER = "Count"
    else:
        LAST_FASTER = "Quick"


    CHANGE *= 0.9999


    fprint("N = {} / K = {} (Count = {:.6f}, Quick = {:.6f}) Vector = {:04.01f}° CHANGE = {:.04f}°\n".format(
        N, K, TimeCount["Count"], TimeCount["Quick"], VECTOR[1], CHANGE
    ))

    fprint(F"{N} {K}", path = "Research2.txt", auto_newline = True, to_terminal = False)

    try:
        if 1/BOUND < TimeCount["Count"] / TimeCount["Quick"] < BOUND:
            fprint(F"{N} {K}", path = "Research3.txt", auto_newline = True, to_terminal = False)
    except: ...
    
    if TimeCount["Count"] > TimeCount["Quick"]: VECTOR[1] -= CHANGE
    else: VECTOR[1] += CHANGE

    N += int(VECTOR[0] * math.cos(VECTOR[1] * math.pi / 180))
    K += int(VECTOR[0] * math.sin(VECTOR[1] * math.pi / 180))