import glob
import os
import time

import numpy
import PIL
import pyautogui

for f in glob.glob("C:/Python_Programs/Screen_capture/*"):
    print(f"Removing {f}...")
    os.remove(f)

images = []

time.sleep(10)

for i in range(36**4):
    current = "C:/Python_Programs/Screen_capture/screenshot_{}.png".format(numpy.base_repr(i, 36).zfill(4))
    prev = "C:/Python_Programs/Screen_capture/screenshot_{}.png".format(numpy.base_repr(i-1, 36).zfill(4))

    images.append(pyautogui.screenshot(current))

    if i == 0: continue

    if PIL.Image.open(current) != PIL.Image.open(prev):
        os.system("Rundll32.exe user32.dll,LockWorkStation")
