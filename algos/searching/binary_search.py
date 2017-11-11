def binary_search(l, key, start=0, end=None):
    if end is None:
        end = len(l)
    if end <= start:
        return None

    mid = (start + end) // 2
    if l[mid] > key:
        return binary_search(l, key, start, mid)
    elif l[mid] < key:
        return binary_search(l, key, mid + 1, end)
    else:
        return mid


if __name__ == "__main__":
    l = [-3.6, 0, 1, 2, 2, 2, 3, 3, 4, 11, 11.1, 11.1, 15, 15, 16, 22.3]
    print("list l is {}".format(l))
    print("(the list has to be sorted already for binary search to work)")
    k = 11
    i = binary_search(l, k)
    if i is None:
        print("value {} was not found in l".format(k))
    else:
        print("value {} is placed at index {} in l".format(k, i))
