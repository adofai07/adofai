from math import *
import os
from time import time, sleep
from sympy.ntheory import factorint
from termcolor import cprint
import keyboard

maxdiv = 0
prime = [2]
p = 3
loadfq = 1440

numColor = "yellow"
timeColor = "yellow"
inputColor = "blue"
''' Can choose between...
grey
red
green
yellow
blue
magenta
cyan
white
'''

start, end, interval = 0, 0, 1

while True:
    while True:
        for i in range(len("Enter a number: ")):
            cprint("Enter a number: "[i], inputColor, end = "")
            sleep(0.01)
        userinput = list(input().split())
        if userinput == []: continue
        else: break

    os.system("cls")

    cprint("Input:", inputColor, end = ' ')
    for i in range(len(userinput)):
        cprint("[" + str(userinput[i]) + "]", inputColor, end = ' ')
    print("\n")
    
    try:
        start, end, interval = int(userinput[0]), int(userinput[0]) + int(userinput[1]), int(userinput[2])
    except:
        try:
            start, end, interval = int(userinput[0]), int(userinput[0]) + int(userinput[1]), 1
        except:
            try:
                start, end, interval = int(userinput[0]), int(userinput[0]) + 1, 1
            except:
                pass

    # print("\nstart = %d" %start)
    # print("end = %d" %end)
    # print("interval = %d\n" %interval)

    start_time = time()


    # c = max(end//loadfq, 1)
    # while prime[-1] < ceil(sqrt(end)):
    #     bad = 0
    #     for i in range(len(prime)):
    #         if p%prime[i] == 0: bad = 1; break
    #         if p < (prime[i])**2: break
    #     if bad == 0: prime.append(p)
    #     p += 2
    #     if (p-1)%9876 == 0:
    #         print(" Loading %.4f%%" %(100*prime[-1]/ceil(sqrt(end))), end = "\r")
    
    # print(" "*100, end = "\r")

    a = 0
    minmaxtime = []

    for testnum in range(start, (end) if interval > 0 else(end-1), interval):
        a += 1
        local_start = time()
        if numColor == "white":
            print(testnum, factorint(testnum))
        else:
            cprint(testnum, numColor, end = " ")
            print(factorint(testnum))
        minmaxtime.append(time() - local_start)
        # if testnum == 0: continue
        # if testnum == 1: print("1 {}"); continue
        # divisor = {}
        # div = 1
        # a = testnum
        # b = 0
        # while a != 1:
        #     for i in range(end):
        #         if a%prime[i] == 0:
        #             divisor[prime[i]] = 0
        #         while a%prime[i] == 0:
        #             a//=prime[i]
        #             divisor[prime[i]] += 1
        #         if prime[i] >= ceil(sqrt(testnum)) or a == 1: break
        #     a = testnum
        #     for i in list(divisor.keys()):
        #         a//=(i**divisor[i])
        #     if a != 1: divisor[a] = 1
        #     if len(divisor) == 0: divisor[testnum] = 1
        #     a = 1
        #     print(testnum, divisor)

        if keyboard.is_pressed("esc"): break

    end_time = time()
    cprint("\nelapsed time = %.3f seconds" %(end_time - start_time), timeColor, end = "")
    cprint(", average time = %.3f seconds" %((end_time - start_time)/a), timeColor, end = "")
    cprint(", minimum time = %.3f seconds" %(min(minmaxtime)), timeColor, end = "")
    cprint(", maximum time = %.3f seconds\n" %((max(minmaxtime))), timeColor)