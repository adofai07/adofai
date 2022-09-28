import re

def pad(string):
    padding = 45

    for i in string:
        if 44032 <= ord(i) < 55204: padding -= 2
        else: padding -= 1

    return string + " "*padding

f = open("/SSHS/codes/Batch/Networks.txt", "r", encoding = "utf-8")
networks = list(map(lambda x: x.strip(), f.readlines()))
f.close()

f = open("/SSHS/codes/Batch/Profiles.txt", "r", encoding = "utf-8")
profiles = list(map(lambda x: x.split(":")[1].strip(), re.findall("Key Content.+", "".join(f.readlines()))))
f.close()

for net, pw in zip(networks, profiles):
    print("{}{} {}{}".format(pad(net), "\033[38;2;0;255;0m", pw, "\033[38;2;255;255;255m"))