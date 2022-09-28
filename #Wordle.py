from nltk.corpus import words
import random
import os
dictionary_ = list(words.words())
dictionary = []
data = len(dictionary_)
if input("Would you use enhanced searching? It will take a lot of time! (Y/N)").upper() == "Y":
    for i in range(len(dictionary_)):
        if dictionary.count(dictionary_[i]) == 0: dictionary.append(dictionary_[i])
        if i%500 == 0: print(" %06.2f%% complete (%d out of %d)" %(100*i/(data-1), i, data-1), end = "\r")
else:
    dictionary = list(words.words())
data = len(dictionary)
exception = []
ball = []
strike = []
candidate = []
length = 5

os.system("cls")

for i in range(len(dictionary)):
    dictionary[i] = list(dictionary[i].lower())

while True:
    userinput = list(input().split())

    if len(userinput) == 0: continue

    if userinput[0] in ["reset"]:
        strike.clear()
        ball.clear()
        exception.clear()
        candidate.clear()
    if userinput[0] in ["strike", "-s"]:
        userinput = [userinput[0]] + list("".join(userinput[1:]))
        for i in range(1, len(userinput), 2):
            strike.append([userinput[i], int(userinput[i+1])])
    if userinput[0] in ["ball", "-b"]:
        userinput = [userinput[0]] + list("".join(userinput[1:]))
        for i in range(1, len(userinput), 2):
            ball.append([userinput[i], int(userinput[i+1])])
    if userinput[0] in ["remove", "-r"]:
        userinput = [userinput[0]] + list("".join(userinput[1:]))
        for i in range(1, len(userinput)):
            exception.append(userinput[i])
    if userinput[0] in ["clear", "-c"]:
        exception.clear()
        ball.clear()
        strike.clear()
        candidate.clear()
    if userinput[0] in ["length", "-l"]:
        length = int(userinput[1])
    if userinput[0] in ["print"]:
        os.system("cls")
        for i in range(len(candidate)):
            print(candidate[i])
        print(f"\n{len(candidate)} cases found")
        input()
    if userinput[0] in ["random"]:
        os.system("cls")
        try:
            for _ in range(int(userinput[1])):
                print(candidate[random.randrange(len(candidate))])
                print(f"\n{len(candidate)} cases found")
        except:
            try:
                print(candidate[random.randrange(len(candidate))])
                print(f"\n{len(candidate)} cases found")
            except:
                print("You have to insert a condition first!")
        input()

    print(f"length : {length}")
    print(f"exception : {exception}")
    print(f"strike : {strike}")
    print(f"ball : {ball}")
    print()

    candidate.clear()
    for i in range(len(dictionary)):
        if i%500 == 0: print(" %06.2f%% complete (%d out of %d)" %(100*i/(data-1), i, data-1), end = "\r")
        good = True
        if len(dictionary[i]) != length: good = False
        for j in range(len(exception)):
            if exception[j] in dictionary[i]: good = False
        for j in range(len(strike)):
            if strike[j][0] not in dictionary[i] or dictionary[i].index(strike[j][0]) != strike[j][1] - 1: good = False
        for j in range(len(ball)):
            if ball[j][0] not in dictionary[i] or dictionary[i].index(ball[j][0]) == ball[j][1] - 1: good = False

        if good: candidate.append(("".join(dictionary[i])).upper())
    os.system("cls")
exit