from random import shuffle


def bogosort(l):
    while not is_sorted(l):
        shuffle(l)


def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True
