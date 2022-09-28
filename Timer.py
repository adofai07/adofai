import os
import pygame
import  keyboard
from time import time, sleep
import copy
from math import *
import random
import sys

def prevent_crash(enable_exit = True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if enable_exit == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

def set_key():
    global key_was_pressed
    key_was_pressed = {chr(i) : 0 for i in range(97, 123)}
    for i in range(10):
        key_was_pressed[str(i)] = 0
    key_was_pressed["shift"] = 0
    key_was_pressed["enter"] = 0
    key_was_pressed["space"] = 0
    key_was_pressed["backspace"] = 0
    key_was_pressed["up arrow"] = 0
    key_was_pressed["down arrow"] = 0
    key_was_pressed["left arrow"] = 0
    key_was_pressed["right arrow"] = 0

def open_window(idle_start):
    global screen, screen_size, programStartTime, key_was_pressed
    currentTime = time()

    pygame.init()
    Color = (0, 0, 0)
    screen = pygame.display.set_mode((screen_size*16, screen_size*9))
    done = False
    clock = pygame.time.Clock()
    delay = 0

    while True:
        prevent_crash()

        screen.fill((0, 0, 0))
        delay = time() - currentTime
        currentTime = time()

        idle_start -= delay

        blit(f"현재 화면 크기: {screen_size}", 40, (0.5, 0.5), (255, 255, 255), False)
        blit("", 40, (0.5, 0.2), (255, 255, 255), False)
        blit("{:06.2f}".format(idle_start) + "초 후 자동 시작", 30, (0.2, 0.9), (255, 255, 255), True)

        if keyboard.is_pressed("up arrow"):
            key_was_pressed["up arrow"] = 1
            screen_size += 1
            break

        if keyboard.is_pressed("down arrow"):
            key_was_pressed["down arrow"] = 1
            screen_size -= 1
            break

        if keyboard.is_pressed("enter") and not key_was_pressed["enter"]:
            key_was_pressed["enter"] = 1
            screen.fill((0, 0, 0))
            startGame()

        if idle_start <= 0:
            screen.fill((0, 0, 0))
            startGame()

        if key_was_pressed["enter"] and not keyboard.is_pressed("enter"):
            key_was_pressed["enter"] = 0
    
    pygame.quit()
    open_window(idle_start)

def blit(message, fontSize, coord, color, condition):
    if color == "white":
        color = (255, 255, 255)
    if color == "red":
        color = (255, 0, 0)
    if color == "green":
        color = (0, 255, 0)
    if color == "blue":
        color = (0, 0, 255)
    if color == "purple":
        color = (255, 0, 255)
    
    if coord == "middle":
        coord = (0.5, 0.5)

    font = pygame.font.SysFont('malgungothic', (screen_size*fontSize//50)) 
    text = font.render(str(message), True, color)
    textRect = text.get_rect()
    textRect.center = (int(coord[0]*screen_size*16), int(coord[1]*screen_size*9))
    screen.blit(text, textRect)
    if condition:
        pygame.display.update()

def time_is_correct():
    global time_
    if time_ == "": return False
    char_index = []
    seconds = 0
    time_ = list(time_)
    inputIsCorrect = True
    for i in range(len(time_)):
        if time_[i] in ["D", "H", "M", "S"]:
            char_index.append(i)
    char_index = [-1] + char_index
    for i in range(len(char_index)-1):
        if not "".join(time_[char_index[i]+1: char_index[i+1]]).isdigit():
            inputIsCorrect = False
    if char_index[-1] != len(time_)-1: inputIsCorrect = False
    if inputIsCorrect:
        for i in range(len(char_index)-1):
            seconds += int("".join(time_[char_index[i]+1: char_index[i+1]])) * {"D" : 86400, "H":3600, "M":60, "S":1}[time_[char_index[i+1]]]
        time_ = "".join(time_)
        return seconds
    else:
        time_ = "".join(time_)
        return False

def get_time():
    global key_was_pressed, time_
    screen.fill((0, 0, 0))
    time_ = ""
    char_index = []
    seconds = 0
    key_was_pressed["enter"] = 0

    while True:
        for i in range(10):
            if keyboard.is_pressed(str(i)) and not key_was_pressed[str(i)]:
                key_was_pressed[str(i)] = 1
                time_ += str(i)
            if key_was_pressed[str(i)] and not keyboard.is_pressed(str(i)):
                key_was_pressed[str(i)] = 0

        if keyboard.is_pressed("enter") and not key_was_pressed["enter"] and time_is_correct():
            key_was_pressed["enter"] = 1
            return time_is_correct()
        if keyboard.is_pressed("enter") and not key_was_pressed["enter"]:
            key_was_pressed["enter"] = 1

        if keyboard.is_pressed("h") and not key_was_pressed["h"]:
            key_was_pressed["h"] = 1
            time_ += "H"
        if keyboard.is_pressed("m") and not key_was_pressed["m"]:
            key_was_pressed["m"] = 1
            time_ += "M"
        if keyboard.is_pressed("s") and not key_was_pressed["s"]:
            key_was_pressed["s"] = 1
            time_ += "S"
        if keyboard.is_pressed("d") and not key_was_pressed["d"]:
            key_was_pressed["d"] = 1
            time_ += "D"
        if keyboard.is_pressed("backspace") and not key_was_pressed["backspace"]:
            key_was_pressed["backspace"] = 1
            time_ = time_[0:len(time_)-1]
            
        if not keyboard.is_pressed("enter"):
            key_was_pressed["enter"] = 0
        if not keyboard.is_pressed("h"):
            key_was_pressed["h"] = 0
        if not keyboard.is_pressed("m"):
            key_was_pressed["m"] = 0
        if not keyboard.is_pressed("s"):
            key_was_pressed["s"] = 0
        if not keyboard.is_pressed("d"):
            key_was_pressed["d"] = 0
        if not keyboard.is_pressed("backspace"):
            key_was_pressed["backspace"] = 0

        screen.fill((0, 0, 0))
        blit("Enter time", 80, (0.5, 0.2), (255, 255, 255), False)
        blit(time_, 50, (0.5, 0.5), ((0, 255, 255) if time_is_correct() else (255, 0, 0)), False)
        if time_is_correct(): blit(str(time_is_correct()) + " seconds", 45, (0.5, 0.8), (0, 255, 255), True)
        else: blit("NaN", 80, (0.5, 0.8), (255, 0, 0), True)

def rect(color, position, condition):
    pygame.draw.rect(screen, color, (screen_size*16*position[0], screen_size*9*position[1], screen_size*16*position[2], screen_size*9*position[3]))
    if condition: pygame.display.update()

def get_color(t1, t2):
    if color_over_time == "random": color = [random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)]
    elif color_over_time == "random_white": color = [random.randrange(200, 255), random.randrange(200, 255), random.randrange(200, 255)]
    elif color_over_time == "random_red": color = [random.randrange(200, 255), random.randrange(0, 56), random.randrange(0, 56)]
    elif color_over_time == "random_green": color = [random.randrange(0, 56), random.randrange(200, 255), random.randrange(0, 56)]
    elif color_over_time == "random_blue": color = [random.randrange(0, 56), random.randrange(0, 56), random.randrange(200, 255)]
    elif type(color_over_time) == list and color_over_time[0] == "random_custom": color = [random.randrange(max(0, color_over_time[1]-55), min(255, color_over_time[1]+55)), random.randrange(max(0, color_over_time[2]-55), min(255, color_over_time[2]+55)), random.randrange(max(0, color_over_time[3]-55), min(255, color_over_time[3]+55))]
    else: color = color_over_time[max(((t1/t2)*100)//1, -1)]

    return color

def startGame():
    global effect_duration, color
    timeLimit = get_time()
    timeLeft = copy.deepcopy(timeLimit)
    currentTime = time()
    color = [0, 0, 0]

    while timeLeft > -30:
        prevent_crash()

        delay = time() - currentTime
        currentTime = time()

        if keyboard.is_pressed("esc"):
            open_window(100)

        timeLeft -= delay


        screen.fill((0, 0, 0))
        if 0 < timeLeft%1 < effect_duration/2:
            color = get_color(timeLeft, timeLimit)

            blit(int(timeLeft), time_font_size, (0.5, 0.3), ((color[0]*(timeLeft%1)/effect_duration)//1, (color[1]*(timeLeft%1)/effect_duration)//1, (color[2]*(timeLeft%1)/effect_duration)//1), False)
            blit(int(timeLeft-1), time_font_size, (0.5, 0.3), (color[0]-(color[0]*(timeLeft%1)/effect_duration)//1, color[1]-(color[1]*(timeLeft%1)/effect_duration)//1, color[2]-(color[2]*(timeLeft%1)/effect_duration)//1), False)
        elif effect_duration/2 <= timeLeft%1 <= effect_duration:
            color = get_color(timeLeft, timeLimit)

            blit(int(timeLeft-1), time_font_size, (0.5, 0.3), (color[0]-(color[0]*(timeLeft%1)/effect_duration)//1, color[1]-(color[1]*(timeLeft%1)/effect_duration)//1, color[2]-(color[2]*(timeLeft%1)/effect_duration)//1), False)
            blit(int(timeLeft), time_font_size, (0.5, 0.3), ((color[0]*(timeLeft%1)/effect_duration)//1, (color[1]*(timeLeft%1)/effect_duration)//1, (color[2]*(timeLeft%1)/effect_duration)//1), False)
        else:
            blit(int(timeLeft), time_font_size, (0.5, 0.3), color, False)

        if timeLeft > 0: rect(color, (0, 0.85, timeLeft/timeLimit, 0.05), True)
        else: pygame.display.update()

    
    open_window(5)

def group(text, keyword, conv_str_to_num):
    keyword.sort(key = len)
    text = list(text)

    i = -1
    while True:
        i += 1
        if i >= len(text): break

        for j in keyword:
            if "".join(text[i:i+len(j)]) == j:
                text = text[:i] + [j] + text[i+len(j):]
                break

    numbers = [str(i) for i in range(10)]

    i = -1
    while True:
        i += 1
        if i > len(text) - 2: break

        if "".join(text[i:i+2]).isdigit():
            text = text[:i] + ["".join(text[i:i+2])] + text[i+2:]
            i -= 1
        

    if conv_str_to_num:
        for i in range(len(text)):
            try: text[i] = int(text[i])
            except:
                try: text[i] = float(text[i])
                except: pass

    return text

set_key()
screen_size = 50
effect_duration = 0.5
time_font_size = 200
color_over_time = {
    100: (0, 0, 255),
    99: (3, 0, 252), 
    98: (5, 0, 250), 
    97: (8, 0, 247), 
    96: (10, 0, 245),
    95: (13, 0, 242),
    94: (15, 0, 240),
    93: (18, 0, 237),
    92: (20, 0, 235),
    91: (23, 0, 232),
    90: (26, 0, 229),
    89: (28, 0, 227),
    88: (31, 0, 224),
    87: (33, 0, 222),
    86: (36, 0, 219),
    85: (38, 0, 217),
    84: (41, 0, 214),
    83: (43, 0, 212),
    82: (46, 0, 209),
    81: (48, 0, 207),
    80: (51, 0, 204),
    79: (54, 0, 201),
    78: (56, 0, 199),
    77: (59, 0, 196),
    76: (61, 0, 194),
    75: (64, 0, 191),
    74: (66, 0, 189),
    73: (69, 0, 186),
    72: (71, 0, 184),
    71: (74, 0, 181),
    70: (76, 0, 178),
    69: (79, 0, 176),
    68: (82, 0, 173),
    67: (84, 0, 171),
    66: (87, 0, 168),
    65: (89, 0, 166),
    64: (92, 0, 163),
    63: (94, 0, 161),
    62: (97, 0, 158),
    61: (99, 0, 156),
    60: (102, 0, 153),
    59: (105, 0, 150),
    58: (107, 0, 148),
    57: (110, 0, 145),
    56: (112, 0, 143),
    55: (115, 0, 140),
    54: (117, 0, 138),
    53: (120, 0, 135),
    52: (122, 0, 133),
    51: (125, 0, 130),
    50: (127, 0, 127),
    49: (130, 0, 125),
    48: (133, 0, 122),
    47: (135, 0, 120),
    46: (138, 0, 117),
    45: (140, 0, 115),
    44: (143, 0, 112),
    43: (145, 0, 110),
    42: (148, 0, 107),
    41: (150, 0, 105),
    40: (153, 0, 102),
    39: (156, 0, 99),
    38: (158, 0, 97),
    37: (161, 0, 94),
    36: (163, 0, 92),
    35: (166, 0, 89),
    34: (168, 0, 87),
    33: (171, 0, 84),
    32: (173, 0, 82),
    31: (176, 0, 79),
    30: (178, 0, 76),
    29: (181, 0, 74),
    28: (184, 0, 71),
    27: (186, 0, 69),
    26: (189, 0, 66),
    25: (191, 0, 64),
    24: (194, 0, 61),
    23: (196, 0, 59),
    22: (199, 0, 56),
    21: (201, 0, 54),
    20: (204, 0, 51),
    19: (207, 0, 48),
    18: (209, 0, 46),
    17: (212, 0, 43),
    16: (214, 0, 41),
    15: (217, 0, 38),
    14: (219, 0, 36),
    13: (222, 0, 33),
    12: (224, 0, 31),
    11: (227, 0, 28),
    10: (229, 0, 26),
    9: (232, 0, 23),
    8: (235, 0, 20),
    7: (237, 0, 18),
    6: (240, 0, 15),
    5: (242, 0, 13),
    4: (245, 0, 10),
    3: (247, 0, 8),
    2: (250, 0, 5),
    1: (252, 0, 3),
    0: (255, 0, 0),
    -1: (56, 56, 56)
}
    
# color_over_time = "random_white"
open_window(50)