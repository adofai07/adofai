import pyscreenshot
import pyautogui
import PIL
import numpy
import time
import os
import sys
import winsound
import shutil

if os.path.isdir("C:/PPT_capture"):
    shutil.rmtree("C:/PPT_capture")

os.makedirs("C:/PPT_capture", exist_ok = True)
max_slide = input("Enter number of slides. Press enter to auto-detect. >> ")
try: max_slide = int(max_slide)
except: max_slide = "auto-detect"
time.sleep(3); pyautogui.press("f5"); time.sleep(5)

for slide in range(10**3):
    image = pyscreenshot.grab(bbox = (0, 0, 1920, 1080))
    image.save("C:/PPT_capture/slide_{:03.0f}.png".format(slide+1))
    screen = PIL.Image.open("C:/PPT_capture/slide_{:03.0f}.png".format(slide+1))
    screen_bitmap = list(numpy.array(screen))
    if max_slide == "auto-detect":
        cnt, full = 0, 0
        for i in screen_bitmap:
            for j in i:
                for k in j:
                    cnt += int(k)
                    full += 255
        print("Brightness of slide {:03.0f}: {:06.3f}% ({:010.0f} of {:010.0f})".format(slide + 1, 100*cnt/full, cnt, full))
        if cnt/full < 0.0015: break
    else:
        if slide == max_slide: break
        time.sleep(0.5) # set this value to 0 if there are no animations
    pyautogui.press("enter")
pyautogui.press("enter")
winsound.Beep(1000, 300)

if max_slide != "auto-detect":
    for slide in range(max_slide + 1):
        screen = PIL.Image.open("C:/PPT_capture/slide_{:03.0f}.png".format(slide+1))
        screen_bitmap = list(numpy.array(screen))
        cnt, full = 0, 0
        for i in screen_bitmap:
            for j in i:
                for k in j:
                    cnt += int(k)
                    full += 255
        print("Brightness of slide {:03.0f}: {:06.3f}% ({:010.0f} of {:010.0f})".format(slide + 1, 100*cnt/full, cnt, full))