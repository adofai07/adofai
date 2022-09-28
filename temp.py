import os

# os.system("Rundll32.exe user32.dll, LockWorkStation")

def QuickSort(array):
    if len(array) <= 1: return array

    pivot = array[len(array) // 2]

    smaller, equal, bigger = [], [], []

    for element in array:
        if element < pivot: smaller.append(element)
        elif element == pivot: equal.append(element)
        else: bigger.append(element)
    
    return (
        QuickSort(smaller) +
        equal + 
        QuickSort(bigger)
    )