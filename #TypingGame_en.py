from math import *
from time import time
import os
import nltk
nltk.download("words")

import keyboard
import pygame
from nltk.corpus import words
import random


def blit(message, fontSize, coord, color, condition):
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    text = font.render(str(message), True, color)
    textRect = text.get_rect()
    textRect.center = (coord[0], coord[1])
    screen.blit(text, textRect)
    if condition:
        pygame.display.update()

def inputIsCorrect():
    global mission, currentInput
    good = 1
    for i in range(min(len(currentInput), len(mission[0]))):
        if currentInput[i] != mission[0][i]: good = 0
    if currentInput == "-": good = 1
    return good

def startGame():
    global dictionary, timeLimit, bonusTime, score, kps, accuracy, mission, currentInput
    keyPressed = [0 for _ in range(27)] #a to z, backspace = 26

    while True:
        timeLeft = timeLimit
        score = 0
        mission = []
        currentInput = ""
        scoreTime = time()
        gameOver = 0
        good = 1
        gameStarted = 0
        gameStartTime = time()
        typedKeys = 0
        correctlyTypedKeys = 0
        accuracy = 0

        while True:
            for _ in range(6 - (len(mission))):
                mission.append(dictionary[random.randrange(0, len(dictionary))])

            if not gameStarted:
                gameStartTime = time()
            else:
                timeLeft -= time() - currentTime
            
            currentTime = time()

            if timeLeft <= 0:
                gameOver = 1

            if currentInput == "":
                currentInput = "-"

            good = inputIsCorrect()

            try: kps = typedKeys/(time() - gameStartTime)
            except: kps = 0

            if gameOver: break

            for word in range(97, 123):
                if keyboard.is_pressed(chr(word)) and not keyPressed[word - 97]:
                    gameStarted = 1
                    typedKeys += 1
                    if currentInput == "-" and chr(word) == mission[0][0]: correctlyTypedKeys += 1
                    elif len(currentInput) < len(mission[0]) and chr(word) == mission[0][len(currentInput)]: correctlyTypedKeys += 1
                    if currentInput == "-":
                        currentInput = ""
                    keyPressed[word - 97] = 1
                    currentInput += chr(word)
                if not keyboard.is_pressed(chr(word)):
                    keyPressed[word - 97] = 0
            if keyboard.is_pressed("backspace") and not keyPressed[26]:
                keyPressed[26] = 1
                currentInput  = currentInput[:len(currentInput)-1]
            if not keyboard.is_pressed("backspace"):
                keyPressed[26] = 0
            if keyboard.is_pressed("enter"):
                currentInput = ""

            if currentInput == mission[0]:
                score += (((len(mission[0])**2)*(30/(time() - scoreTime)))**2)/10000
                mission.remove(mission[0])
                currentInput = ""
                timeLeft += bonusTime
                scoreTime = time()
                good = 1

            try: accuracy = (correctlyTypedKeys/typedKeys)*100
            except: pass


            screen.fill((0, 0, 0))
            blit(currentInput, 60, (800, 540), ((0, 255, 0) if good == 1 else (255, 0, 0)), False)
            blit(mission[0], 60, (800, 450), (255, 255, 255), False)
            for i in range(1, len(mission)):
                blit(mission[i], 45 - 7*(i-1), (800, 450 - i*80), (155, 155, 155), False)
            blit("{:.2f}".format(accuracy) + "%", 55, (240, 480), (255, 127, 0), False)
            blit( "{:.0f}".format(kps*60) + "/M", 55, (240, 560), (0, 127, 255), False)
            blit(mission[0], 60, (800, 450), (255, 255, 255), False)
            blit("SCORE ", 90, (240, 100), (255, 255, 255), False)
            blit("{:.0f}".format(score), 55, (240, 180), (255, 255, 0), False)
            blit("TIME", 90, (240, 300), (255, 255, 255), False)
            blit("0"*max(0, 3-len(str(int(timeLeft)))) + str(int(timeLeft)), 70, (200, 380), (0, 0, 255), False)
            blit(str(timeLeft - timeLeft//1)[2:5] if len(str(timeLeft - timeLeft//1)[2:5]) >= 3 else "000", 40, (305, 390), (255, 0, 255), True)

        
        if gameOver: break
            
def ready():
    global score, kps
    while True:
        screen.fill((0, 0, 0))
        blit("Score : " + "{:.0f}".format(score), 50, (600, 200), (255, 255, 255), False)
        blit("KPM : " + "{:.2f}".format(kps*60), 50, (600, 300), (255, 255, 255), False)
        blit("Accuracy : " + "{:.2f}".format(accuracy) + "%", 50, (600, 400), (255, 255, 255), False)
        blit("Effective KPM : " + "{:.2f}".format(kps*accuracy*0.6), 50, (600, 500), (255, 255, 255), False)
        blit("Press enter to start", 50, (600, 80), (255, 255, 255), True)
        if keyboard.is_pressed("enter"):
            startGame()

pygame.init()
Color = (0, 0, 0)
screen = pygame.display.set_mode([1200, 600])
done = False
clock = pygame.time.Clock()

dictionary = list(words.words())
for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].lower()
score = 0

timeLimit = 30
bonusTime = 1
kps = 0
accuracy = 0

ready()