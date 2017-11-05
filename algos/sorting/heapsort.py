from swap import swap


def heapsort(l, start=0, end=None):
    if end is None:
        end = len(l)

    if end < start + 2:
        return

    heapify(l, start, end)

    while end >= start + 1:
        swap(l, start, end - 1)
        end -= 1  # very important
        sift_down(l, start, end)


def heapify(l, start, end):
    j = end - 1
    while j >= start:
        sift_down(l, j, end)
        j -= 1


def sift_down(l, start, end):
    j = start
    cch = choose_child(l, start, end, j)
    while cch < end and l[j] < l[cch]:
        swap(l, cch, j)
        j = cch
        cch = choose_child(l, start, end, j)


def choose_child(l, start, end, j):
    ch1 = start + 2 * (j - start) + 1
    ch2 = start + 2 * (j - start) + 2
    if ch2 >= end or l[ch1] > l[ch2]:
        return ch1
    else:
        return ch2


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    heapsort(l)
    print(l)
