import copy
import math
import os
import numpy
import sys

import matplotlib.pyplot

global memory

SIZE = 110000000
width = os.get_terminal_size()[0]

memory = [0 for _ in range(SIZE+1)]
# memory = numpy.zeros(SIZE+1, dtype = numpy.int8)

def collatz(n):
    _n = copy.deepcopy(n)
    step = 0
    while n > 1:
        if (n % 2):
            n = (3*n + 1)//2
            step += 2
        else:
            n = n//2
            step += 1
        if n <= SIZE and memory[n] != 0:
            memory[_n] = step + memory[n]
    memory[_n] = step

start = 1

try:
    f = open("./collatz.txt", "r")
    alldata = f.readlines()
    f.close()
    start = int(alldata[-1].split()[0])
    for i in alldata:
        number, process = i.split()
        number = int(number)
        process = int(process)
        memory[number] = process
except: pass

UPDATE = (SIZE - start + 1) // width // 10 + 1

res = ""

for i in range(start+1, SIZE+1):
    collatz(i)
    res += f"{i} {memory[i]}\n"
    if i%UPDATE == 0 or i == SIZE:
        sys.stdout.write("{:06.2f}% ".format(100 * (i - start + 1) / (SIZE - start + 1)) + "\033[38;2;0;255;0m" + "="*(math.ceil((width-8) * (i - start + 1) / (SIZE - start + 1))) + "\033[38;2;255;255;255m" + "="*((width-8) - math.ceil(width * (i - start + 1) / (SIZE - start + 1))) + "\r")
        f = open("./collatz.txt", "a+")
        f.write(res)
        f.close()
        res = ""

# print("\033[38;2;0;255;0m" + "="*width + "\033[38;2;255;255;255m")
print()
input("Done! Press enter to show graph >> ")

matplotlib.pyplot.scatter(x = [i for i in range(1, SIZE + 1)], y = memory[1:SIZE+1], s = 0.08, c = [([0, 0, 0] if i < start else [0, 1, 0]) for i in range(SIZE)])
matplotlib.pyplot.show()
