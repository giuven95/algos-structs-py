from random import randint
from swap import swap
from quickpartition import hoare_partition


def quicksort(l, start=0, end=None):
    if end is None:
        end = len(l)
    
    if end < start + 2:
        return
            
    bls = hoare_partition(l, start, end)
    quicksort(l, start, bls)
    quicksort(l, bls + 1, end)


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    quicksort(l)
    print(l)
