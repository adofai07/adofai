import copy
import random
import math
import sys
import glob

cout = sys.stdout.write

def read(path):
    f = open(path, "r")
    data = f.readlines()
    f.close()

    return "".join(data)

def prob(curr, new):
    if new >= 8140: return 2
    
    res = math.tanh((new - curr) / 35) * 0.5 + 0.5

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
    for number in range(1, 100000):
        N = str(number)

        if "0" < N[-1] < N[0]: continue

        found = False

        for i in range(8):
            for j in range(14):
                if not found and arr[i][j] == N[0]:
                    found = find(arr, i, j, N)

        if not found: return number - 1

try:
    progress = glob.glob("C:/SSHS/814/*.txt")
    temp = read(progress[-(random.randrange(0, 3) % len(progress)) - 1])

except:
    temp = """
    00000000000000
    00000000000000
    00000000000000
    00000000000000
    00000000000000
    00000000000000
    00000000000000
    00000000000000
    """



arr = [list(i) for i in temp.split()]
curr_val = result(arr)


MAX = copy.deepcopy(curr_val)
MAXARR = copy.deepcopy(arr)
ITER = 120000
UPDATE = 5

step = 0
for i in range(ITER-1, -1, -1):
    T = 1
    step += 1

    if random.uniform(0, 1) < 0.2: T = 2
    if random.uniform(0, 1) < 0.01: T = 3
    if random.uniform(0, 1) < 0.001: T = 4

    new_arr = copy.deepcopy(arr)

    for _ in range(T):
        rand_x = random.randrange(0, 8)
        rand_y = random.randrange(0, 14)

        new_arr[rand_x][rand_y] = str(random.randrange(0, 10))

    new_val = result(new_arr)

    if random.uniform(0, 1) < prob(curr_val, new_val):
        arr = copy.deepcopy(new_arr)
        curr_val = copy.deepcopy(new_val)

    if i % UPDATE == 0:
        cout("STEP = {:06.0f} ({:05.2f}%) / T = {:04.0f} / MAX = {} / RES = {}\r".format(step, step * 100 / ITER, T, MAX, curr_val))
    
    if curr_val > MAX:
        MAX = curr_val
        MAXARR = copy.deepcopy(arr)

        f = open("C:/SSHS/814/{:04.0f}.txt".format(MAX), "w+")
        f.write("\n".join("".join(str(b) for b in a) for a in arr))
        f.close()

    if curr_val >= 8140: break
