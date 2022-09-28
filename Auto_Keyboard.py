import subprocess
import sys
import time
import datetime


try: import pyperclip
except: subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
finally: import pyperclip

try: import keyboard
except: subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
finally: import keyboard

try: import pyautogui
except: subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
finally: import pyautogui

try: import win32com.client
except: subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
finally: import win32com.client

def kor_to_eng(text):
    first = ['r', 'R', 's', 'e', 'E', 'f', 'a', 'q', 'Q', 't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g']
    second = ['k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l']
    third = ['', 'r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g']
    exception = {'ㄱ': 'r', 'ㄴ': 's', 'ㄷ': 'e', 'ㄹ': 'f', 'ㅁ': 'a', 'ㅂ': 'q', 'ㅅ': 't', 'ㅇ': 'd', 'ㅈ': 'w', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅍ': 'v', 'ㅎ': 'g', 'ㄲ': 'R', 'ㄸ': 'E', 'ㅃ': 'Q', 'ㅆ': 'T', 'ㅉ': 'W', 'ㅏ': 'k', 'ㅑ': 'i', 'ㅓ': 'j', 'ㅕ': 'u', 'ㅗ': 'h', 'ㅛ': 'y', 'ㅜ': 'n', 'ㅠ': 'b', 'ㅡ': 'm', 'ㅣ': 'l', 'ㅐ': 'o', 'ㅒ': 'O', 'ㅔ': 'p', 'ㅖ': 'P', 'ㅘ': 'hk', 'ㅙ': 'ho', 'ㅚ': 'hl', 'ㅝ': 'nj', 'ㅞ': 'np', 'ㅟ': 'nl', 'ㅢ': 'ml'}
    result = ""

    for i in range(len(text)):
        if not 44032 <= ord(text[i]) <= 55203:
            if text[i] in exception: result += exception[text[i]]
            else: result += text[i]
            continue
        result += first[(ord(text[i])-44032)//588] + second[((ord(text[i])-44032)%588)//28] + third[((ord(text[i])-44032)%588)%28]
    return result

def eng_to_kor(text, change_caps = True): # 영어 문자열을 한글로 변환
    caps = ["Q", "W", "E", "R", "T", "O", "P"]
    first = {"r" : "ㄱ", "R" : "ㄲ", "s" : "ㄴ", "e" : "ㄷ", "E" : "ㄸ", "f" : "ㄹ", "a" : "ㅁ", "q" : "ㅂ", "Q" : "ㅃ", "t" : "ㅅ", "T" : "ㅆ", "d" : "ㅇ", "w" : "ㅈ", "W" : "ㅉ", "c" : "ㅊ", "z" : "ㅋ", "x" : "ㅌ", "v" : "ㅍ", "g" : "ㅎ"}
    second = {"k" : "ㅏ", "o" : "ㅐ", "i" : "ㅑ", "O" : "ㅒ", "j" : "ㅓ", "p" : "ㅔ", "u" : "ㅕ", "P" : "ㅖ", "h" : "ㅗ", "hk" : "ㅘ", "ho" : "ㅙ", "hl" : "ㅚ", "y" : "ㅛ", "n" : "ㅜ", "nj" : "ㅝ", "np" : "ㅞ", "nl" : "ㅟ", "b" : "ㅠ", "m" : "ㅡ", "ml" : "ㅢ", "l" : "ㅣ"}
    third = {"" : "", "r" : "ㄱ", "R" : "ㄲ", "rt" : "ㄳ", "s" : "ㄴ" , "sw" : "ㄵ", "sg" : "ㄶ", "e" : "ㄷ", "f" : "ㄹ", "fr" : "ㄺ", "fa" : "ㄻ", "fq" : "ㄼ", "ft" : "ㄽ", "fx" : "ㄾ", "fv" : "ㄿ", "fg" : "ㅀ", "a" : "ㅁ", "q" : "ㅂ", "qt" : "ㅄ", "t" : "ㅅ", "T" : "ㅆ", "d" : "ㅇ", "w" : "ㅈ", "c" : "ㅊ", "z" : "ㅋ", "x" : "ㅌ", "v" : "ㅍ", "g" : "ㅎ"}

    fk = list(first.keys())
    sk = list(second.keys())
    tk = list(third.keys())

    text = list(text)

    if change_caps:
        for i in range(len(text)):
            if text[i] not in caps:
                text[i] = text[i].lower()

    i = -1 # 이중 모음 합치기
    while True:
        if len(text) == 0: break
        i += 1
        if i >= len(text)-1: break

        if "".join(text[i:i+2]) in sk:
            text = text[:i] + ["".join(text[i:i+2])] + text[i+2:]
            i -= 1

    i = -1 # 쌍자음 합치기
    while True:
        if len(text) == 0: break
        i += 1
        if i >= len(text)-1: break

        if text[i] in fk and text[i+1] in fk and (i == len(text) - 2 or text[i+2] not in sk) and "".join(text[i:i+2]) in tk:
            text = text[:i] + ["".join(text[i:i+2])] + text[i+2:]
            i -= 1

    i = -1
    while True: # 단어 조합하기
        if len(text) == 0: break
        i += 1
        if i >= len(text) - 1: break

        # 받침이 없는 단어 조합하기
        if text[i] in fk and text[i+1] in sk and (i >= len(text) -2 or (i <= len(text) - 3 and text[i+2] not in fk and text[i+2] not in tk) or (i <= len(text) - 4 and text[i+2] in fk and text[i+3] in sk)):
            # print("2-character letter detected")
            text = text[:i] + [text[i:i+2] + [""]] + text[i+2:]
            i -= 1
        
        # 받침이 있는 단어 조합하기
        if i <= len(text) - 3 and text[i] in fk and text[i+1] in sk and text[i+2] in tk and (i >= len(text) - 3 or text[i+3] not in sk):
            # print("3-character letter detected")
            text = text[:i] + [text[i:i+3]] + text[i+3:]

    for i in range(len(text)): # 조합된 단어를 한글로 변환하기
        if type(text[i]) == str:
            if text[i] in first.keys(): text[i] = first[text[i]]
            if text[i] in second.keys(): text[i] = second[text[i]]
            if text[i] in third.keys(): text[i] = third[text[i]]
        
        if type(text[i]) == list:
            text[i] = chr(588*(fk.index(text[i][0])) + 28*(sk.index(text[i][1])) + tk.index(text[i][2]) + 44032)

    for i in range(text.count("`")): # "`" 제거하기 (믈ㅅ셕 같은 단어 입력용)
        text.remove("`")

    return "".join(text) # 조합된 단어를 반환하기

def calc(variable_int, variable_str, string, current_iter):
    scope = {}

    code = compile(variable_int + " = " + current_iter, "<string>", "exec")
    exec(code, scope)

    code = compile(variable_str + " = " + "\"" + current_iter + "\"", "<string>", "exec")
    exec(code, scope)

    code = compile(variable_int + variable_str + " = " + string, "<string>", "exec")
    exec(code, scope)

    return scope[variable_int + variable_str]

def wait():
    global delay, put_delay

    start_time = time.time()

    if put_delay:
        while time.time() - start_time < delay:
            ...

Shell = win32com.client.Dispatch("WScript.Shell")

while not keyboard.is_pressed("enter"):
    pass

time.sleep(3)

delay = 0.16

number_of_messengers = 1
repeat = 1000

# /tag{name}{time}
# /htky{*keys}
# /kor{string}{delay}
# /eng{string}{delay}
# /time{format}
# /every{number}{if_true}{if_false}
# /formula{int_var}{str_var}{expr}ation]

message = [
    
]

for i in range(len(message)):
    message[i] = kor_to_eng(message[i])


for i in range(1, repeat + 1):
    for j in range(len(message)):
        k = -1
        put_delay = "/tag" not in message[j]

        while k < len(message[j]) - 1:
            k += 1

            if keyboard.is_pressed("enter"):
                sys.exit(0)

            elif message[j][k:k+4] == "/tag":
                SB = ["", ""]
            
                for l in range(k+5, len(message[j])):
                    if message[j][l] != "}": SB[0] += message[j][l]
                    else: break
            
                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": SB[1] += message[j][l]
                    else: break
                
                k = l

                pyautogui.hotkey("shift", "2")

                for ch in SB[0]:
                    Shell.SendKeys(ch)
                    wait()
                
                time.sleep(int(SB[1]) / 1000)

                Shell.SendKeys("{tab}")

            elif message[j][k:k+5] == "/htky":
                keys = []

                try:
                    l = k + 4
                    while True:
                        keys.append("")
                        for l in range(l+2, len(message[j])):
                            if message[j][l] != "}": keys[-1] += message[j][l]
                            else: break

                        if message[j][l+1] != "{": break
                except: ...

                k = l

                pyautogui.hotkey(*keys)
            
            elif message[j][k:k+4] == "/kor":
                kor = ""
                delay_SB = ""

                for l in range(k+5, len(message[j])):
                    if message[j][l] != "}": kor += message[j][l]
                    else: break

                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": delay_SB += message[j][l]
                    else: break

                k = l

                pyperclip.copy(eng_to_kor(kor))
                time.sleep(int(delay_SB) / 1000)
                keyboard.press_and_release("ctrl + v")
                keys = []

                try:
                    l = k + 4
                    while True:
                        keys.append("")
                        for l in range(l+2, len(message[j])):
                            if message[j][l] != "}": keys[-1] += message[j][l]
                            else: break

                        if message[j][l+1] != "{": break
                except: ...

                k = l

                pyautogui.hotkey(*keys)
            
            elif message[j][k:k+4] == "/eng":
                kor = ""
                delay_SB = ""

                for l in range(k+5, len(message[j])):
                    if message[j][l] != "}": kor += message[j][l]
                    else: break

                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": delay_SB += message[j][l]
                    else: break

                k = l

                pyperclip.copy(kor)
                time.sleep(int(delay_SB) / 1000)
                keyboard.press_and_release("ctrl + v")

            elif message[j][k:k+5] == "/time":
                time_vars = datetime.datetime.now().strftime("%Y %m %d %H %M %S").split()

                time_str = ""

                for l in range(k+6, len(message[j])):
                    if message[j][l] != "}": time_str += message[j][l]
                    else: break

                k = l

                for l in range(6):
                    time_str = time_str.replace(F"#{l+1}", time_vars[l])

                time_str = time_str.replace("#7", str(time.time()).split(".")[1][:3])

                for ch in time_str:
                    Shell.SendKeys(ch)
                    wait()

            elif message[j][k:k+6] == "/every":
                every_num = ""
                if_true = ""
                if_false = ""

                for l in range(k+7, len(message[j])):
                    if message[j][l] != "}": every_num += message[j][l]
                    else: break

                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": if_true += message[j][l]
                    else: break

                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": if_false += message[j][l]
                    else: break

                k = l
                
                if (i - 1) % int(every_num) == 0:
                    for ch in if_true:
                        Shell.SendKeys(ch)
                        wait()
                
                else:
                    for ch in if_false:
                        Shell.SendKeys(ch)
                        wait()
                    
            elif message[j][k:k+8] == "/formula":
                iter_var_int = ""
                iter_var_str = ""
                formula = ""

                for l in range(k+9, len(message[j])):
                    if message[j][l] != "}": iter_var_int += message[j][l]
                    else: break

                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": iter_var_str += message[j][l]
                    else: break

                for l in range(l+2, len(message[j])):
                    if message[j][l] != "}": formula += message[j][l]
                    else: break

                k = l

                for ch in calc(iter_var_int, iter_var_str, formula, str(i)):
                    Shell.SendKeys(ch)
                    wait()

            else:
                Shell.SendKeys(message[j][k])
                wait()

        Shell.SendKeys("{enter}")

        if number_of_messengers != 1: pyautogui.keyDown("alt")
        for _ in range(number_of_messengers - 1): pyautogui.press("tab")
        if number_of_messengers != 1: pyautogui.keyUp("alt")
