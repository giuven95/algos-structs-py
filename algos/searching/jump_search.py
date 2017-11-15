from math import sqrt


# the list has to be sorted already
def jump_search(l, key):
    start = 0
    end = len(l)
    
    right = int(sqrt(end))
    mid = min(right, end)
    while l[mid - 1] < key:
        start = right
        right += int(sqrt(end))
        mid = min(right, end)
        if end <= start:
            return None

    end = mid
    while l[start] < key:
        start += 1
        if end <= start:
            return None

    if l[start] == key:
        return start
    else:
        return None
