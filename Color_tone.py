import colorsys
import ctypes
import datetime
import random
import sys
import time
from math import *

import numpy
from PIL import Image, ImageDraw, ImageFont

cout = sys.stdout.write

def NYPC(COLOR, TXTCOLOR, d) -> None:
    TXT = [
        "NEXON",
        "YOUTH",
        "PROGRAMMING",
        "CHALLENGE"
    ]

    for i in range(len(TXT)):
        for j in range(len(TXT[i])):
            bold = (9 if j == 0 else 3)
            grad = tuple((TXTCOLOR[k] * (45 - (j+33)) + COLOR[k] * (j+33))//45 for k in range(3))

            if j != 0:
                d.text(
                    (100 + j * 100, 160 + i * 130),
                    TXT[i][j],
                    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 120),
                    fill = grad,
                    stroke_width = bold
                )

            if j == 0:
                cnt = 0
                for k in range(9, -1, -5):
                    cnt += 1
                    d.text(
                        (100 + j * 100, 160 + i * 130),
                        TXT[i][j],
                        font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 120),
                        fill = (COLOR if cnt%2 == 0 else TXTCOLOR),
                        stroke_width = k
                    )


def make_image_1(path):
    BR = numpy.base_repr
    COLOR = [0, 0, 0]
    MESSAGE = "Diamond V"
    TXTCOLOR = [0, 150, 255]

    COLOR = [0, 0, 0]
    MESSAGE = "Diamond V"
    TXTCOLOR = [0, 150, 255]

    COLOR = tuple(COLOR)
    TXTCOLOR = tuple(TXTCOLOR)

    THIRDCOLOR = (0, 0, 0)
    while THIRDCOLOR in [COLOR, TXTCOLOR]:
        THIRDCOLOR = (
            random.randrange(0, 256),
            random.randrange(0, 256),
            random.randrange(0, 256)
        )


    img = Image.new("RGB", (1920, 1080), color = COLOR)
    # img = Image.open("C:/Themes/Night Rainbow.png")


    d = ImageDraw.Draw(img)
    d.text(
    (10, 870),
    MESSAGE,
    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 120),
    fill = TXTCOLOR,
    stroke_width = 5
    )

    d = ImageDraw.Draw(img)
    d.text(
    (10, 870),
    MESSAGE,
    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 120),
    fill = COLOR,
    stroke_width = 2
    )

    # img.save("C:/Themes/tone.png"); sys.exit(0)

    d.text(
    (10, 792),
    f"RGB ({COLOR[0]}, {COLOR[1]}, {COLOR[2]}) / COLOR CODE " + "#{}{}{}".format(BR(COLOR[0], 16).zfill(2), BR(COLOR[1], 16).zfill(2), BR(COLOR[2], 16).zfill(2)),
    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 35),
    fill = TXTCOLOR,
    stroke_width = 1
    )

    for i in range(1920):
        for j in range(2400 - i, 1080):
            if img.getpixel((i, j)) == COLOR: img.putpixel((i, j), TXTCOLOR)
            else: img.putpixel((i, j), COLOR)

    for i in range(1920):
        for j in range(790, 795):
            if img.getpixel((i, j)) == COLOR: img.putpixel((i, j), TXTCOLOR)
            else: img.putpixel((i, j), COLOR)

    for i in range(1606, 1611):
        for j in range(1080):
            if img.getpixel((i, j)) == COLOR: img.putpixel((i, j), TXTCOLOR)
            else: img.putpixel((i, j), COLOR)

    for i in range(1508, 1708):
        for j in range(692, 892):
            if (i - 1608) ** 2 + (j - 792) ** 2 < 84 ** 2:
                if img.getpixel((i, j)) == COLOR: img.putpixel((i, j), TXTCOLOR)
                else: img.putpixel((i, j), COLOR)
            if (i - 1608) ** 2 + (j - 792) ** 2 < 72 ** 2:
                if img.getpixel((i, j)) == COLOR: img.putpixel((i, j), TXTCOLOR)
                else: img.putpixel((i, j), COLOR)
            if (i - 1608) ** 2 + (j - 792) ** 2 < 60 ** 2:
                if img.getpixel((i, j)) == COLOR: img.putpixel((i, j), TXTCOLOR)
                else: img.putpixel((i, j), COLOR)


    d.text(
    (1700, 750),
    datetime.datetime.today().strftime("%Y-%m-%d"),
    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 35),
    fill = COLOR,
    stroke_width = 1
    )

    d.text(
    (1608, 925),
    f"({TXTCOLOR[0]}, {TXTCOLOR[1]}, {TXTCOLOR[2]})",
    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 35),
    fill = COLOR,
    stroke_width = 1
    )

    d.text(
    (1611, 975),
    "#{}{}{}".format(BR(TXTCOLOR[0], 16).zfill(2), BR(TXTCOLOR[1], 16).zfill(2), BR(TXTCOLOR[2], 16).zfill(2)),
    font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 35),
    fill = COLOR,
    stroke_width = 1
    )

    NYPC(COLOR, TXTCOLOR, d)

    img.save(path)

def make_image_2(path, message, set_to_back = True):
    img = Image.new("RGB", (1920, 1080), color = (0, 0, 0))

    for i in range(0, 1920):
        for j in range(0, 1080):
            c = int(min(255, max(0, (
                int(((i - 960) ** 2 + (j - 540) ** 2) ** 2.5 / 200000000000)
                # + (255 - min(255, max(0, int(((i - 960) ** 2 + (j - 540) ** 2) ** 1.5 / 200000)))) / 3
            ))))
            img.putpixel((i, j), (c, c, c))

    d = ImageDraw.Draw(img)

    WIDTHS = [24, 22, 18, 16, 12, 10, 6, 4]

    for i in range(len(WIDTHS)):
        d.text(
        (10, 180),
        message,
        font = ImageFont.truetype("C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf", 520),
        fill = (255, 255, 255) if i%2 == 0 else (0, 0, 0),
        stroke_width = WIDTHS[i]
        )

    img.save("C:/Themes/temp.png")

    for i in range(0, 1920):
        for j in range(0, 1080):
            if any(img.getpixel((i, j))):
                SUM3 = sum(img.getpixel((i, j))) // 3
                img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i + j + 8500) / 2900, 1, SUM3 / 255)))

    img.save(path)

    if set_to_back:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

def make_image_3(read_path, save_path, format = "png"):
    img = Image.open(read_path)
    d = ImageDraw.Draw(img)

    DIV = 5000

    for i in range(0, 10 ** 10):
        try:
            for j in range(0, 10 ** 10):
                if any(img.getpixel((i, j))):
                    SUM3 = sum(img.getpixel((i, j))) / 3
                    img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i - j + 6600) / DIV, 1, SUM3 / 255)))
        except: ...
        cout(F"Doing column {i}...\r")
        if j == 0: break

    print()

    img.save(save_path + "_1." + format)

    try:
        for i in range(0, 10 ** 10):
            try:
                for j in range(0, 10 ** 10):
                    img.putpixel((i, j), tuple(255 - i for i in img.getpixel((i, j))))
            except: ...
            cout(F"Doing column {i}...\r")
            if j == 0: raise EOFError("End of Image")
    except: ...

    print()

    img.save(save_path + "_2." + format)


# make_image_3("C:/Themes/Futuristic Technical Theme.jpg", "C:/Themes/BW1")
# make_image_3("C:/Themes/ROG G14 Knolling.jpg", "C:/Themes/BW3")
# make_image_3("C:/Themes/KakaoTalk_20220921_144301078.jpg", "C:/Themes/BIO")

# make_image_2("C:/Themes/adofai.png", R"SSHS34", True)

img = Image.new("RGB", (22, 42), color = (255, 255, 255))
img.save("C:/Themes/WHITE.png")