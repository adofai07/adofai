import copy
import random
import math
import sys
import glob

print = sys.stdout.write

def read(path):
    f = open(path, "r")
    data = f.readlines()
    f.close()

    return "".join(data)

def prob(curr, new):
    if new >= 8140: return 2
    
    res = math.tanh((new - curr) / 5) * 0.5 + 0.5

    if res < 0.5: res *= 0.75

    return res

def find(arr, x, y, number):
    BFS = [(x, y)]
    for i in range(1, len(number)):
        for curr in copy.deepcopy(BFS):
            adjacent = [
            (curr[0]+1, curr[1]), (curr[0]-1, curr[1]), (curr[0], curr[1]+1), (curr[0], curr[1]-1),
            (curr[0]+1, curr[1]+1), (curr[0]-1, curr[1]+1), (curr[0]-1, curr[1]-1), (curr[0]+1, curr[1]-1)
            ]

            for coord in adjacent:
                if 0 <= coord[0] < 8 and 0 <= coord[1] < 14 and arr[coord[0]][coord[1]] == number[i]:
                    BFS.append(coord)
            
            BFS.remove(curr)

    return len(BFS) != 0

def result(arr):
    res = 0
    for number in range(1, 8141):
        N = str(number)

        found = False

        for i in range(8):
            for j in range(14):
                if arr[i][j] == N[0]:
                    found = find(arr, i, j, N)
                
                if found: break
            if found: break
        
        if found: res += 1

    return res


try:
    progress = glob.glob("C:/SSHS/814_D/*.txt")
    temp = read(progress[-(random.randrange(0, 4) % len(progress)) - 1])

except:
    temp = """
    33333333333111
    44444444444111
    55555555555111
    66666666666111
    77777777777222
    88888888888222
    99999999999222
    00000000000222
    """


arr = [list(i) for i in temp.split()]
curr_val = result(arr)

MAX = 0
MAXARR = None
ITER = 30
UPDATE = 1

step = 0
for i in range(ITER-1, -1, -1):
    T = 1
    step += 1

    if random.uniform(0, 1) < 0.01: T = 2
    if random.uniform(0, 1) < 0.007: T = 3
    if random.uniform(0, 1) < 0.001: T = 4

    new_arr = copy.deepcopy(arr)

    for _ in range(T):
        rand_x1 = random.randrange(0, 8)
        rand_y1 = random.randrange(0, 14)
        rand_x2 = random.randrange(0, 8)
        rand_y2 = random.randrange(0, 14)

        new_arr[rand_x1][rand_y1], new_arr[rand_x2][rand_y2] = arr[rand_x2][rand_y2], arr[rand_x1][rand_y1]

    new_val = result(new_arr)

    if random.uniform(0, 1) < prob(curr_val, new_val):
        arr = copy.deepcopy(new_arr)
        curr_val = copy.deepcopy(new_val)

    if i % UPDATE == 0:
        print("STEP = {:06.0f} ({:05.2f}%) / T = {:04.0f} / MAX = {} / RES = {}\r".format(step, step * 100 / ITER, T, MAX, curr_val))
    
    if curr_val > MAX:
        MAX = curr_val
        MAXARR = copy.deepcopy(arr)

        f = open("C:/SSHS/814_D/{:04.0f}.txt".format(MAX), "w+")
        f.write("\n".join("".join(str(b) for b in a) for a in arr))
        f.close()

    if curr_val >= 8140: break
