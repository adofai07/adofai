from urllib.request import *
from bs4 import BeautifulSoup
import time
import pyperclip
import traceback
import sys
import requests
import os
import colorsys

FOUND = False
tot = []

cnt = 1
while True:
    tot = list(set(tot))
    if not FOUND:
        if len(tot):
            for i in range(len(tot)-1, -1, -1):
                if "  " in tot[i]:
                    tot.extend(tot[i].split("  "))
                    tot.pop(i)
                if "More Like This" in tot[i]:
                    tot.pop(i)

            for i in range(len(tot)-1, -1, -1):
                if len(tot[i]) < 10:
                    tot.pop(i)

            for hue in range(len(tot)):
                color = [int(c*255) for c in colorsys.hsv_to_rgb(hue*0.075, 1, 1)]
                print("\033[38;2;{};{};{}m".format(*color) + tot[hue])
        print("\033[38;2;255;255;255m", end = "")
        
        word = input(f"\nWord {cnt} >> ")
        os.system("cls")
        print(f"Definition of \"{word}\"")
        cnt += 1
        URL = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
        res = ""
        tot = []

    else:
        if "_" not in URL:
            URL += "_1"
    
        else:
            curr_idx = int(URL.split("_")[-1])
            URL = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}_{curr_idx+1}"

    FOUND = True

    # URL = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"

    try:
        print(f"\033[38;2;52;52;52mConnecting to {URL}\033[38;2;255;255;255m")

        req = Request(URL, headers = {"User-Agent": "Mozila/5.0"})
        webpage = urlopen(req)
        soup = str(BeautifulSoup(webpage, features = "lxml")).replace("<span class=\"eb\">", "")

        soup = soup[:(len(soup)) - "".join(reversed(soup)).index("smoidI")]
    
    except: FOUND = False

    while True:
        if "<span class=\"def\" hclass=\"def\" htag=\"span\">" in soup:
            idx = soup.index("<span class=\"def\" hclass=\"def\" htag=\"span\">") + 43
        
        elif "<span class=\"def\" htag=\"span\" hclass=\"def\">" in soup:
            idx = soup.index("<span class=\"def\" htag=\"span\" hclass=\"def\">") + 43

        else: break


        try:
            i = idx-1
            while True:
                i += 1

                if soup[i:i+10] == "</span><ul": break
                if soup[i:i+17] == "</span></span><ul": break
                if soup[i+8:i+27] == "<span class=\"xrefs\"": break
                if soup[i:i+5] in [f"</h{i}>" for i in range(1, 7)]: break
                if soup[i:i+7] == "</span>": i += 7
                if soup[i] == "<":
                    while soup[i] != ">":
                        i += 1
                    continue
                res += soup[i]
            
            res += "\0"

        except: pass

        # res = "\n".join(res.split("\0")[:-1])
            
        for r in res.split("\0")[:-1]:
            if r.count("\n") > 0: continue
            tot.append(r)

        soup = soup[i:]
