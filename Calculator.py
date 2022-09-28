from math import *
import os
import traceback
import pyperclip
import copy

inputs = []

os.system("cls")

class conv:
    J_eV = 6.242e+18
    eV_J = 1.60218e-19


h = 6.626e-34
c = 3e8
g = 9.80665
G = 6.6743e-11
R = 8.314
r = 0.082
pi = 3.14159265359
Kb = 1.380649e-23
Ke = 8.9875517923e9
Kw = 10 ** -14
NA = 6.022e23
Ryd = 2.1798723611035e-18

prev = ""

while True:
    userinput = input("\033[38;2;255;255;100m>>> \033[38;2;0;255;0m").replace("$prev", prev)

    if userinput[:7] == "\\repeat":
        repeat = int(userinput.split()[1])

        userinput = ((" ".join(userinput.split()[2:]) + " /// ")*repeat)[:-5]

    prev = copy.deepcopy(userinput)

    userinput = list(map(lambda x: x.strip(), userinput.split("///")))

    if userinput == [""]:
        userinput = inputs[-1]

    inputs.append(userinput)

    for i in range(len(userinput)):
        print("\033[38;2;0;255;255m", end = "")
        try:
            ans = eval(userinput[i])
            strans = str(ans)
            for i in range(len(strans)):
                print(strans[i], end = "")
            print()
            pyperclip.copy(strans)
        except:
            try: ans = eval("ans " + userinput[i]); print(ans); pyperclip.copy(str(ans))
            except:
                try: exec(userinput[i])
                except: print(f"\033[38;2;255;72;0mError occurred while executing command {i+1}.\n" + "\033[38;2;255;0;0m" + traceback.format_exc(chain = False).split("\n")[-2])
                