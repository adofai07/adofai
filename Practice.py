import os
import time
import sys

def tprint(message, end = "\0", delay = 0, pause = 0, blank_pause = 0, color = (255, 255, 255)):
    message = str(message)
    blank = 0
    start = time.time()
    i = -1
    while i < len(message) - 1:
        i += 1
        if message[i:i+6] == "\\color":
            for j in range(i+7, len(message)):
                if message[j] == " " and message[j-1] != ",": break

            temp = message[i+7:j]
            for k in range(len(temp)):
                if temp[k] == ",": temp = temp[:k] + " " + temp[k+1:]

            color = tuple(map(int, "".join(temp).split()))
            i = j + 1
        sys.stdout.write(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{message[i]}")
        if message[i] == " " and blank_pause: time.sleep(blank_pause)
        while time.time() - start < delay / len(message): pass
        start = time.time()
    while time.time() - start < pause: pass
    if end == "\0": sys.stdout.write("\n")
    else: sys.stdout.write(end)

tprint(("-"*1000)[:os.get_terminal_size()[0]], delay = 2, color = (0, 255, 255))
os.system("cls")

tprint(f"Executing at \\color 0, 255, 255 {os.getcwd()}", delay = 1.5, blank_pause = 0.15)
tprint(f"Terminal size : \\color 255, 255, 180 {list(os.get_terminal_size())[0]} * {list(os.get_terminal_size())[1]}", delay = 2, blank_pause = 0.2, pause = 1)
tprint(f"Username : \\color 255, 255, 0 {os.getlogin()}", delay = 2, blank_pause = 0.2, pause = 1)

output = os.popen("ipconfig/all").read()

output = list(output.split("\n"))

for i in range(len(output)):
    output[i] = list(output[i])
    for _ in range(output[i].count(" ")):
        output[i].remove(" ")
    output[i] = "".join(output[i])

for _ in range(output.count("")):
    output.remove("")

for i in range(len(output)):
    if output[i][:14] ==  "호스트이름........:": desktop_name = output[i][14:]
    if output[i][:16] ==  "IPv4주소.........:": IPv4_address = output[i][16:-6]
    if output[i][:16] ==  "링크-로컬IPv6주소....:": IPv6_address = output[i][16:-8]

tprint(f"Desktop name : \\color 255, 0, 255 {desktop_name}", delay = 2, pause = 1, blank_pause = 0.2)
tprint(f"IPv4 address : \\color 255, 0, 127 {IPv4_address}", delay = 2, pause = 1, blank_pause = 0.2)
tprint(f"IPv6 address : \\color 255, 0, 0 {IPv6_address}", delay = 2, pause = 1, blank_pause = 0.2)
input("Press enter to terminate...")