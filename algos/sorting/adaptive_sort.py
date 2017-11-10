import math
from quickpartition import hoare_partition
from heapsort import heapsort
from insertionsort import insertionsort


def adaptive_sort(l, start=0, end=None, maxdepth=None):
    if end is None:
        end = len(l)
    if maxdepth is None:
        maxdepth = math.log(end - start)
    adasort_helper(l, start, end, maxdepth)


def adasort_helper(l, start, end, depth):
    if end <= start + 16:
        insertionsort(l, start, end)
    elif depth == 0:
        heapsort(l, start, end)
    else:
        bls = hoare_partition(l, start, end)
        adasort_helper(l, start, bls, depth - 1)
        adasort_helper(l, bls + 1, end, depth - 1)


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    adaptive_sort(l)
    print(l)
