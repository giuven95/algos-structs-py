from math import sqrt


# the list has to be sorted already
def jump_search(l, key, start=0, end=None):
    if end is None:
        end = len(l)
    if end <= start:
        return None

    if l[start] == key:
        return start
    start += 1    

    right = start + int(sqrt(end - start))
    mid = min(right, end)
    if l[mid - 1] < key:
        return jump_search(l, key, mid, end)

    end = mid
    while start < end and l[start] < key:
        start += 1
    return jump_search(l, key, start, end)
