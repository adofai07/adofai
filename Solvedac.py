import os
import time
from urllib import request

global COLORS

null = None

NAMES = {
    "최은호": "adofai",
    "정민건": "math_rabbit_1028",
    "이동원": "dongwondavid",
    "구동현": "physics07",
    "정현우": "andyjung2104",
    "박상훈": "qwerasdfzxcl",
    "반딧불": "79brue",
    "이태윤": "taeyun149",
    "김주혁": "kimjoohyuk420",
    "최민종": "minpaper",
    "최건": "seagram",
    "구사과": "koosaga"
}

rating_numbers = {
    0: "Unrated   ",
    1: "Bronze 5  ",
    2: "Bronze 4  ",
    3: "Bronze 3  ",
    4: "Bronze 2  ",
    5: "Bronze 1  ",
    6: "Silver 5  ",
    7: "Silver 4  ",
    8: "Silver 3  ",
    9: "Silver 2  ",
    10: "Silver 1  ",
    11: "Gold 5    ",
    12: "Gold 4    ",
    13: "Gold 3    ",
    14: "Gold 2    ",
    15: "Gold 1    ",
    16: "Platinum 5",
    17: "Platinum 4",
    18: "Platinum 3",
    19: "Platinum 2",
    20: "Platinum 1",
    21: "Diamond 5 ",
    22: "Diamond 4 ",
    23: "Diamond 3 ",
    24: "Diamond 2 ",
    25: "Diamond 1 ",
    26: "Ruby 5    ",
    27: "Ruby 4    ",
    28: "Ruby 3    ",
    29: "Ruby 2    ",
    30: "Ruby 1    ",
    31: "Master    "
}

COLORS = [
"\033[38;2;40;40;40m",
"\033[38;2;120;53;19m",
"\033[38;2;175;175;175m",
"\033[38;2;255;180;0m",
"\033[38;2;0;255;170m",
"\033[38;2;0;230;255m",
"\033[38;2;255;5;76m",
"\033[38;2;100;50;150m"
]

def pad(string, length):
    for i in str(string):
        if ord("가") <= ord(i) <= ord("힣"): length -= 2
        else: length -= 1
    return str(string) + " " * (max(0, length))

def color(tier):
    if tier <= 0: return COLORS[0]
    if tier <= 5: return COLORS[1]
    if tier <= 10: return COLORS[2]
    if tier <= 15: return COLORS[3]
    if tier <= 20: return COLORS[4]
    if tier <= 25: return COLORS[5]
    if tier <= 30: return COLORS[6]
    return COLORS[7]

def get_score(score):
    bounds = [
    0,
    30, 60, 90, 120, 150,
    200, 300, 400, 500, 650,
    800, 950, 1100, 1250, 1400,
    1600, 1750, 1900, 2000, 2100,
    2200, 2300, 2400, 2500, 2600,
    2700, 2800, 2850, 2900, 2950,
    3000
    ]

    if score >= 3000:
        return (score - 3000, " ? ")
    
    if score < 30:
        return (" ? ", 30 - score)

    for i in range(1, len(bounds) - 1):
        if bounds[i] <= score < bounds[i+1]:
            return (score - bounds[i], bounds[i+1] - score)

os.system("cls")

for name, nickname in NAMES.items():
    print(f"Searching for {name}'s stats...", end = "\r")

    for trial in range(1000):

        try:
            response = request.urlopen(f"https://solved.ac/profile/{nickname}")
            page, sb = response.read().decode("utf-8"), "{"
            for i in range(page.index("\"ratingBySolvedCount\""), 0, -1):
                if page[i:i+13] == "\"solvedCount\"": break
            for i in range(i, len(page)):
                sb += page[i]
                if page[i] == "}": break
            stats = eval(sb)
            if "ratingByVoteCount" not in stats: stats["ratingByVoteCount"] = 0

            print("{name} [{COLOR}{nickname}{WHITE}] -> {COLOR}{rank}{WHITE} ({COLOR2}{prev}{WHITE} <- {COLOR}{rating}{WHITE} -> {COLOR3}{next}{WHITE}) EXP: {COLOR}{exp}{WHITE}".format(
                name = pad(name, 8),
                nickname = pad(nickname, max([len(i) for i in NAMES.values()])),
                rank = rating_numbers[stats["tier"]],
                rating = str(stats["rating"]).zfill(4),
                exp = "{:,}".format(stats["exp"]).replace(",", " ").rjust(14, " "),
                COLOR = color(stats["tier"]),
                WHITE = "\033[38;2;255;255;255m",
                prev = str(get_score(stats["rating"])[0]).zfill(3),
                next = str(get_score(stats["rating"])[1]).zfill(3),
                COLOR2 = color(stats["tier"]-1),
                COLOR3 = color(stats["tier"]+1)
            ))

            break
        except: ...

        wait = (trial+1)**2 * 5

        start_time = time.time()

        while time.time() - start_time < wait:
            print("Failed to fetch data: Please wait for {:05.1f}".format(wait + start_time - time.time()), end = "\r")

        print(" " * os.get_terminal_size()[0], end = "\r")

print()
