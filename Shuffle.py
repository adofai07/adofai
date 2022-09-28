import random

def shuffle(word):
    if len(word) <= 3: return word

    mid = list(word[1:-1])
    random.shuffle(mid)

    return word[0] + "".join(mid) + word[-1]

while True:
    sentence = input("\033[38;2;255;255;255m").split()
    print("\033[38;2;0;150;255m" + " ".join(map(shuffle, sentence)))