from swap import swap


def biselection_sort(l):
    start = 0
    end = len(l)
    while end - start >= 2:
        (imin, imax) = select_extremes(l, start, end)

        swap(l, imin, start)
        if l[imax] < l[imin]:  # very important!
            imax = imin
        swap(l, imax, end - 1)

        start += 1
        end -= 1


def select_extremes(l, start, end):
    imin = start
    imax = start
    for j in range(start + 1, end):
        if l[j] < l[imin]:
            imin = j
        elif l[j] >= l[imax]:  # not >, >= ---> keeps it a stable sort
            imax = j
    return (imin, imax)


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    biselection_sort(l)
    print(l)
