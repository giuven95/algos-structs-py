from swap import swap


def selection_sort(l):
    start = 0
    end = len(l)
    while end - start >= 2:
        imin = select_argmin(l, start, end)
        swap(l, start, imin)
        start += 1


def select_argmin(l, start, end):
    imin = start
    for j in range(start + 1, end):
        if l[j] < l[imin]:
            imin = j
    return imin


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    selection_sort(l)
    print(l)
