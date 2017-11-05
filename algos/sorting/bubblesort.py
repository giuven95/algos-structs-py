from random import randint
from swap import swap


def bubblesort(l, start=0, end=None):
    if end is None:
        end = len(l)

    over = False
    while (not over) and end > start + 1:
        over = bubblesort_internal(l, start, end)
        end -= 1


def bubblesort_internal(l, start, end):
    flag = True
    for i in range(start, end - 1):
        if l[i] > l[i + 1]:
            swap(l, i, i + 1)
            flag = False
    return flag


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    bubblesort(l)
    print(l)
