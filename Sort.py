import bisect
import os
import statistics
import sys
import time
import random
import traceback
import plotly.express
import matplotlib.pyplot

import tensorflow

tensorflow.debugging.set_log_device_placement(True)
os.system("cls")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def counting_sort(array):
    _min = min(array)
    _max = max(array)

    for i in range(len(array)):
        array[i] -= _min

    #counting array 생성
    counting_array = [0]*(_max+1)
 
    #counting array에 input array내 원소의 빈도수 담기
    for i in array:
        counting_array[i] += 1
 
    #counting array 업데이트.
    for i in range(_max):
        counting_array[i+1] += counting_array[i]
 
    #output array 생성
    output_array = [-1]*len(array)
 
    #output array에 정렬하기(counting array를 참조)
    for i in array:
        output_array[counting_array[i] -1] = i
        counting_array[i] -= 1

    for i in range(len(array)):
        output_array[i] += _min

    return output_array

times = []

x = []
y = []

try:
    f = open("./Sort_data.txt", "r")
    temp = f.readlines()
    f.close()
    prev_data = temp[-1].strip()
    RANGE = int(prev_data.split(" / ")[1][8:])
    SIZE = int(prev_data.split(" / ")[0][7:])
    UPDATE = 25

    for i in temp:
        x.append(int(i.split(" / ")[1][8:]))
        y.append(int(i.split(" / ")[0][7:]))

    write = False
except:
    # print(traceback.format_exc(chain = False).split("\n")[-2])
    RANGE = 700
    SIZE = 100
    UPDATE = 25
    write = True

while True:
    print(f"Size of data: \033[38;2;123;255;123m{SIZE}\033[38;2;255;255;255m / Range of data: \033[38;2;123;255;123m{RANGE}\033[38;2;255;255;255m / \033[38;2;123;255;123m{len(x)+1}\033[38;2;255;255;255mth data")

    time_log1 = []
    time_log2 = []

    sum1, sum2 = 0, 0

    measure_start_time = time.time()
    stop_tolerance = False

    left_time = 8
    bonus_time = 0

    give_bonus_time = True

    current_time = time.time()

    i = 1
    while left_time + bonus_time > 0 or give_bonus_time:
        data = [random.randrange(RANGE) for _ in range(SIZE)]

        delay = time.time() - current_time
        current_time = time.time()

        if left_time > 0:
            left_time -= delay
        else:
            bonus_time -= delay

        if i%2 == 0:
            start_time = time.time()
            quick_sort(data)
            sum1 += time.time() - start_time

            start_time = time.time()
            counting_sort(data)
            sum2 += time.time() - start_time
        else:
            start_time = time.time()
            counting_sort(data)
            sum2 += time.time() - start_time
            
            start_time = time.time()
            quick_sort(data)
            sum1 += time.time() - start_time


        mean1, mean2 = sum1 / i, sum2 / i

        i += 1

        if i % UPDATE: continue

        if give_bonus_time and left_time <= 0:
            give_bonus_time = False
            bonus_time += min(0.07 * (0.1 * (mean1 + mean2) / abs(mean1 - mean2))**1.5, 15)

        if abs(mean1 - mean2) / (mean1 + mean2) > 0.01: bonus_time = 0

        try: sys.stdout.write("CASE #\033[38;2;255;123;123m{}\033[38;2;255;255;255m: Quick: \033[38;2;123;123;255m{:.7f}\033[38;2;255;255;255m / Counting: \033[38;2;123;123;255m{:.7f}\033[38;2;255;255;255m / Difference: \033[38;2;123;123;255m{:05.2f}\033[38;2;255;255;255m% (Ends in \033[38;2;123;255;255m{:.1f}\033[38;2;255;255;255m + \033[38;2;123;255;255m{:.1f}\033[38;2;255;255;255ms)     \r".format(
            i,
            mean1,
            mean2,
            200 * abs(mean1 - mean2) / (mean1 + mean2),
            abs(left_time),
            abs(bonus_time)
        ))
        except: pass


    print("\n\n" + "-"*os.get_terminal_size()[0] + "\n")

    if write:
        f = open("./Sort_data.txt", "a+")
        f.write("Size = {} / Range = {} / Inaccuracy = {:.3f}%\n".format(SIZE, RANGE, 200 * abs(mean1 - mean2) / (mean1 + mean2)))
        f.close()

        y.append(SIZE)
        x.append(RANGE)

    # graph = plotly.express.scatter(x, y)
    # graph.show()

    if len(x)%25 == 0:
        matplotlib.pyplot.scatter(x, y)
        matplotlib.pyplot.show(block = False)
        matplotlib.pyplot.pause(3)
        matplotlib.pyplot.close()
    
    write = True

    if mean1 > mean2:
        RANGE = round(RANGE * 1.01)
    if mean2 > mean1:
        SIZE = round(SIZE * 1.01)