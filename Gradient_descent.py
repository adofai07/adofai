import sys
import pygame
import pyautogui
import decimal

D = decimal.Decimal
decimal.getcontext().prec = 250

pygame.init()
screen_size = pyautogui.size()
screen = pygame.display.set_mode(screen_size)
pygame.display.flip()

def prevent_crash(enable_exit = True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if enable_exit == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

def blit(message1, fontSize, coord, color, condition = False, mode = "center", Font = "C:/Pygame_fonts/SourceCodePro-VariableFont_wght.ttf"):
    font = pygame.font.Font(Font, fontSize)
    text = font.render(str(message1), True, color)
    textRect = text.get_rect()
    exec(f"textRect.{mode} = (coord[0], coord[1])")
    screen.blit(text, textRect)
    if condition: pygame.display.update()

def f(x):
    return x ** 3 + 3 * x - 5

init = D(0)
GRAD = D(10)
goal = D("31.0000000000000000000001")

UPDATE = 1

grad = GRAD

for i in range(1, 100_000_000):
    screen.fill((0, 0, 0))
    prevent_crash()

    if f(init) > goal: init -= grad
    
    elif f(init) < goal: init += grad

    grad *= D("0.97")

    # sys.stdout.write(f"{init}\r")
    if i%UPDATE == 0:
        
        blit(f"STEP = {i}", 120, (0, 300), (52, 52, 52), False, "midleft")
        blit("DELTA = {:.120f}".format(grad), 25, (0, 420), (123, 123, 123), False, "midleft")
        blit("VALUE = {:+}".format(init), 25, (0, 540), (255, 255, 255), True, "midleft")

    if grad <= 10 ** -120: break

while True:
    prevent_crash()
