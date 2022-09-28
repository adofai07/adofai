import markdown
import datetime
import os

def print_task(tasks):
    max_len = [0, 0, 0]

    print("\n\033[38;2;255;0;255m" + "-"*((os.get_terminal_size()[0]-14)//2) + " List of tasks " + "-"*((os.get_terminal_size()[0]-15)//2) + "\033[38;2;255;255;255m")

    for i in range(len(tasks)):
        for j in range(3):
            max_len[j] = max(max_len[j], len(tasks[i][j+1]))

    f = open(path, "w")
    
    f.write("# Homework" + "\n")
    f.write("" + "\n")
    f.write("**Assignments are sorted by:**" + "\n")
    f.write("&nbsp;&nbsp;&nbsp;&nbsp;1. Due date." + "\n")
    f.write("&nbsp;&nbsp;&nbsp;&nbsp;2. Subject name." + "\n")
    f.write("&nbsp;&nbsp;&nbsp;&nbsp;3. Assignment name." + "\n")
    f.write("" + "\n")
    f.write("| No. | Subject | Assignment(s) | Due |" + "\n")
    f.write("|:---|:---|:---|:---|" + "\n")

    for i in range(len(tasks)):
        print(tasks[i][0], end = "\033[38;2;127;127;127m|    \033[38;2;255;0;0m")
        print((tasks[i][1] + " "*max_len[0])[:max_len[0]], end = "    \033[38;2;0;255;0m")
        print((tasks[i][2] + " "*max_len[1])[:max_len[1]], end = "    \033[38;2;0;0;255m")
        print((tasks[i][3] + " "*max_len[2])[:max_len[2]], end = "    \033[38;2;255;255;255m")
        print()

        f.write(" | ".join(f"`{tasks[i][j]}`" for j in range(4)) + "\n")

    f.close()
    
    print()

path = "C:/Users/chldm/OneDrive/바탕 화면/서울과학고/codes/Markdown/Homework.md"

f = open(path, "r")
markdown = markdown.markdown(f.read()).split("\n")
f.close()
markdown = markdown[markdown.index("|:---|:---|:---|:---|")+1:]


tasks = []

for i in range(len(markdown)):
    temp = markdown[i].split(" | ")
    for j in range(4):
        temp[j] = temp[j][6:-7]
    if i == len(markdown)-1: temp[3] = temp[3][:-4]
    tasks.append(temp)

current_date = datetime.datetime.today().strftime("%Y-%m-%d")

print(tasks)

while len(tasks) > 0 and tasks[0][3] < current_date:
    tasks.pop(0)

while True:
    for i in range(len(tasks)):
        tasks[i][0] = "{:03.0f}".format(i+1)
        
    print_task(tasks)
    # print(tasks)

    while True:
        userinput = input("\033[38;2;255;127;0mEnter \"+\" to append, \"-\" to delete >> ")
        if userinput in ["+", "-"]: break

    if userinput == "+":
        tasks.append([
            "000",
            input("\033[38;2;255;127;0mEnter subject >> \033[38;2;0;255;255m"),
            input("\033[38;2;255;127;0mEnter homework >> \033[38;2;0;255;255m"),
            input("\033[38;2;255;127;0mEnter due date >> \033[38;2;0;255;255m")
        ])
        tasks.sort(key = lambda x: x[3] + x[1] + x[2])
    else:
        temp = list(map(int, input("\033[38;2;255;127;0mEnter number(s) >> \033[38;2;0;255;255m").split()))
        for i in reversed(sorted(temp)):
            tasks.pop(i-1)