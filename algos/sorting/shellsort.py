from random import randint
from swap import swap


GAPS = [701, 301, 132, 57, 23, 10, 4, 1]


def shellsort(l, start=0, end=None):
    if end is None:
        end = len(l)

    gaps = GAPS[:]
    for gap in gaps:
        shellsort_internal(l, start, end, gap)


def shellsort_internal(l, start, end, gap):
    for mid in range(start + gap, end):
        t = l[mid]
        j = mid - gap
        while j >= start and l[j] > t:
            l[j + gap] = l[j]
            j -= gap
        l[j + gap] = t


l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
     22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
     19, 18, 15, 14, 81, 83, 85, 87, 89]
shellsort(l)
print(l)
