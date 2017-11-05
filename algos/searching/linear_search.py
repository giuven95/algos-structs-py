def linear_search(l, key, start=0, end=None):
    if end is None:
        end = len(l)

    for i in range(start, end):
        if l[i] == key:
            return i
    return None


if __name__ == "__main__":
    l = [-3.6, 22.3, 1, 2, 3, 4, 2, 15, 15, 11, 2, 16, 3, 11.1, 11.1, 0]
    print("list l is {}".format(l))
    k = 11
    i = linear_search(l, k)
    if i is None:
        print("value {} was not found in l".format(k))
    else:
        print("value {} is placed at index {} in l".format(k, i))
