import os
import pygame
import keyboard
import random
from time import time
from math import *
import copy
import sys

pygame.init()
Color = (0, 0, 0)
screen = pygame.display.set_mode([1200, 600])
done = False
clock = pygame.time.Clock()

def prevent_crash(enable_exit = True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if enable_exit == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

def blit(message, fontSize, coord, color, condition):
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    text = font.render(str(message), True, color)
    textRect = text.get_rect()
    textRect.center = (coord[0], coord[1])
    screen.blit(text, textRect)
    if condition:
        pygame.display.update()

def lobby():
    global score

    screen.fill((0, 0, 0))
    blit("score: {:.0f}".format(score), 60, (600, 300), (111, 111, 111), False)
    blit("Press enter to start", 60, (600, 200), (111, 111, 111), True)
    while True:
        prevent_crash()
        if keyboard.is_pressed("enter"):
            while keyboard.is_pressed("enter"):
                pass
            startGame()

def GameIsOver():
    global character_coord, character_radius, circle_obstacle, meteor_obstacle, turret_obstacle, bullet_obstacle
    if not 50 <= character_coord[0] <= 1150: return True
    if not 50 <= character_coord[1] <= 550: return True
    for i in range(len(circle_obstacle)):
        if (character_coord[0] - circle_obstacle[i][2][0])**2 + (character_coord[1] - circle_obstacle[i][2][1])**2 <= (2 * character_radius)**2: return True
    for i in range(len(meteor_obstacle)):
        if meteor_obstacle[i][3] == 1 and (character_coord[0] - meteor_obstacle[i][0][0])**2 + (character_coord[1] - meteor_obstacle[i][0][1])**2 <= (meteor_obstacle[i][1] + character_radius)**2: return True
    for i in range(len(turret_obstacle)):
        if turret_obstacle[i][2] > 5 and (character_coord[0] - turret_obstacle[i][0][0])**2 + (character_coord[1] - turret_obstacle[i][0][1])**2 <= (turret_obstacle[i][1] + character_radius)**2: return True
    for i in range(len(bullet_obstacle)):
        if (character_coord[0] - bullet_obstacle[i][0][0])**2 + (character_coord[1] - bullet_obstacle[i][0][1])**2 <= (bullet_obstacle[i][1] + character_radius)**2: return True
    return False

def startGame():
    global score, character_coord, character_radius, circle_obstacle, meteor_obstacle, turret_obstacle, bullet_obstacle

    score = 0
    tick = 0
    level = 0
    current_time = time()
    game_start_time = time()
    dash_cooltime = 0
    invincible = 0
    shift_debuff = 0
    character_coord = [600, 300]
    character_radius = 10
    level_color = [[0, 145, 255], [0, 255, 55], [191, 209, 29], [255, 128, 0], [255, 0, 0]]
    keyPressed = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0,
        "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
    }
    difficulty = 0
    circle_obstacle = [] # [starting direction, speed, current position]
    meteor_obstacle = [] # [position, radius, time left, dead]
    turret_obstacle = [] # [position, radius, age, ammo, facing direction, turbo]
    bullet_obstacle = [] # [position, radius, speed]


    while True:
        prevent_crash()
        
        tick += 1
        score += level * 0.4 + 0.1
        difficulty += 1
        elapsed_time = time() - game_start_time
        level = int(elapsed_time//25) + 2
        delay = time() - current_time
        current_time = time()
        dash_cooltime = max(dash_cooltime - delay, 0)

        screen.fill((0, 0, 0))
        for i in range(97, 123):
            if keyboard.is_pressed(chr(i)):
                keyPressed[chr(i)] = 1
            if keyPressed[chr(i)] and not keyboard.is_pressed(chr(i)):
                keyPressed[chr(i)] = 0

        character_speed = 0.55
        character_radius = 10

        if keyboard.is_pressed("shift"):
            character_speed = 0.13
            character_radius = 5
            shift_debuff += 0.003
            score -= shift_debuff
        if keyboard.is_pressed("enter"):
            if dash_cooltime == 0 or dash_cooltime >= 29.5:
                character_speed = 2
            if dash_cooltime == 0:
                dash_cooltime = 30

        invincible = 0
        if dash_cooltime >= 28: invincible = 1
        if 0 <= elapsed_time%25 <= 3: invincible = 1
        if keyboard.is_pressed("shift"): invincible = 1

        if keyPressed["w"]:
            character_coord[1] -= character_speed * delay * 1200
        if keyPressed["a"]:
            character_coord[0] -= character_speed * delay * 1200
        if keyPressed["s"]:
            character_coord[1] += character_speed * delay * 1200
        if keyPressed["d"]:
            character_coord[0] += character_speed * delay * 1200


        if level <= 1: # spawn circle obstacles
            if random.randrange(1, 300) == 1:
                a = random.randrange(1, 7)
                if a in [1]:
                    b =  random.randrange(50-character_radius, 551-character_radius)
                    circle_obstacle.append(["left", random.randrange(8, 13)/10, [50, b]])
                elif a in [2]:
                    b =  random.randrange(50-character_radius, 551-character_radius)
                    circle_obstacle.append(["right", random.randrange(8, 13)/10, [1150, b]])
                if a in [3, 4]:
                    b = random.randrange(50-character_radius, 1151-character_radius)
                    circle_obstacle.append(["up", random.randrange(6, 15)/20, [b, 50]])
                elif a in [5, 6]:
                    b = random.randrange(50-character_radius, 1151-character_radius)
                    circle_obstacle.append(["down", random.randrange(6, 15)/20, [b, 550]])

        i = -1
        while True: # move circle obstacles
            if len(circle_obstacle) == 0: break
            i += 1
            if i == len(circle_obstacle): break

            if circle_obstacle[i][0] == "left":
                if circle_obstacle[i][2][0] >= 1150:
                    circle_obstacle.remove(circle_obstacle[i])
                    score += 120
                    i -= 1; continue
                else:
                    circle_obstacle[i][2][0] += circle_obstacle[i][1] * delay * 700
            if circle_obstacle[i][0] == "right":
                if circle_obstacle[i][2][0] <= 50:
                    circle_obstacle.remove(circle_obstacle[i])
                    score += 120
                    i -= 1; continue
                else:
                    circle_obstacle[i][2][0] -= circle_obstacle[i][1] * delay * 700
            if circle_obstacle[i][0] == "up":
                if circle_obstacle[i][2][1] >= 550:
                    circle_obstacle.remove(circle_obstacle[i])
                    score += 120
                    i -= 1; continue
                else:
                    circle_obstacle[i][2][1] += circle_obstacle[i][1] * delay * 700
            if circle_obstacle[i][0] == "down":
                if circle_obstacle[i][2][1] <= 50:
                    circle_obstacle.remove(circle_obstacle[i])
                    score += 120
                    i -= 1; continue
                else:
                    circle_obstacle[i][2][1] -= circle_obstacle[i][1] * delay * 700

        if level >= 1: # spawn meteor obstacles
            if random.randrange(1, 500) == 1 and len(meteor_obstacle) <= 3:
                meteor_obstacle.append([(random.randrange(100, 1100), random.randrange(100, 500)), random.randrange(45, 51), 5, 0])
            if random.randrange(1, 5000) == 1 and len(meteor_obstacle) <= 3:
                meteor_obstacle.append([(random.randrange(200, 1000), random.randrange(200, 400)), random.randrange(145, 151), 5, 0])

        i = -1
        while True: # move meteor obstacles
            if len(meteor_obstacle) == 0: break
            i += 1
            if i >= len(meteor_obstacle): break

            if meteor_obstacle[i][3] == 80:
                score += meteor_obstacle[i][1] * 7
                meteor_obstacle.remove(meteor_obstacle[i])
            elif meteor_obstacle[i][2] <= 0:
                meteor_obstacle[i][3] += 1
            else:
                meteor_obstacle[i][2] -= delay

        if level >= 2: # spawn turret obstacles
            a, b = random.randrange(300, 901), random.randrange(300, 301)
            while True:
                a, b = random.randrange(300, 901), random.randrange(300, 301)
                if not 300 <= a <= 900 and not 150 <= b <= 450: break

            if random.randrange(1, 1200) == 1 and len(turret_obstacle) <= 1:
                if random.randrange(1, 21) != 1:
                    turret_obstacle.append([[a, b], 30, 0, random.randrange(0, 21) + 50, random.uniform(0, 2*pi), 0])
                else:
                    turret_obstacle.append([[a, b], 30, 0, 500, random.uniform(0, 2*pi), 1])

        i = -1
        while True: # move turret obstacles
            if len(turret_obstacle) == 0: break
            i += 1
            if i >= len(turret_obstacle): break

            turret_obstacle[i][2] += delay
            if (turret_obstacle[i][2] > 5 and tick % 10 == 0 and turret_obstacle[i][3] <= 100) or (turret_obstacle[i][2] > 5 and turret_obstacle[i][3] >= 100):
                bullet_obstacle.append([copy.deepcopy(turret_obstacle[i][0]), character_radius, (cos(turret_obstacle[i][4]), sin(turret_obstacle[i][4]))])
                turret_obstacle[i][3] -= 1
                if not turret_obstacle[i][5]:
                    score += level * 20
                    turret_obstacle[i][4] += random.uniform(0, pi)
                else:
                    score += level * 0.1
                    turret_obstacle[i][4] += pi/1.5 + pi/5000
            if turret_obstacle[i][3] == 0:
                turret_obstacle.remove(turret_obstacle[i])
        
        i = -1
        while True: # move bullet obstacles
            if len(bullet_obstacle) == 0: break
            i += 1
            if i >= len(bullet_obstacle): break

            bullet_obstacle[i][0][0] += bullet_obstacle[i][2][0] * delay * 250
            bullet_obstacle[i][0][1] += bullet_obstacle[i][2][1] * delay * 250

            if not (50 <= bullet_obstacle[i][0][0] <= 1150 and 50 <= bullet_obstacle[i][0][1] <= 550): bullet_obstacle.remove(bullet_obstacle[i])


        if GameIsOver() and not invincible: lobby()

        blit("{:.0f}".format(score), 100, (600, 450), (30, 30, 30), False)
        blit(("{:.1f}".format(dash_cooltime) if dash_cooltime != 0 else "DASH"), 100, (600, 150), (30, 30, 30), False)
        blit("SHEILD", 100, (600, 250), ((30, 30, 30) if invincible == 0 else (60, 60, 60)), False)
        # blit("{:.02d} : {:.02d} : {:.02d}".format(elapsed_time//3600, (elapsed_time%3600)//60, (elapsed_time%60)//1), 100, (600, 450), (30, 30, 30), False)

        for i in range(len(circle_obstacle)):
            pygame.draw.circle(screen, (0, 175, 255), circle_obstacle[i][2], character_radius, 4)

        for i in range(len(meteor_obstacle)):
            if meteor_obstacle[i][3] == 0:
                pygame.draw.circle(screen, (0, 255, 55), meteor_obstacle[i][0], meteor_obstacle[i][1], 4)
                blit("{:.1f}".format(meteor_obstacle[i][2]), meteor_obstacle[i][1], meteor_obstacle[i][0], (0, 255, 55), False)
            else:
                pygame.draw.circle(screen, (0, 255 - meteor_obstacle[i][3]*3, int(90 - meteor_obstacle[i][3])), meteor_obstacle[i][0], meteor_obstacle[i][1])

        for i in range(len(bullet_obstacle)):
            pygame.draw.circle(screen, (191, 209, 29), bullet_obstacle[i][0], character_radius, 4)

        for i in range(len(turret_obstacle)):
            if turret_obstacle[i][2] <= 5:
                pygame.draw.circle(screen, (191, 209, 29), turret_obstacle[i][0], turret_obstacle[i][1], 4)
                blit("{:.1f}".format(5 - turret_obstacle[i][2]), turret_obstacle[i][1], turret_obstacle[i][0], [191, 209, 29], False)
            else:
                pygame.draw.circle(screen, (191, 209, 29), turret_obstacle[i][0], turret_obstacle[i][1])
                blit("{:.0f}".format(turret_obstacle[i][3]), turret_obstacle[i][1]-5, turret_obstacle[i][0], [0, 0, 0], False)

        pygame.draw.rect(screen, (level_color[min(4, level)] if invincible == 0 else (50, 50, 50)), (50, 50, 1100, 500), 10, 20)
        pygame.draw.circle(screen, (255, 255, 255), character_coord, character_radius, 4)
        pygame.display.update()

    
score = 0
lobby()