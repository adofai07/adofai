import os
import winsound
from math import *
from time import sleep, time
import inflect; inflect_engine = inflect.engine()
import keyboard
import pygame

def reset_screen():
    global screen_color
    screen.fill((screen_color[0], screen_color[1], screen_color[2]))

def draw_rainbow():
    fill_character = "|"
    pattern_height = 100
    pattern_x = 0
    pattern_y = 500

    font = pygame.font.Font('freesansbold.ttf', 120) 
    text = font.render("Chess Timer", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (600, 150)
    screen.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 20) 
    text = font.render("v.14.1", True, (100, 100, 100))
    textRect = text.get_rect()
    textRect.center = (900, 200)
    screen.blit(text, textRect)
    pygame.display.update()

    for i in range(0, 256):
        font = pygame.font.Font('freesansbold.ttf', pattern_height) 
        text = font.render(fill_character, True, (255, i, 0))
        textRect = text.get_rect()
        textRect.center = (pattern_x + (200/256)*i, pattern_y)
        screen.blit(text, textRect)
    pygame.display.update()
    for i in range(0, 256):
        font = pygame.font.Font('freesansbold.ttf', pattern_height) 
        text = font.render(fill_character, True, (255-i, 255, 0))
        textRect = text.get_rect()
        textRect.center = (pattern_x + 200 + (200/256)*i, pattern_y)
        screen.blit(text, textRect)
    pygame.display.update()
    for i in range(0, 256):
        font = pygame.font.Font('freesansbold.ttf', pattern_height) 
        text = font.render(fill_character, True, (0, 255, i))
        textRect = text.get_rect()
        textRect.center = (pattern_x + 400 + (200/256)*i, pattern_y)
        screen.blit(text, textRect)
    pygame.display.update()
    for i in range(0, 256):
        font = pygame.font.Font('freesansbold.ttf', pattern_height) 
        text = font.render(fill_character, True, (0, 255-i, 255))
        textRect = text.get_rect()
        textRect.center = (pattern_x + 600 + (200/256)*i, pattern_y)
        screen.blit(text, textRect)
    pygame.display.update()
    for i in range(0, 256):
        font = pygame.font.Font('freesansbold.ttf', pattern_height) 
        text = font.render(fill_character, True, (i, 0, 255))
        textRect = text.get_rect()
        textRect.center = (pattern_x + 800 + (200/256)*i, pattern_y)
        screen.blit(text, textRect)
    pygame.display.update()
    for i in range(0, 256):
        font = pygame.font.Font('freesansbold.ttf', pattern_height) 
        text = font.render(fill_character, True, (255, 0, 255-i))
        textRect = text.get_rect()
        textRect.center = (pattern_x + 1000 + (200/256)*i, pattern_y)
        screen.blit(text, textRect)
    pygame.display.update()
    
    text = font.render("Press enter to start", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (600, 510)
    screen.blit(text, textRect)
    pygame.display.update()

    while not keyboard.is_pressed("enter"):
        pass

pygame.init()
Color = (0, 0, 0)
padWidth, padHeight = 1200, 600
screen = pygame.display.set_mode((padWidth, padHeight))
done = False
clock = pygame.time.Clock()
clock.tick_busy_loop(144)

time_digits = 0
turn_sound = [1000, 0]
end_sound = [1200, 0]
ready_time = 0
resume_time = 0
base, add = 3, 2
fontSize_ready = 70
fontSize_bignumber = 120
fontSize_smallnumber = 60
fontSize_inning = 84
fontSize_pause = 40
fontSize_fps = 60
fontSize_settings = 45
turn_effect = 48
blink_effect = True
display_fps = True
show_end_message = False
clock_start_turn = False
display_time = ["minute and second", "second", "percentage"][0]
game_mode_color = [60, 60, 60]
ready_text_color = [255, 255, 255]
number_up_color = [[0, 175, 255]]
# number_up_color = [[0, 0, 255], [255, 0, 0]]
number_down_color = [69, 40, 40]
danger_color1 = [0, 255, 132]
danger_color2 = [255, 215, 13]
danger_color3 = [255, 61, 61]
end_color = [70, 70, 70]
inning_color = [60, 60, 60]
pause_color = [255, 255, 255]
fps_color = [110, 110, 110]
screen_color = [0, 0, 0]
possible_base_times = [1/4, 1/2, 3/4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180]
possible_add_times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180]


fps_log = []

draw_rainbow()

for round in range(1, 10**100):
    
    if base == 0: base = 1/60
    black, white = float(base*60), float(base*60)
    turn = -1
    inning = 1
    game_over = 0
    white_is_pressing = 0
    black_is_pressing = 0
    left_arrow_is_pressing = 0
    right_arrow_is_pressing = 0
    up_arrow_is_pressing = 0
    down_arrow_is_pressing = 0
    space_is_pressing = 0
    s_is_pressing = 0

    coordx_black, coordy_black_up, coordy_black_down = 900, 350, 420
    coordx_white, coordy_white_up, coordy_white_down = 300, 350, 420
    coordx_inning, coordy_inning = 600, 300


    while True:
        reset_screen()
        font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
        text = font.render("Press Lshift or Rshift to start", True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
        textRect = text.get_rect()
        textRect.center = (padWidth/2, padHeight/2-70)
        screen.blit(text, textRect)
        font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
        text = font.render("Press space to adjust time", True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
        textRect = text.get_rect()
        textRect.center = (padWidth/2, padHeight/2)
        font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
        screen.blit(text, textRect)
        text = font.render("Press s to change settings", True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
        textRect = text.get_rect()
        textRect.center = (padWidth/2, padHeight/2+70)
        screen.blit(text, textRect)
        pygame.display.update()
        if keyboard.is_pressed("left shift"):
            first_turn = "right shift"
            left_is_pressing = 1
            break
        if keyboard.is_pressed("right shift"):
            first_turn = "left shift"
            right_is_pressing = 1
            break
        if keyboard.is_pressed("s") and not s_is_pressing:
            s_is_pressing = 1
            up_arrow_is_pressing = 0
            down_arrow_is_pressing = 0
            left_arrow_is_pressing = 0
            right_arrow_is_pressing = 0
            selected_item = 1
            while True:
                if keyboard.is_pressed("up arrow") and not up_arrow_is_pressing:
                    if selected_item != 1: selected_item -= 1
                    up_arrow_is_pressing = 1
                if keyboard.is_pressed("down arrow") and not down_arrow_is_pressing:
                    if selected_item != 7: selected_item += 1
                    down_arrow_is_pressing = 1
                if keyboard.is_pressed("left arrow") and selected_item == 1 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    blink_effect = [True, False][([True, False].index(blink_effect)-1)%2]
                if keyboard.is_pressed("right arrow") and selected_item == 1 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    blink_effect = [True, False][([True, False].index(blink_effect)+1)%2]
                if keyboard.is_pressed("left arrow") and selected_item == 2 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    display_fps = [True, False][([True, False].index(display_fps)-1)%2]
                if keyboard.is_pressed("right arrow") and selected_item == 2 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    display_fps = [True, False][([True, False].index(display_fps)+1)%2]
                if keyboard.is_pressed("left arrow") and selected_item == 3 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    show_end_message = [True, False][([True, False].index(show_end_message)-1)%2]
                if keyboard.is_pressed("right arrow") and selected_item == 3 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    show_end_message = [True, False][([True, False].index(show_end_message)+1)%2]
                if keyboard.is_pressed("left arrow") and selected_item == 4 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    clock_start_turn = [True, False][([True, False].index(clock_start_turn)-1)%2]
                if keyboard.is_pressed("right arrow") and selected_item == 4 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    clock_start_turn = [True, False][([True, False].index(clock_start_turn)+1)%2]
                if keyboard.is_pressed("left arrow") and selected_item == 5 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    display_time = ["minute and second", "second", "percentage"][(["minute and second", "second", "percentage"].index(display_time)-1)%3]
                if keyboard.is_pressed("right arrow") and selected_item == 5 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    display_time = ["minute and second", "second", "percentage"][(["minute and second", "second", "percentage"].index(display_time)+1)%3]
                if keyboard.is_pressed("left arrow") and selected_item == 6 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    ready_time = [0, 1, 2, 3, 4, 5][([0, 1, 2, 3, 4, 5].index(ready_time)-1)%6]
                if keyboard.is_pressed("right arrow") and selected_item == 6 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    ready_time = [0, 1, 2, 3, 4, 5][([0, 1, 2, 3, 4, 5].index(ready_time)+1)%6]
                if keyboard.is_pressed("left arrow") and selected_item == 7 and not left_arrow_is_pressing:
                    left_arrow_is_pressing = 1
                    time_digits = [0, 1, 2, 3, 4, 5][([0, 1, 2, 3, 4, 5].index(time_digits)-1)%6]
                if keyboard.is_pressed("right arrow") and selected_item == 7 and not right_arrow_is_pressing:
                    right_arrow_is_pressing = 1
                    time_digits = [0, 1, 2, 3, 4, 5][([0, 1, 2, 3, 4, 5].index(time_digits)+1)%6]


                if not keyboard.is_pressed("up arrow"):
                    up_arrow_is_pressing = 0
                if not keyboard.is_pressed("down arrow"):
                    down_arrow_is_pressing = 0
                if not keyboard.is_pressed("left arrow"):
                    left_arrow_is_pressing = 0
                if not keyboard.is_pressed("right arrow"):
                    right_arrow_is_pressing = 0
                

                reset_screen()
                font = pygame.font.Font('freesansbold.ttf', 70) 
                text = font.render("Press s again to return", True, (100, 100, 100))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 40)
                screen.blit(text, textRect)

                font = pygame.font.Font('freesansbold.ttf', fontSize_settings) 
                text = font.render("Blink effect : " + ("true" if blink_effect else "false"), True, ((255, 255, 255) if selected_item == 1 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 150)
                screen.blit(text, textRect)

                text = font.render("Display FPS : " + ("true" if display_fps else "false"), True, ((255, 255, 255) if selected_item == 2 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 220)
                screen.blit(text, textRect)

                text = font.render("Show message at game over : " + ("true" if show_end_message else "false"), True, ((255, 255, 255) if selected_item == 3 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 290)
                screen.blit(text, textRect)

                text = font.render("Stop clock at first turn : " + ("true" if clock_start_turn else "false"), True, ((255, 255, 255) if selected_item == 4 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 360)
                screen.blit(text, textRect)

                text = font.render("Time format : " + str(display_time), True, ((255, 255, 255) if selected_item == 5 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 430)
                screen.blit(text, textRect)

                text = font.render("Time to get ready : " + str(ready_time), True, ((255, 255, 255) if selected_item == 6 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 500)
                screen.blit(text, textRect)

                text = font.render("Digits under decimal point : " + str(time_digits), True, ((255, 255, 255) if selected_item == 7 else (100, 100, 100)))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 570)
                screen.blit(text, textRect)


                if not keyboard.is_pressed("s"):
                    s_is_pressing = 0

                if keyboard.is_pressed("s") and not s_is_pressing:
                    s_is_pressing = 1
                    break

                pygame.display.update()
        if keyboard.is_pressed("space") and not space_is_pressing:
            space_is_pressing = 1
            reset_screen()
            selected_item = -1
            while True:
                if (keyboard.is_pressed("right arrow") or keyboard.is_pressed("d")) and selected_item == -1 and not right_arrow_is_pressing:
                    reset_screen()
                    selected_item *= -1
                    left_arrow_is_pressing = 1
                if (keyboard.is_pressed("left arrow") or keyboard.is_pressed("a")) and selected_item == 1 and not left_arrow_is_pressing:
                    reset_screen()
                    selected_item *= -1
                    right_arrow_is_pressing = 1
                if (keyboard.is_pressed("up arrow") or keyboard.is_pressed("w")) and selected_item == -1 and not up_arrow_is_pressing:
                    reset_screen()
                    up_arrow_is_pressing = 1
                    if base != possible_base_times[-1]:
                        base = possible_base_times[possible_base_times.index(base) + 1]
                    if keyboard.is_pressed("shift"):
                        base = possible_base_times[-1]
                if (keyboard.is_pressed("down arrow") or keyboard.is_pressed("s")) and selected_item == -1 and not down_arrow_is_pressing:
                    reset_screen()
                    down_arrow_is_pressing = 1
                    if base != possible_base_times[0]:
                        base = possible_base_times[possible_base_times.index(base) - 1]
                    if keyboard.is_pressed("shift"):
                        base = possible_base_times[0]
                if (keyboard.is_pressed("up arrow") or keyboard.is_pressed("w")) and selected_item == 1 and not up_arrow_is_pressing:
                    reset_screen()
                    up_arrow_is_pressing = 1
                    if add != possible_add_times[-1]:
                        add = possible_add_times[possible_add_times.index(add) + 1]
                    if keyboard.is_pressed("shift"):
                        add = possible_add_times[-1]
                if (keyboard.is_pressed("down arrow") or keyboard.is_pressed("s")) and selected_item == 1 and not down_arrow_is_pressing:
                    reset_screen()
                    down_arrow_is_pressing = 1
                    if add != possible_add_times[0]:
                        add = possible_add_times[possible_add_times.index(add) - 1]
                    if keyboard.is_pressed("shift"):
                        add = possible_add_times[0]
                if keyboard.is_pressed("space") and not space_is_pressing:
                    space_is_pressing = 1
                    break
                if not (keyboard.is_pressed("left arrow") or keyboard.is_pressed("a")):
                    left_arrow_is_pressing = 0
                if not (keyboard.is_pressed("right arrow") or keyboard.is_pressed("d")):
                    right_arrow_is_pressing = 0
                if not (keyboard.is_pressed("up arrow") or keyboard.is_pressed("w")):
                    up_arrow_is_pressing = 0
                if not( keyboard.is_pressed("down arrow") or keyboard.is_pressed("s")):
                    down_arrow_is_pressing = 0
                if not keyboard.is_pressed("space"):
                    space_is_pressing = 0
                
                if base%1 == 0:
                    ready_message = str(base)
                elif base == 1/4:
                    ready_message = "1/4"
                elif base == 1/2:
                    ready_message = "1/2"
                elif base == 3/4:
                    ready_message = "3/4"
                font = pygame.font.Font('freesansbold.ttf', fontSize_bignumber)
                if selected_item == -1:
                    text = font.render(ready_message, True, (255, 255, 255))
                else:
                    text = font.render(ready_message, True, (55, 55, 55))
                textRect = text.get_rect()
                textRect.center = (coordx_white, padHeight/2)
                screen.blit(text, textRect)
                ready_message = str(add)
                font = pygame.font.Font('freesansbold.ttf', fontSize_bignumber) 
                if selected_item == -1:
                    text = font.render(ready_message, True, (55, 55, 55))
                else:
                    text = font.render(ready_message, True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (coordx_black, padHeight/2)
                screen.blit(text, textRect)
                ready_message = "+"
                font = pygame.font.Font('freesansbold.ttf', fontSize_bignumber) 
                text = font.render(ready_message, True, (155, 155, 155))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, padHeight/2)
                screen.blit(text, textRect)
                ready_message = "Use arrow keys to control"
                font = pygame.font.Font('freesansbold.ttf', 70) 
                text = font.render(ready_message, True, (155, 155, 155))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 50)
                screen.blit(text, textRect)
                ready_message = "Press space again to return"
                font = pygame.font.Font('freesansbold.ttf', 70) 
                text = font.render(ready_message, True, (155, 155, 155))
                textRect = text.get_rect()
                textRect.center = (padWidth/2, 550)
                screen.blit(text, textRect)
                pygame.display.update()
        
        if not keyboard.is_pressed("space"):
            space_is_pressing = 0
        if not keyboard.is_pressed("s"):
            s_is_pressing = 0

    if first_turn == "left shift":
        second_turn = "right shift"
        coordy_white_up -= turn_effect
        coordy_white_down -= turn_effect
    if first_turn == "right shift":
        second_turn = "left shift"
        coordy_black_up -= turn_effect
        coordy_black_down -= turn_effect
    
    if not clock_start_turn:
        for i in range(ready_time*10, 0, -1):
            reset_screen()
            turn_message = "First turn: " + ("LEFT" if first_turn == "left shift" else "RIGHT")
            font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
            text = font.render(turn_message, True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
            textRect = text.get_rect()
            textRect.center = (padWidth/2, padHeight/2)
            screen.blit(text, textRect)
            font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
            time_message = "Game starts in " + str(i/10)
            text = font.render(time_message, True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
            textRect = text.get_rect()
            textRect.center = (padWidth/2, padHeight/2+fontSize_ready)
            screen.blit(text, textRect)
            pygame.display.update()
            font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
            time_message = "Round " + str(round)
            text = font.render(time_message, True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
            textRect = text.get_rect()
            textRect.center = (padWidth/2, padHeight/2-3*fontSize_ready)
            screen.blit(text, textRect)
            pygame.display.update()
            sleep(0.099)

    while keyboard.is_pressed(first_turn):
        pass
        
    white_current_time = base*60
    black_current_time = base*60
    current_time = time()
    tick = 0
    game_start_time = time()
    press_count = 0
    danger_time1 = base*48
    danger_time2 = base*17
    danger_time3 = base*6.5


    while black*white > 0:
        tick += 1

        if keyboard.is_pressed(first_turn) and turn == -1 and not white_is_pressing:
            turn *= -1
            winsound.Beep(turn_sound[0], turn_sound[1])
            black -= turn_sound[1]/1000
            if not clock_start_turn or (press_count >= 2 and clock_start_turn):
                white_current_time += add
            coordy_white_up += turn_effect*(1 if  first_turn == "left shift" else -1)
            coordy_white_down += turn_effect*(1 if  first_turn == "left shift" else -1)
            coordy_black_up -= turn_effect*(1 if  first_turn == "left shift" else -1)
            coordy_black_down -= turn_effect*(1 if  first_turn == "left shift" else -1)
            white_is_pressing = 1
            press_count += 1
        if keyboard.is_pressed(second_turn) and turn == 1 and not black_is_pressing:
            turn *= -1
            inning += 1
            winsound.Beep(turn_sound[0], turn_sound[1])
            white -= turn_sound[1]/1000
            if not clock_start_turn or (press_count >= 2 and clock_start_turn):
                black_current_time += add
            coordy_white_up -= turn_effect*(1 if  first_turn == "left shift" else -1)
            coordy_white_down -= turn_effect*(1 if  first_turn == "left shift" else -1)
            coordy_black_up += turn_effect*(1 if  first_turn == "left shift" else -1)
            coordy_black_down += turn_effect*(1 if  first_turn == "left shift" else -1)
            black_is_pressing = 1
            press_count += 1
        if keyboard.is_pressed("space") and not space_is_pressing:
            pause_message = "Game paused-Press space to resume, esc to reset"
            font = pygame.font.Font('freesansbold.ttf', fontSize_pause) 
            text = font.render(pause_message, True, (pause_color[0], pause_color[1], pause_color[2]))
            textRect = text.get_rect()
            textRect.center = (600, 100)
            screen.blit(text, textRect)
            pygame.display.update()
            space_is_pressing = 1
            pause_start_time = time()
            while keyboard.is_pressed("space"):
                pass
            while True:
                if keyboard.is_pressed("space"):
                    space_is_pressing = 1
                    for i in range(resume_time*10, 0, -1):
                        reset_screen()
                        pause_message = "Game restarts in " + str(i/10)
                        font = pygame.font.Font('freesansbold.ttf', fontSize_ready) 
                        text = font.render(pause_message, True, (ready_text_color[0], ready_text_color[1], ready_text_color[2]))
                        textRect = text.get_rect()
                        textRect.center = (padWidth/2, padHeight/2)
                        screen.blit(text, textRect)
                        pygame.display.update()
                        sleep(0.099)
                    if turn == -1:
                        white_current_time += (time() - pause_start_time)
                    else:
                        black_current_time += (time() - pause_start_time)
                    break
                if keyboard.is_pressed("esc"):
                    game_over = 1
                    reset_screen()
                    break
        if keyboard.is_pressed("esc"):
            break

        if not keyboard.is_pressed(first_turn):
            white_is_pressing = 0
        if not keyboard.is_pressed(second_turn):
            black_is_pressing = 0
        if not keyboard.is_pressed("space"):
            space_is_pressing = 0

        reset_screen()

        chess_type = str(base) + " + " + str(add)
        
        if not clock_start_turn or (press_count >= 2 and clock_start_turn):
            if turn == -1:
                white_current_time -= (time() - current_time)
            if turn == 1:
                black_current_time -= (time() - current_time)

        if white_current_time <= 0: white_current_time = 0
        if black_current_time <= 0: black_current_time = 0


        delay = time() - current_time
        current_time = time()
        black_elapsed_time_ratio = (base*60 - black_current_time)/(base*60)
        white_elapsed_time_ratio = (base*60 - white_current_time)/(base*60)

        if display_time == "minute and second":
            if len(str((int(white_current_time)%60))) == 1:
                white_up = str(int(white_current_time)//60) + ":0" + str((int(white_current_time)%60))
            else:
                white_up = str(int(white_current_time)//60) + ":" + str((int(white_current_time)%60))
            if white_current_time == 0:
                white_down = ""
            else:
                white_down = str(white_current_time - white_current_time//1)[2:2 + time_digits]
                if len(white_down) < time_digits: white_down = "0"*time_digits
        if display_time == "second":
            white_up = str(int(white_current_time))
            if white_current_time == 0:
                white_down = ""
            else:
                white_down = str(white_current_time - white_current_time//1)[2:2 + time_digits]
                if len(white_down) < time_digits: white_down = "0"*time_digits
        if display_time == "percentage":
            white_up = str(int(100*white_current_time/(base*60))) + "%"
            white_down = str(list(map(str, (str(100*white_current_time/(base*60))).split('.')))[1])[:time_digits]
            if len(white_down) < time_digits: white_down = "0"*time_digits

        if display_time == "minute and second":
            if len(str((int(black_current_time)%60))) == 1:
                black_up = str(int(black_current_time)//60) + ":0" + str((int(black_current_time)%60))
            else:
                black_up = str(int(black_current_time)//60) + ":" + str((int(black_current_time)%60))
            if black_current_time == 0:
                black_down = ""
            else:
                black_down = str(black_current_time - black_current_time//1)[2:2 + time_digits]
                if len(black_down) < time_digits: black_down = "0"*time_digits
        if display_time == "second":
            black_up = str(int(black_current_time))
            if black_current_time == 0:
                black_down = ""
            else:
                black_down = str(black_current_time - black_current_time//1)[2:2 + time_digits]
                if len(black_down) < time_digits: black_down = "0"*time_digits
        if display_time == "percentage":
            black_up = str(int(100*black_current_time/(base*60))) + "%"
            black_down = str(list(map(str, (str(100*black_current_time/(base*60))).split('.')))[1])[:time_digits]
            if len(black_down) < time_digits: black_down = "0"*time_digits


        if black_current_time == 0:
            black_down = ""
        if white_current_time == 0:
            white_down = ""
        inning_middle = "{:03d}".format(inning)


        font = pygame.font.Font('freesansbold.ttf', fontSize_bignumber)
        if len(number_up_color) == 1:
            if white_current_time >= danger_time1:
                text = font.render(white_up, True, (number_up_color[0][0], number_up_color[0][1], number_up_color[0][2]))
            elif white_current_time >= danger_time2:
                text = font.render(white_up, True, (danger_color1[0], danger_color1[1], danger_color1[2]))
            elif white_current_time >= danger_time3:
                text = font.render(white_up, True, (danger_color2[0], danger_color2[1], danger_color2[2]))
            elif white_current_time > 0:
                text = font.render(white_up, True, (danger_color3[0], danger_color3[1], danger_color3[2]))
            else:
                text = font.render(white_up, True, (end_color[0], end_color[1], end_color[2]))
        else:
            if white_elapsed_time_ratio < 0:
                text = font.render(white_up, True, (number_up_color[0][0], number_up_color[0][1], number_up_color[0][2]))
            else:
                start_color = number_up_color[0]
                end_color = number_up_color[1]
                white_current_color = []
                white_current_color.append(((end_color[0] - start_color[0])*white_elapsed_time_ratio + start_color[0])//1)
                white_current_color.append(((end_color[1] - start_color[1])*white_elapsed_time_ratio + start_color[1])//1)
                white_current_color.append(((end_color[2] - start_color[2])*white_elapsed_time_ratio + start_color[2])//1)
                text = font.render(white_up, True, (white_current_color[0], white_current_color[1], white_current_color[2]))
        textRect = text.get_rect()
        if first_turn == "left shift":
            textRect.center = (coordx_white, coordy_white_up)
        if first_turn == "right shift":
            textRect.center = (coordx_black, coordy_black_up)
        screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', fontSize_smallnumber) 
        text = font.render(white_down, True, (number_down_color[0], number_down_color[1], number_down_color[2]))
        textRect = text.get_rect()
        if first_turn == "left shift":
            textRect.center = (coordx_white, coordy_white_down)
        if first_turn == "right shift":
            textRect.center = (coordx_black, coordy_black_down)
        screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', fontSize_bignumber)
        if len(number_up_color) == 1:
            if black_current_time >= danger_time1:
                text = font.render(black_up, True, (number_up_color[0][0], number_up_color[0][1], number_up_color[0][2]))
            elif black_current_time >= danger_time2:
                text = font.render(black_up, True, (danger_color1[0], danger_color1[1], danger_color1[2]))
            elif black_current_time >= danger_time3:
                text = font.render(black_up, True, (danger_color2[0], danger_color2[1], danger_color2[2]))
            elif black_current_time > 0:
                text = font.render(black_up, True, (danger_color3[0], danger_color3[1], danger_color3[2]))
            else:
                text = font.render(black_up, True, (end_color[0], end_color[1], end_color[2]))
        else:
            if black_elapsed_time_ratio < 0:
                text = font.render(white_up, True, (number_up_color[0][0], number_up_color[0][1], number_up_color[0][2]))
            else:
                start_color = number_up_color[0]
                end_color = number_up_color[1]
                black_current_color = []
                black_current_color.append(((end_color[0] - start_color[0])*black_elapsed_time_ratio + start_color[0])//1)
                black_current_color.append(((end_color[1] - start_color[1])*black_elapsed_time_ratio + start_color[1])//1)
                black_current_color.append(((end_color[2] - start_color[2])*black_elapsed_time_ratio + start_color[2])//1)
                text = font.render(black_up, True, (black_current_color[0], black_current_color[1], black_current_color[2]))
        textRect = text.get_rect()
        if first_turn == "left shift":
            textRect.center = (coordx_black, coordy_black_up)
        if first_turn == "right shift":
            textRect.center = (coordx_white, coordy_white_up)
        screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', fontSize_smallnumber)
        text = font.render(black_down, True, (number_down_color[0], number_down_color[1], number_down_color[2]))
        textRect = text.get_rect()
        if first_turn == "left shift":
            textRect.center = (coordx_black, coordy_black_down)
        if first_turn == "right shift":
            textRect.center = (coordx_white, coordy_white_down)
        screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', fontSize_inning) 
        if ((((2*white_current_time)//1)%2 == 0 and turn == -1) or (((2*black_current_time)//1)%2 == 0 and turn == 1)) and blink_effect:
            text = font.render(inning_middle, True, (screen_color[0], screen_color[1], screen_color[2]))
        else:
            text = font.render(inning_middle, True, (inning_color[0], inning_color[1], inning_color[2]))
        textRect = text.get_rect()
        textRect.center = (coordx_inning, coordy_inning)
        screen.blit(text, textRect)

        try:
            if display_fps: 
                fps_log.append(1/delay)
                avg_fps = str("{:.2f}".format(sum(fps_log)/len(fps_log)))
                fps = str("{:.2f}".format(1/delay))
                if (time() - game_start_time) >= 30 or round != 1: fps_log.remove(fps_log[0])

            font = pygame.font.Font('freesansbold.ttf', fontSize_fps)
            text = font.render("FPS = " + avg_fps, True, (fps_color[0], fps_color[1], fps_color[2]))
            textRect = text.get_rect()
            textRect.center = (padWidth/2, 40)
            screen.blit(text, textRect)
        except: pass

        font = pygame.font.Font('freesansbold.ttf', fontSize_fps)
        text = font.render("Round " + str(round) + " (" +chess_type + ")", True, (game_mode_color[0], game_mode_color[1], game_mode_color[2]))
        textRect = text.get_rect()
        textRect.center = (padWidth/2, 560)
        screen.blit(text, textRect)
        pygame.display.update()

        if black_current_time*white_current_time <= 0 or game_over == 1: break

    if show_end_message:
        ready_message = "Game over"
        font = pygame.font.Font('freesansbold.ttf', 70) 
        text = font.render(ready_message, True, (70, 70, 70))
        textRect = text.get_rect()
        textRect.center = (padWidth/2, 150)
        screen.blit(text, textRect)
        ready_message = "Press enter to restart"
        font = pygame.font.Font('freesansbold.ttf', 70) 
        text = font.render(ready_message, True, (70, 70, 70))
        textRect = text.get_rect()
        textRect.center = (padWidth/2, 400)
        screen.blit(text, textRect)
        pygame.display.update()

    winsound.Beep(end_sound[0], end_sound[1])

    while not keyboard.is_pressed("esc"):
        pass