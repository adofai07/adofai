import glob
import time
import sys

print = sys.stdout.write

def backtrack(dirname, step = 0, disc = "", force_print = True, delay = 0.5):

    filename = "  "*step + dirname.split("\\")[-1]

    if force_print:
        if disc != "" and disc in filename and len(glob.glob(dirname + "\\*")) == 0:
            print("\033[38;2;0;255;0m" + filename + "\033[38;2;255;255;255m\n")
            if delay >= 0: time.sleep(delay)
            else: input()

        else:
            print(filename + "\n")
    
    else:
        if disc != "" and disc in dirname:
            print(dirname + "\n")


    for d in glob.glob(dirname + "\\*"):
        try:
            backtrack(d, step = step + 1, disc = disc, force_print = force_print, delay = delay)
        except:
            continue
    
    return

backtrack(r"C:\Users\chldm\OneDrive\바탕 화면\서울과학고\기타\정민건\이동원 USB", step = 4, disc = ".cpp", delay = 0, force_print = True)
