import sys
import time

import keyboard
import pyautogui
import pygame

pygame.init()
screen_size = pyautogui.size()
screen = pygame.display.set_mode(screen_size)
pygame.display.flip()

def prevent_crash(enable_exit = True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if enable_exit:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

def blit(message1, fontSize, coord, color, condition = False, mode = "center", Font = "C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf"):
    font = pygame.font.Font(Font, fontSize)
    text = font.render(str(message1), True, color)
    textRect = text.get_rect()
    exec(F"textRect.{mode} = (coord[0], coord[1])")
    screen.blit(text, textRect)
    if condition: pygame.display.update()

def MainMenu():
    screen.fill((0, 0, 0))

    MAX_STAGES = 5

    for i in range(1, MAX_STAGES+1):
        blit(i, 120, (150 * i + 100, 500), (255, 255, 255), False)
    
    pygame.display.update()

    STAGE = 0

    while True:
        prevent_crash()

        for i in range(1, MAX_STAGES+1):
            if keyboard.is_pressed(str(i)):
                STAGE = i

        if STAGE != 0: break

    for i in range(256):
        prevent_crash()

        screen.fill((i, i, i))

        for i in range(1, MAX_STAGES+1):
            blit(i, 120, (150 * i + 100, 500), (255, 255, 255), False)
        
        pygame.display.update()

        time.sleep(0.004)
    
    Stage(STAGE)
    

def Stage(integer):
    screen.fill((0, 0, 0))

    key_was_pressed = {
        i: False for i in range(10)
    }

    if integer == 1:
        OUTPUT = 17
        START = "a = 5"
        END = "print(a)"
        EVAL = "LOCALS['a']"
        LINES = 2
        COMMANDS = [
            "pass",
            "a += 2",
            "a *= 3"
        ]
        CODES = []

    if integer == 2:
        OUTPUT = 11
        START = "a = 1; b = 1"
        END = "print(a + b)"
        EVAL = "LOCALS['a'] + LOCALS['b']"
        LINES = 6
        COMMANDS = [
            "pass",
            "a += b",
            "b += a"
        ]
        CODES = []

    if integer == 3:
        OUTPUT = 185
        START = "a = 0; add = 2"
        END = "print(a)"
        EVAL = "LOCALS['a']"
        LINES = 7
        COMMANDS = [
            "pass",
            "a //= 2",
            "for i in range(10):",
            "   add += i",
            "a += i",
            "   a += i",
            "a += add",
            "   a += add"
        ]
        CODES = []

    if integer == 4:
        OUTPUT = "010"
        START = "a = '10'"
        END = "print(a)"
        EVAL = "LOCALS['a']"
        LINES = 4
        COMMANDS = [
            "pass",
            "a = ''.join(a)",
            "a = reversed(a)",
            "a += a",
            "a = a[:-1]"
        ]
        CODES = []

    if integer == 5:
        OUTPUT = "5 1"
        START = "a = 0; b = 1"
        END = "print(a, b)"
        EVAL = "str(LOCALS['a']) + ' ' + str(LOCALS['b'])"
        LINES = 14
        COMMANDS = [
            "pass",
            "a += b",
            "a += 1; b -= a",
            "a += 5; b += 1",
            "a //= 2; a -= 3",
            "a *= b",
            "a //= b",
            "a += 1; b += 3"
        ]
        CODES = []
     
    blit("Output", 120, (0, 0), (255, 255, 255), False, "topleft")
    blit(OUTPUT, 120, (0, 120), (0, 120, 255), True, "topleft")

    for i in range(0, 450):
        for j in range(280, 290):
            screen.set_at((i, j), (255, 255, 0))

    for i in range(len(COMMANDS)):
        blit(i, 60, (0, 300 + 75 * i), (255, 70, 70), False, "topleft")
        blit(COMMANDS[i], 60, (130, 300 + 75 * i), (255, 255, 255), False, "topleft")

    for i in range(LINES + 2):
        if i == 0: blit(START, 36, (1150, 60 * i + 60), (255, 255, 255), False, "topleft")
        elif i == LINES + 1: blit(END, 36, (1150, 60 * i + 60), (255, 255, 255), False, "topleft")
        else: blit("", 36, (1150, 60 * i + 60), (255, 255, 255), False, "topleft")

        blit(i+1, 36, (1100, 60 * i + 60), (123, 123, 123), False, "topright")

    for i in range(1130, 1137):
        for j in range(60, 60 * (LINES + 2) + 60):
            screen.set_at((i, j), (70, 255, 70))
            

    pygame.display.update()

    while True:
        prevent_crash()

        for i in range(len(COMMANDS)):
            if keyboard.is_pressed(str(i)) and not key_was_pressed[i]:
                CODES.append(COMMANDS[i])
                blit(COMMANDS[i], 36, (1150, 60 * len(CODES) + 60), (150, 255, 150), True, "topleft")
                if len(CODES) >= LINES: break
            
            if keyboard.is_pressed(str(i)): key_was_pressed[i] = True
            else: key_was_pressed[i] = False
        
        if len(CODES) >= LINES: break
    
    try:
        code = compile("\n".join([START] + CODES), "<string>", "exec")
        LOCALS = {}
        exec(code, LOCALS)
    except:
        blit("ERROR", 120, (550, 0), (255, 70, 70), True, "topleft")
        time.sleep(1.7)
        Stage(integer)

    blit(eval(EVAL), 120, (550, 0), ((70, 255, 70) if eval(EVAL) == OUTPUT else (255, 70, 70)), True, "topleft")

    time.sleep(1.7)

    if eval(EVAL) == OUTPUT: MainMenu()
    else: Stage(integer)

MainMenu()
