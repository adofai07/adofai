import bisect
import collections
import copy
import decimal
import fractions
import itertools
import math
import random
import sys
import time
from contextlib import contextmanager
from functools import lru_cache

cin = sys.stdin.readline
cout = sys.stdout.write

decimal.getcontext().prec = 50
sys.setrecursionlimit(2147483647)

C = math.comb
D = decimal.Decimal
E = decimal.Decimal("2.71828182845904523536028747135266249775724709369995")
F = fractions.Fraction
P = math.perm
BS = bisect.bisect
CH = itertools.chain
DC = copy.deepcopy
DQ = collections.deque
LN = math.log
PI = decimal.Decimal("3.141592653589793238462643383279502884197169399375105820974944")
ACC = itertools.accumulate
BSL = bisect.bisect_left
BSR = bisect.bisect_right
COS = math.cos
GCD = math.gcd
GRB = itertools.groupby
LCM = math.lcm
MOD = 1_000_000_007
POW = math.pow
SIN = math.sin
TAN = math.tan
CEIL = math.ceil
SQRT = math.sqrt
ATAN2 = math.atan2
FLOOR = math.floor

@contextmanager
def color(*args):
    cout("\033[38;2;{}m".format(";".join(map(str, args))))
    yield
    cout("\033[38;2;255;255;255m")

class PStools:
    class bisect:
        @lru_cache(maxsize = None)
        def int_left(lower_bound: int, upper_bound: int, goal: int, f: callable) -> int:
            start, end = lower_bound, upper_bound

            while True:
                mid = (start + end) // 2

                if f(start) == goal: return start

                if start == end - 1:
                    if f(end) == goal: return end
                    return start

                if f(mid) < goal: start = mid
                else: end = mid

        @lru_cache(maxsize = None)
        def int_right(lower_bound: int, upper_bound: int, goal: int, f: callable) -> int:
            start, end = lower_bound, upper_bound

            while True:
                mid = (start + end + 1) // 2

                if f(end) == goal: return end

                if start == end - 1:
                    if f(start) == goal: return start
                    return end

                if f(mid) > goal: start = mid
                else: end = mid

        @lru_cache(maxsize = None)
        def float_left(lower_bound: float, upper_bound: float, goal: float, f: callable, accuracy: float = 0.0001) -> float:
            start, end = D(lower_bound), D(upper_bound)

            if f(start) == goal: return start
            if f(end) == goal: return end

            mid = (start + end) / D(2)

            while end - start > accuracy:
                mid = (start + end) / D(2)

                if f(mid) < goal: start = mid
                else: end = mid
            
            return mid

        @lru_cache(maxsize = None)
        def float_right(lower_bound: float, upper_bound: float, goal: float, f: callable, accuracy: float = 0.0001) -> float:
            start, end = D(lower_bound), D(upper_bound)

            if f(start) == goal: return start
            if f(end) == goal: return end

            mid = (start + end) / D(2)

            while end - start > accuracy:
                mid = (start + end) / 2

                if f(mid) > goal: start = mid
                else: end = mid
            
            return mid

        @lru_cache(maxsize = None)
        def parse_left(arr: tuple, lower_bound: any, upper_bound: any) -> tuple:
            return arr[BSL(arr, lower_bound): BS(arr, upper_bound)]

    class ntheory:
        @lru_cache(maxsize = None)
        def pow_mod(n: int, k: int, m: int) -> int:
            res = 1

            while k:
                if k % 2: res *= n; res %= m
                k >>= 1; n = n ** 2 % m

            return res
        
        @lru_cache(maxsize = None)
        def fact_mod(n: int, k: int) -> int:
            prod = 1

            for i in range(2, n+1):
                prod = (prod * i) % k
            
            return prod

        @lru_cache(maxsize = None)
        def primerange(start: int, end: int) -> tuple:
            temp = [True for i in range(end + 2)]
            temp[0], temp[1] = False, False

            for i in range(2, FLOOR(SQRT(end))+2):
                if temp[i]:
                    for j in range(2*i, end + 2, i):
                        temp[j] = False
            
            return [i for i in range(max(2, start), end+1) if temp[i]]

        @lru_cache(maxsize = None)
        def catalan(n: int) -> int:
            if n == 0: return 1

            return 2 * PStools.ntheory.catalan(n-1) * (2*n-1) // (n + 1)

        @lru_cache(maxsize = None)
        def fibonacci(n: int) -> int:
            if n == 0: return 0
            if n == 1 or n == 2: return 1

            a, b = PStools.ntheory.fibonacci(n//3), PStools.ntheory.fibonacci(n//3+1)

            if n%3 == 0: return 5*a**3+3*(-1)**n*a
            if n%3 == 1: return b**3+3*b*a**2-a**3
            if n%3 == 2: return b**3+3*a*b**2+a**3

        @lru_cache(maxsize = None)
        def fibonacci_mod(n: int, k: int) -> int:
            if n == -1 or n == 1 or n == 2: return 1 % k
            if n == 0: return 0

            a, b = PStools.ntheory.fibonacci_mod(n//3, k), PStools.ntheory.fibonacci_mod(n//3+1, k)

            if n%3 == 0: return (5*a**3+3*(-1)**n*a) % k
            if n%3 == 1: return (b**3+3*b*a**2-a**3) % k
            if n%3 == 2: return (b**3+3*a*b**2+a**3) % k

        @lru_cache(maxsize = None)
        def factorial(n: int) -> int:
            return math.factorial(n)

        @lru_cache(maxsize = None)
        def factorize(n: int, type: classmethod) -> dict:
            res = []

            while n > 1:
                divisor = PStools.ntheory.pollard_rho(n)
                res.append(divisor)
                n //= divisor

            res.sort()

            if type == list: return res

            if type == dict: return {k: len(list(g)) for k, g in GRB(res)}
            
        def allfactors(n: int) -> list:
            temp = PStools.ntheory.factorize(n, dict)
            res = [1]
            
            for k, v in temp.items():
                power = k
                l = len(res)
                for _ in range(v):
                    for i in range(l):
                        res.append(res[i] * power)
                        
                    power *= k

            res.sort()
            return res                 

        @lru_cache(maxsize = None)
        def totient(n: int) -> int:
            for p in PStools.ntheory.factorize(n, dict).keys():
                n //= p
                n *= p-1
            
            return n

        @lru_cache(maxsize = None)
        def stirling1(n: int, k: int) -> int:
            if n == k: return 1
            if n == 2 and k == 1: return 1
            if n * k == 0: return 0
            return (n-1) * PStools.ntheory.stirling1(n-1, k) + PStools.ntheory.stirling1(n-1, k-1)

        def p(b, e, m):
            res = 1
            b = b % m
            while e > 0:
                if e & 1:
                    res = (res * b) % m

                b = (b * b) % m
                e = e >> 1
                
            return res

        def miller_rabin(n, k):
            if n == 1: return False
            if n == 2 or n == 3: return True

            r, s = 0, n - 1
            while s % 2 == 0:
                r += 1
                s //= 2
            for _ in range(k):
                a = random.randrange(2, n - 1)
                x = PStools.ntheory.p(a, s, n)
                if x in [1, n - 1]: continue
                for _ in range(r - 1):
                    x = PStools.ntheory.p(x, 2, n)
                    if x == n - 1: break
                else: return False
            return True

        def get_prime(n):
            temp = [2, 3, 5, 7, 9, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47]
            if n == 1: return False
            if n == 2 or n == 3: return True
            if n%2 == 0: return False

            for i in temp:
                if n == i: return True
                if not PStools.ntheory.miller_rabin(n, i): return False
            return True

        def pollard_rho(n):
            if PStools.ntheory.get_prime(n): return n
            if n == 1: return n
            if n%2 == 0: return 2

            x = random.randrange(2, n)
            y = x
            c = random.randrange(1, n)
            d = 1

            while d == 1:
                x = ((x ** 2) % n + c + n) % n
                y = ((y ** 2) % n + c + n) % n
                y = ((y ** 2) % n + c + n) % n

                d = math.gcd(abs(x-y), n)
                if d == n: return PStools.ntheory.pollard_rho(n)
            if PStools.ntheory.get_prime(d): return d
            else: return PStools.ntheory.pollard_rho(d)

    class algebra:
        @lru_cache(maxsize = None)
        def integral(lower_bound: float, upper_bound: float, f: callable, split: int) -> float:
            res = D(0)

            for i in range(split):
                try:
                    a = D(lower_bound + (upper_bound - lower_bound) * i) / D(split)
                    b = D(lower_bound + (upper_bound - lower_bound) * (i+1)) / D(split)

                    res += D(f(a)) + D(f(b)) + D(4) * f(D(a+b)/D(2))

                except: ...

            return D(upper_bound - lower_bound) * res / D(6) / D(split)

        @lru_cache(maxsize = None)
        def sin(x: D, iter: int) -> D:
            x = x%(2*PI) - PI

            if x > PI / 2: x = PI - x
            if x < -1 * PI / 2: x = -PI - x

            res = D(0)

            for i in range(iter):
                res -= D((-1) ** i) * x ** (2*i + 1) / D(PStools.ntheory.factorial(2*i + 1))

            return res

    class geometry:
        @lru_cache(maxsize = None)
        def intersects(a, b, c, d, e, f, g, h):
            CCW1 = ((c-a)*(f-b) - (e-a)*(d-b)) * ((c-a)*(h-b) - (g-a)*(d-b))
            CCW2 = ((g-e)*(b-f) - (a-e)*(h-f)) * ((g-e)*(d-f) - (c-e)*(h-f))

            if CCW1 == CCW2 == 0:
                if (a == c and b > d) or a > c:
                    a, b, c, d = c, d, a, b

                if (e == g and f > h) or e > g:
                    e, f, g, h = g, h, e, f

                if ((a == g and b <= h) or a < g) and ((c == e and d >= f) or c > e): return True
                else: return False

            if CCW1 <= 0 and CCW2 <= 0:
                return True
            
            return False

        @lru_cache(maxsize = None)
        def coord_inter(a, b, c, d, e, f, g, h):
            if PStools.geometry.intersects(a, b, c, d, e, f, g, h):

                try: return (((a*d-b*c)*(e-g)-(a-c)*(e*h-f*g))/((a-c)*(f-h)-(b-d)*(e-g)), ((a*d-b*c)*(f-h)-(b-d)*(e*h-f*g))/((a-c)*(f-h)-(b-d)*(e-g)))
                except:
                    if (a == c and b > d) or a > c:
                        a, b, c, d = c, d, a, b

                    if (e == g and f > h) or e > g:
                        e, f, g, h = g, h, e, f

                    if c == e and d == f: return (c, d)
                    elif a == g and b == h: return (a, b)

    class algorithm:
        def LDS(arr: tuple) -> list:
            dp, temp, res = [], [], []

            for i in arr:
                if not dp or i > dp[-1]: dp.append(i); temp.append((len(dp)-1,i))
                else: dp[BSL(dp, i)] = i; temp.append((BSL(dp, i), i))

            idx = len(dp)-1

            for i in range(len(temp)-1, -1, -1):
                if temp[i][0] == idx:
                    res.append(temp[i][1])
                    idx -= 1

            return res

start_time = time.time()

"""
Enter code from here
"""

def f(X, Y, Z):
    if Z == 0: return 5
    return PStools.ntheory.pow_mod(PStools.ntheory.fibonacci_mod(X, Z), Y, Z)

def formula_maker(p, add):
    if random.randrange(1, 100) < p: return str(random.randrange(10000000, 100000000))
    else: return "f({}, {}, {})".format(formula_maker(p + add, add), formula_maker(p + add, add), formula_maker(p + add, add))

if 1:
    while True:
        a = formula_maker(int(input()), float(input()))
        
        f = open("formula.txt", "w+")
        f.write("f(X, Y, Z) = (Xth fibonacci number to the power of Y modulo Z) if Z is positive, else 5\n\n")
        f.write("Password is the value of the following ({} letters, {} functions):\n\n".format(len(a), a.count("f")))
        f.write(a)
        f.close()

else:
    print()