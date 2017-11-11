import math
from binary_search import binary_search


def adaptive_search(l, key, start=0, end=None, maxdepth=None):
    if end is None:
        end = len(l)
    if end <= start:
        return None
    
    if maxdepth is None:    
        maxdepth = math.log(end - start)
    adasearch_helper(l, start, end, maxdepth)


def adasearch_helper(l, start, end, depth):
    if end <= start:
        return None
    elif depth == 0:
        return binary_search(l, key, start, end)
    
    ratio = (end - start) / (l[end - 1] - l[start])
    guess = int(start + (key - l[start]) * ratio)
    if l[guess] > key:
        return adasearch_helper(l, key, start, guess, depth - 1)
    elif l[guess] < key:
        return adasearch_helper(l, key, guess + 1, end, depth - 1)
    else:
        return guess


if __name__ == "__main__":
    l = [-3.6, 0, 1, 2, 2, 2, 3, 3, 4, 11, 11.1, 11.1, 15, 15, 16, 22.3]
    print("list l is {}".format(l))
    print("(the list has to be sorted already " +
          "for adaptive search to work)")
    k = 11
    i = adaptive_search(l, k)
    if i is None:
        print("value {} was not found in l".format(k))
    else:
        print("value {} is placed at index {} in l".format(k, i))
