from PIL import Image, ImageDraw, ImageFont
import datetime
import ctypes
from urllib import request
import os
import time
import colorsys
import traceback
import math

def log_time(f: callable):
    import time
    def wrapper(*args):
        start = time.time()
        f(*args)
        print("{}() -> {:.4f}".format(f.__name__, time.time() - start))
    return wrapper

img = Image.new("RGB", (1920, 1080), color = (16, 19, 22))
d = ImageDraw.Draw(img)
w = ["Couldn't get data", "Couldn't get data"]
schedule = int(time.time())

WHITE1 = []
WHITE2 = []

def blit(message, coord, fontsize = 15, color = (255, 255, 255), strk_width = 2, fnt_path = "C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf"):
    global img, d

    fnt = ImageFont.truetype(fnt_path, fontsize)
    d.text(coord, str(message), font = fnt, fill = color,  stroke_width = strk_width)

def weather():
    global img, d
    
    res = ["", ""]
    URL = "https://weather.naver.com/"
    response = request.urlopen(URL)
    page = response.read().decode("utf-8")

    f = open("weather.txt", "w", encoding = "utf-8"); f.write(page); f.close()

    for i in range(page.index("현재 온도")+12, 10 ** 10):
        if page[i:i+21] == "<span class=\"degree\">": break
        res[0] += page[i]
    
    res[0] += chr(176) + "C"

    for i in range(i, 10 ** 10):
        if ord(page[i]) == 176: break

    for i in range(i+1, 10 ** 10):
        if ord(page[i]) == 176: break
    
    for j in range(i-1, -1, -1):
        if page[j] not in "0123456789.": break
    
    if page[j-3:j-1] == "up": res[0] += f" (+{page[j+1:i]})"
    else: res[0] += f" (-{page[j+1:i]})"

    for i in range(len(page)-1, -1, -1):
        if page[i:i+4] == "humd": break
    
    for j in range(i+6, len(page)):
        if page[j] == ",": break
    
    res[1] += page[i+6:j] + "%"
    
    return res

def setWallPaper(memo_weather):
    global img, d

    BACKCOLOR = tuple(round(c*255) for c in colorsys.hsv_to_rgb(time.time() / 250, 1, 1))
    BACKCOLOR = (100, 100, 100)
    TXTCOLOR = tuple(255 - BACKCOLOR[i] for i in range(3))

    img = Image.new("RGB", (1920, 1080), color = BACKCOLOR)
    d = ImageDraw.Draw(img)

    print("Making wallpaper for {}".format(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
    blit(
    datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + ".{}".format(str(time.time() % 1)[2])
    , (100, 150), fontsize = 100, color = TXTCOLOR
    )

    wkday = datetime.datetime.today().strftime("%a").upper()
    if wkday == "SAT": blit(wkday, (1500, 150), fontsize = 100, color = TXTCOLOR)
    elif wkday == "SUN": blit(wkday, (1500, 150), fontsize = 100, color = TXTCOLOR)
    else: blit(wkday, (1500, 150), fontsize = 100, color = TXTCOLOR)


    try: w = weather(); memo_weather = w
    except: w = memo_weather

    blit("Temperature: " + w[0], (100, 350), fontsize = 75, color = TXTCOLOR)
    blit("Humidity: " + w[1], (100, 450), fontsize = 75, color = TXTCOLOR)

    img.save("C:/Themes/test.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Themes/test.png", 0)

    return memo_weather

def weather():
    global img, d
    
    res = ["", ""]
    URL = "https://weather.naver.com/"
    response = request.urlopen(URL)
    page = response.read().decode("utf-8")

    f = open("weather.txt", "w", encoding = "utf-8"); f.write(page); f.close()

    for i in range(page.index("현재 온도")+12, 10 ** 10):
        if page[i:i+21] == "<span class=\"degree\">": break
        res[0] += page[i]
    
    res[0] += chr(176) + "C"

    for i in range(i, 10 ** 10):
        if ord(page[i]) == 176: break

    for i in range(i+1, 10 ** 10):
        if ord(page[i]) == 176: break
    
    for j in range(i-1, -1, -1):
        if page[j] not in "0123456789.": break
    
    if page[j-3:j-1] == "up": res[0] += f" (+{page[j+1:i]})"
    else: res[0] += f" (-{page[j+1:i]})"

    for i in range(len(page)-1, -1, -1):
        if page[i:i+4] == "humd": break
    
    for j in range(i+6, len(page)):
        if page[j] == ",": break
    
    res[1] += page[i+6:j] + "%"
    
    return res

@log_time
def setWallPaper2(memo_weather):
    global img, d, WHITE1

    TIME = time.time()

    img = Image.new("RGB", (1920, 1080), color = (0, 0, 0))
    d = ImageDraw.Draw(img)

    dates = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S").split("-")
    # dates[-1] += ".{}".format(str(TIME % 1)[2])

    GRID = [
        "  YEAR >>",
        " MONTH >>",
        "   DAY >>",
        "  HOUR >>",
        "MINUTE >>",
        "SECOND >>"
    ]

    for i in range(6):
        for j in range(8):
            blit(GRID[i][j], (50 + 80 * j, 81 + 170 * i), fontsize = 50, color = (255, 255, 255), strk_width = 1)

        blit(dates[i], (745, 34 + 170 * i), fontsize = 120, color = (255, 255, 255), strk_width = 3)

    for i in range(725, 1920):
        if i < 890: LEFT, RIGHT = 1, 1080
        else: LEFT, RIGHT = 1, 170
        
        for j in range(LEFT, RIGHT):
            if any(img.getpixel((i, j))):
                SUM3 = sum(img.getpixel((i, j))) // 3
                img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i - j + TIME) / 1300, 1, SUM3 / 255)))

    
    blit("Made by", (1300, 150), 50, strk_width = 1)
    blit("ADOFAI", (1300, 190), 120, strk_width = 1, fnt_path = "C:/Pygame_fonts/TrainOne-Regular.ttf")

    if len(WHITE1) == 0:
        for i in range(1290, 1800):
            for j in range(150, 350):
                if any(img.getpixel((i, j))):
                    WHITE1.append((i, j))
                    SUM3 = sum(img.getpixel((i, j))) // 3
                    img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i - j + TIME) / 1300, 1, SUM3 / 255)))

    else:
        for wp in WHITE1:
            i, j = wp
            SUM3 = sum(img.getpixel((i, j))) // 3
            img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i - j + TIME) / 1300, 1, SUM3 / 255)))


    RADIUS = 120

    if len(WHITE2) == 0:
        for i in range(1300, 1800):
            for j in range(450, 950):
                if (i - 1550) ** 2 + (j - 700) ** 2 < RADIUS ** 2:
                    WHITE2.append((i, j))
                    img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i - j + TIME) / 1300, 1, 1 - (((i - 1550) ** 2 + (j - 700) ** 2) ** 0.5 / RADIUS))))

    else:
        for pos in WHITE2:
            i, j = pos
            img.putpixel((i, j), tuple(round(c*255) for c in colorsys.hsv_to_rgb((i - j + TIME) / 1300, 1, 1 - (((i - 1550) ** 2 + (j - 700) ** 2) ** 0.5 / RADIUS))))


    wkday = datetime.datetime.today().strftime("%a").upper()

    img.save("C:/Themes/test.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Themes/test.png", 0)

    return memo_weather


for _ in range(10 ** 20):
    if time.time() > schedule:
        try:
            w = setWallPaper2(w)
        except: print("\033[38;2;255;0;0m" + traceback.format_exc(chain = False).split("\n")[-2] + "\033[38;2;255;255;255m")
        schedule = int(time.time()) + 1
    else: ...