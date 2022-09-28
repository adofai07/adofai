"""
HOTCLEAR is an TETR.IO AI made by SSHS crews
Copyright not reserved.
"""

def get_block(color):
    COLORS = [
        (0, 0, 0),
        (69, 67, 67),
        (195, 57, 64),
        (192, 105, 54),
        (191, 161, 53),
        (140, 188, 54),
        (55, 187, 138),
        (85, 65, 173),
        (173, 65, 163)
    ]

    min_diff = 1000
    min_diff_idx = 0

    for i in range(8):
        temp = sum(abs(COLORS[i][j] - color[j]) for j in range(3))

        if temp < min_diff:
            min_diff = temp
            min_diff_idx = i

    return " X0000000"[min_diff_idx]

def get_falling_block():
    global grid

    block_cnt = 0
    block_coord = []

    # first_block_coord
    FBC = None

    for i in range(22):
        for j in range(10):
            if grid[i][j] != " ":
                if block_cnt == 0:
                    FBC = (i, j)

                block_cnt += 1
                block_coord.append((i, j))
    
        if block_cnt >= 4: break
    
    if block_cnt == 4:
        for coord in block_coord:
            grid[coord[0]][coord[1]] = " "
            
        if (
            (FBC[0], FBC[1]+1) in block_coord and
            (FBC[0]+1, FBC[1]+1) in block_coord and
            (FBC[0]+1, FBC[1]+2) in block_coord
        ): return "Z"

        if (
            (FBC[0]+1, FBC[1]) in block_coord and
            (FBC[0]+1, FBC[1]-1) in block_coord and
            (FBC[0]+1, FBC[1]-2) in block_coord
        ): return "L"

        if (
            (FBC[0]+1, FBC[1]) in block_coord and
            (FBC[0], FBC[1]+1) in block_coord and
            (FBC[0]+1, FBC[1]+1) in block_coord
        ): return "O"

        if (
            (FBC[0]+1, FBC[1]) in block_coord and
            (FBC[0], FBC[1]+1) in block_coord and
            (FBC[0]+1, FBC[1]-1) in block_coord
        ): return "S"

        if (
            (FBC[0], FBC[1]+1) in block_coord and
            (FBC[0], FBC[1]+2) in block_coord and
            (FBC[0], FBC[1]+3) in block_coord
        ): return "I"

        if (
            (FBC[0]+1, FBC[1]) in block_coord and
            (FBC[0]+1, FBC[1]+1) in block_coord and
            (FBC[0]+1, FBC[1]+2) in block_coord
        ): return "J"

        if (
            (FBC[0]+1, FBC[1]-1) in block_coord and
            (FBC[0]+1, FBC[1]) in block_coord and
            (FBC[0]+1, FBC[1]+1) in block_coord
        ): return "T"

def get_floor(grid):
    floor = []

    for i in range(10):
        for j in range(23):
            if j == 22: break

            if grid[j][i] != " ":
                break
        
        floor.append(22 - j)
    
    return floor

def get_best_move(falling_block, floor, holded_, key_delay):
    cand = [[], [], [], []]

    if falling_block == "Z":
        offset = [3, 4, 3, 3]

        for i in range(8):
            if floor[i] - 1 == floor[i+1] == floor[i+2]:
                cand[0].append(i)

        for i in range(9):
            if floor[i] + 1 == floor[i+1]:
                cand[1].append(i)

    if falling_block == "L":
        offset = [3, 4, 3, 3]

        for i in range(8):
            if floor[i] == floor[i+1] == floor[i+2]:
                cand[0].append(i)
            
        for i in range(9):
            if floor[i] == floor[i+1]:
                cand[1].append(i)

        for i in range(8):
            if floor[i] + 1 == floor[i+1] == floor[i+2]:
                cand[2].append(i)

        for i in range(9):
            if floor[i] - 2 == floor[i+1]:
                cand[3].append(i)

    if falling_block == "O":
        offset = [4, 4, 4, 4]

        for i in range(9):
            if floor[i] == floor[i+1]:
                cand[0].append(i)

    if falling_block == "S":
        offset = [3, 4, 3, 3]

        for i in range(8):
            if floor[i] == floor[i+1] == floor[i+2] - 1:
                cand[0].append(i)

        for i in range(9):
            if floor[i] == floor[i+1] + 1:
                cand[1].append(i)

    if falling_block == "I":
        # Put it in the lowest spot
        offset = [3, 5, 3, 4]

        for i in range(10):
            if floor[i] == min(floor):
                cand[1].append(i)

    if falling_block == "J":
        offset = [3, 4, 3, 3]

        for i in range(8):
            if floor[i] == floor[i+1] == floor[i+2]:
                cand[0].append(i)

        for i in range(9):
            if floor[i] + 2 == floor[i+1]:
                cand[1].append(i)

        for i in range(8):
            if floor[i] == floor[i+1] == floor[i+2] + 1:
                cand[2].append(i)

        for i in range(9):
            if floor[i] == floor[i+1]:
                cand[3].append(i)

    if falling_block == "T":
        offset = [3, 4, 3, 3]

        for i in range(8):
            if floor[i] == floor[i+1] == floor[i+2]:
                cand[0].append(i)

        for i in range(9):
            if floor[i] + 1 ==  floor[i+1]:
                cand[1].append(i)

        for i in range(8):
            if floor[i] == floor[i+1] + 1 == floor[i+2]:
                cand[2].append(i)
        
        for i in range(9):
            if floor[i] == floor[i+1] + 1:
                cand[3].append(i)


    try: choice = random.randrange(0, sum(len(cand[i]) for i in range(4)))
    except:
        if not holded_:
            pyautogui.keyDown("h"); pyautogui.keyup("h"); return True
        
        if holded_:
            pyautogui.press("space"); return False

    for i in range(4):
        if choice < len(cand[i]):
            # return (i, cand[i][choice] - offset[i])

            pos = cand[i][choice] - offset[i]

            for _ in range(i):
                pyautogui.keyDown("up")
                pyautogui.keyUp("up")
                time.sleep(key_delay)

            if pos > 0:
                for _ in range(pos):
                    pyautogui.press("right")
                    time.sleep(key_delay)

            if pos < 0:
                for _ in range(-pos):
                    pyautogui.press("left")
                    time.sleep(key_delay)

            pyautogui.press("space")

            return False
        
        choice -= len(cand[i])


import pyautogui
import pyscreenshot
import win32com.client
import time
import random
import winsound

shell = win32com.client.Dispatch("WScript.Shell")

# 34 pixels per grid
LEFTUPPER = (790, 134)
RIGHTLOWER = (1130, 880)

time.sleep(2)
winsound.Beep(2000, 1000)

holded = False

while True:
    try:
        screen = pyscreenshot.grab(bbox = (*LEFTUPPER, *RIGHTLOWER))
        screen.save("C:/Themes/HOTCLEAR.png")


        grid = [[get_block(screen.getpixel((i, j))) for i in range(17, 340, 34)] for j in range(17, 748, 34)]
        falling_block = get_falling_block()

        if falling_block == None: continue

        floor = get_floor(grid)

        print(falling_block, floor)

        holded = get_best_move(falling_block, floor, holded, 0.04)

    except: ...