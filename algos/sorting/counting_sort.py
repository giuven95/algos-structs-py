from numpy import zeros


def counting_sort(l, start=0, end=None):
    if end is None:
        end = len(l)
    if end < start + 2:
        return

    min_value = l[0]
    max_value = l[1]
    for key in l:
        if key > max_value:
            max_value = key
        if key < min_value:
            min_value = key

    size = max_value - min_value + 1
    count = zeros(size, dtype=int)
    for key in l:
        i = key - min_value
        count[i] += 1

    tot = 0
    for i in range(size):
        old = count[i]
        count[i] = tot
        tot += old

    old_list = l[:]
    for key in old_list:
        i = key - min_value
        l[count[i]] = key
        count[i] += 1


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    counting_sort(l)
    print(l)
