from binary_search import binary_search


def exponential_search(l, key, start=0, end=None):
    if end is None:
        end = len(l)
    elif end <= start:
        return None

    i = start
    p = 1
    while i < end and l[i] < key:
        p *= 2
        i += p // 2  # equivalent to "i = start + p"

    if l[i] == key:
        return i
    else:
        return binary_search(l, key, i - p // 2, min(i, end))


if __name__ == "__main__":
    l = [-3.6, 0, 1, 2, 2, 2, 3, 3, 4, 11, 11.1, 11.1, 15, 15, 16, 22.3]
    print("list l is {}".format(l))
    print("(the list has to be sorted already for exponential search to work)")
    k = 11
    i = exponential_search(l, k)
    if i is None:
        print("value {} was not found in l".format(k))
    else:
        print("value {} is placed at index {} in l".format(k, i))
