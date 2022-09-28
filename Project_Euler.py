import sympy.ntheory
import sys
import sympy
import os

primes = [i for i in sympy.primerange(5000)]

candidate = list(range(1, 50000001))

os.system("cls")

for p in primes:
    for r in range(1, p//2+1):
        sys.stdout.write(f"Searching {p}\r")
        if (2*r**2-1)%p == 0:
            sys.stdout.write(f"Removing {p}/{r}\r")
            cnt = 0
            for c in range(len(candidate)):
                if candidate[c]%p == r:
                    # sys.stdout.write(f"Searching for {p}/{r}... Removing {candidate[c]}\r")
                    candidate[c] = 0
                    cnt += 1
            
            sys.stdout.write(f"Removing {p}/{r} - Removed {cnt} - Remain {len(candidate)-candidate.count(0)}\n")

cnt = 0

for i in candidate:
    if i == 0: continue
    if list(sympy.ntheory.factorint(2*i**2-1).values()) == [1]: cnt += 1

    if cnt%200 == 0:sys.stdout.write(f"Checking {i} / Result = {cnt}\r")

sys.stdout.write(f"Checking {i} / Result = {cnt}\n")