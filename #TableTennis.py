import pygame
import keyboard
from time import time, sleep
from math import *

def set_key():
    global key_was_pressed
    key_was_pressed = {chr(i) : 0 for i in range(65, 91)}
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
    key_was_pressed["left shift"] = 0
    key_was_pressed["right shift"] = 0

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

def rect(color, position, condition):
    pygame.draw.rect(screen, color, (screen_size*16*position[0], screen_size*9*position[1], screen_size*16*position[2], screen_size*9*position[3]))
    if condition: pygame.display.update()

def display(elapsed_time, p1_score, p2_score, p1_chance, condition):
    global goal, deuce

    screen.fill((0, 0, 0))
    blit("{:02.0f}:{:02.0f}:{:05.2f}".format(elapsed_time//3600, (elapsed_time%3600)//60, elapsed_time%60), 60, (0.5, 0.1), (255, 255, 255), False)
    blit("{:03d}".format(p1_score), 100, (0.2, 0.5), (255, 100, 100), False)
    blit("{:03d}".format(p2_score), 100, (0.8, 0.5), (100, 100, 255),False)
    blit("{:03d}".format(goal), 100, (0.88, 0.1), (100, 255, 100),False)
    blit("{:05.2f}%".format(p1_chance), 70, (0.2, 0.7), (255, 100, 100), False)
    blit("{:05.2f}%".format(100 - p1_chance), 70, (0.8, 0.7), (100, 100, 255), False)
    rect((100, 100, 255), (0, 0.9, 1, 0.05), False)
    if game_is_matchpoint(): blit("MATCHPOINT", 80, (0.5, 0.3), (100, 255, 100), False)
    if deuce: blit("DEUCE", 60, (0.15, 0.1), (100, 255, 100), False)
    rect((255, 100, 100), (0, 0.9, p1_chance/100, 0.05), (True if condition else False))

def game_is_matchpoint():
    global player1_score, player2_score, goal

    if (player1_score == goal - 1 or player2_score == goal - 1) and player1_score != goal and player2_score != goal: return True
    else: return False

def game_is_deuce():
    global player1_score, player2_score, goal, new_goal, deuce
    if player1_score == player2_score == goal - 1: deuce = 1; return True
    else: return False

def get_chance():
    global player1_score, player2_score, goal

    if player1_score+player2_score == 0: return
    if player1_score == goal and not player2_score == goal: return 100

    n = (goal**2 - player1_score - player2_score)//1
    p = (player1_score/(player1_score + player2_score) + n)/(2*n+1)
    

    chance = 0

    for k in range(goal - player2_score):
        try: chance += pow(p, goal - player1_score)*pow(1-p, k)*comb(goal - player1_score + k - 1, k)
        except: pass

    return chance*100

def startGame():
    global goal, key_was_pressed, player1_score, player2_score, goal, effect_duration, new_goal, screen_size, deuce
    
    while not keyboard.is_pressed("space"):
        if keyboard.is_pressed("left arrow") and not key_was_pressed["left arrow"]:
            key_was_pressed["left arrow"] = 1
            goal -= 1
        if keyboard.is_pressed("right arrow") and not key_was_pressed["right arrow"]:
            key_was_pressed["right arrow"] = 1
            goal += 1
        if keyboard.is_pressed("up arrow") and not key_was_pressed["up arrow"]:
            key_was_pressed["up arrow"] = 1
            goal += 1
        if keyboard.is_pressed("down arrow") and not key_was_pressed["down arrow"]:
            key_was_pressed["down arrow"] = 1
            goal -= 1

        if not keyboard.is_pressed("left arrow"):
            key_was_pressed["left arrow"] = 0
        if not keyboard.is_pressed("right arrow"):
            key_was_pressed["right arrow"] = 0
        if not keyboard.is_pressed("up arrow"):
            key_was_pressed["up arrow"] = 0
        if not keyboard.is_pressed("down arrow"):
            key_was_pressed["down arrow"] = 0
        
        screen.fill((0, 0, 0))
        blit("Goal : {:03d}".format(goal), 100, (0.5, 0.5), (255, 255, 255), False)
        blit("Press space to start", 70, (0.5, 0.7), (0, 255, 0), True)
        pygame.display.update()

    
    player1_score, player2_score = 0, 0
    elapsed_time = 0
    current_time = time()
    current_chance = 0
    matchpoint = 0
    deuce = 0

    while True:
        delay = time() - current_time
        current_time = time()
        elapsed_time += delay

        if keyboard.is_pressed("left shift") and not key_was_pressed["left shift"]:
            key_was_pressed["left shift"] = 1
            player1_score += 1
        if keyboard.is_pressed("right shift") and not key_was_pressed["right shift"]:
            key_was_pressed["right shift"] = 1
            player2_score += 1

        if not keyboard.is_pressed("left shift"):
            key_was_pressed["left shift"] = 0
        if not keyboard.is_pressed("right shift"):
            key_was_pressed["right shift"] = 0

        new_chance = get_chance() if player1_score+player2_score != 0 else 50
        if current_chance != new_chance:
            effect_start_time = time()
            d = new_chance - current_chance
            while time() - effect_start_time < effect_duration:
                x = time() - effect_start_time
                display(elapsed_time, player1_score, player2_score, current_chance + (d/effect_duration)*pow(effect_duration**7 - (abs(x - effect_duration))**7, 1/7), True)
            elapsed_time += effect_duration
        current_chance = new_chance

        if game_is_deuce(): goal += 1

        if max(player1_score, player2_score) == goal: open_window(500)                
        
        display(elapsed_time, player1_score, player2_score, new_chance, True)
        

goal = 11
screen_size = 50
effect_duration = 1.7
deuce = 0
set_key()
open_window(50)