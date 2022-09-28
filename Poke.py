import copy
import os
import sys
import time

import_error = []

try: import cv2
except: import_error.append("opencv-python")

try: import keyboard
except: import_error.append("keyboard")

try: import numpy
except: import_error.append("numpy")

try: import PIL
except: import_error.append("pillow")

try: import pyautogui
except: import_error.append("pyautogui")

try: import pyscreenshot
except: import_error.append("pyscreenshot")

try: import pyclovaocr
except: import_error.append("pyclovaocr")

if len(import_error):
    print("\033[38;2;255;0;0mError occurred. Please open cmd and type \"\033[38;2;255;255;255mpip install {}\033[38;2;255;;0m\".\033[38;2;255;255;255m".format(" ".join(import_error)))
    sys.exit(0)


POKE_LIMIT = 10
POKE_PATH = "./poke_alert.png"

os.system("cls")

print("\033[38;2;255;255;255mChecking if\033[38;2;0;255;0m ./poke_alert.png\033[38;2;255;255;255m exists...")

print()

print("Please turn on\033[38;2;255;0;255m https://www.facebook.com/pokes\033[38;2;255;255;255m and wait.")
print("Press\033[38;2;127;255;255m ctrl + alt + b\033[38;2;255;255;255m to break.")
print("Search will start in 5 seconds...\n")

timeout = 3

while not os.path.exists(POKE_PATH):
    print("Making\033[38;2;0;255;0m poke_alert.png\033[38;2;255;255;255m since it didn\'t exist...")
    pyautogui.screenshot("./screenshot.png")

    words = pyclovaocr.ClovaOCR().run_ocr(
		image_path = "./screenshot.png",
		language_code = "ko",
		ocr_mode = "general"
	)["words"]

    os.remove("./screenshot.png")

    found = False

    try:
        for word in words:
            if "나도" in word["text"]: found = True; break
    except: pass


    if not found:
        timeout = int(timeout*1.2 + 3)
        temp = copy.deepcopy(timeout)
        effect_start_time = time.time()
        while time.time() - effect_start_time < timeout:
            sys.stdout.write("Trying again in {} seconds\r".format("{:.02f}".format(timeout + effect_start_time - time.time()).zfill(len(str(timeout))+3)))
        print("\n")
        continue

    pyscreenshot.grab(bbox = (word["boundingBox"][0][0], word["boundingBox"][0][1], word["boundingBox"][2][0], word["boundingBox"][2][1], )).save(POKE_PATH)

print("-"*os.get_terminal_size()[0])
poked = 0


while not keyboard.is_pressed("ctrl + alt + b"):
    button_pos = list(map(lambda x: [*x], pyautogui.locateAllOnScreen(POKE_PATH)))

    print(f"Poked {poked} times", end = "\r")
    
    for i in range(min(len(button_pos), POKE_LIMIT)):
        pyautogui.click(x = button_pos[i][0] + button_pos[i][2]//2, y = button_pos[i][1] + button_pos[i][3]//2)
        poked += 1
