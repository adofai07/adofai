import itertools
import copy
import sys
import os

global n, fact, people, advocate, chance, left, votes

def end():
    total = sum(chance.values())

    for k, v in chance.items():
        chance[k] = "{:.4f}".format(100 * v / total)
        print("Winner: \033[38;2;0;255;0m{}\033[38;2;255;255;255m / Chance: \033[38;2;0;255;0m{}\033[38;2;255;255;255m%".format(k, chance[k]))

    sys.exit(0)


people = int(input())
advocate = list(map(int, input().split()))
left = people - sum(advocate)
n = len(advocate)
chance = dict()
fact = {0: 1}
for i in range(max(left, n*3)):
    fact[i+1] = fact[i] * (i+1)

for i in range(1, n+1):
    for j in itertools.combinations([str(c+1) for c in range(n)], i):
        chance[", ".join(j)] = 0

os.system("cls")

CHOICE = [
"random",
"same",
"two-s"
][2]

if CHOICE == "random":
    choice = [1 for _ in range(n)]
elif CHOICE == "same":
    choice = copy.deepcopy(advocate)
elif CHOICE == "two-s":
    for pair in itertools.combinations([i for i in range(n)], 2):
        first, second = 0, 0

        for i in range(left+1):
            if advocate[pair[0]] + i >= advocate[pair[1]] + left - i:
                first += fact[left] // (fact[i] * fact[left - i])
            if advocate[pair[0]] + i <= advocate[pair[1]] + left - i:
                second += fact[left] // (fact[i] * fact[left - i])

        for k in chance.keys():
            temp = k.split(", ")

            if str(pair[0] + 1) in temp:
                chance[k] += first
            if str(pair[1] + 1) in temp:
                chance[k] += second
            
    for i in range(1, n+1):
        for j in itertools.combinations([str(c+1) for c in range(n)], i):
            chance[", ".join(j)] = chance[", ".join(j)]**1.1
            chance[", ".join(j)] //= fact[i*3]
            
    end()


votes = []

def backtrack(step = 0):
    if step == n:
        result = [advocate[i] + votes[i] for i in range(n)]

        winner = []
        max_votes = max(result)

        for i in range(n):
            if result[i] == max_votes:
                winner.append(i+1)

        occur = fact[left]

        for i in range(n):
            occur //= fact[votes[i]]
            occur *= choice[i]**votes[i]

        chance[", ".join(map(str, winner))] += occur

        return

    if step < n-1:
        for i in range(left - sum(votes) + 1):
            votes.append(i)
            backtrack(step = step + 1)
            votes.pop()
    if step == n-1:
        votes.append(left - sum(votes))
        backtrack(step = step + 1)
        votes.pop()
    
backtrack()

end()