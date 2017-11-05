def mergesort(l, start=0, end=None):
    if end is None:
        end = len(l)

    if end < start + 2:
        return

    mid = (start + end) // 2
    a = l[start:mid]  # sublist up to mid EXCLUDED
    b = l[mid:end]  # sublist up to mid INCLUDED

    mergesort(a)
    mergesort(b)
    l[start:end] = sortmerge(a, b)


def sortmerge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1
    return c


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    mergesort(l)
    print(l)
