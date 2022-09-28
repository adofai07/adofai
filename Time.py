import time
import sys

TIMEOUT = 60
TRIES = 15

program_start_time = time.time()
method1, method2 = 0, 0
WHITE, GREEN, BLUE = [
"\033[38;2;255;255;255m",
"\033[38;2;0;255;0m",
"\033[38;2;64;64;255m"
]

CODE = "li = list(range(123456))"

code1 = """
for i in range(len(li)):
    li[i] += 5
"""

code2 = """
li = list(map(lambda x: x+5, li))
"""

for _ in range(TRIES):
    i = -1
    while method1 + method2 < TIMEOUT:
        exec(CODE)
        i += 1
        if i%2 == 0:
            start_time = time.time()
            exec(code1)
            method1 += time.time() - start_time

            start_time = time.time()
            exec(code2)
            method2 += time.time() - start_time
        
        else:
            start_time = time.time()
            exec(code2)
            method2 += time.time() - start_time

            start_time = time.time()
            exec(code1)
            method1 += time.time() - start_time

        if method1 + method2: sys.stdout.write("Code 1 {}{:.2f}{} {}{:.2f}{} {} {}{:.2f}{} {}{:.2f}{} Code 2\r".format(GREEN, method1, WHITE, BLUE, 100 * method1 / (method1 + method2), WHITE, "<>"[method1 > method2], BLUE, 100 * method2 / (method1 + method2), WHITE, GREEN, method2, WHITE))
        
    method1, method2 = 0, 0
    print()
