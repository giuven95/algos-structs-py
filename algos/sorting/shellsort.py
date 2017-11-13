GAPS = [701, 301, 132, 57, 23, 10, 4, 1]


def shellsort(l, start=0, end=None):
    if end is None:
        end = len(l)

    gaps = GAPS[:]
    for gap in gaps:
        shellsort_internal(l, start, end, gap)


def shellsort_internal(l, start, end, gap):
    for mid in range(start + gap, end):
        t = l[mid]
        j = mid - gap
        while j >= start and l[j] > t:
            l[j + gap] = l[j]
            j -= gap
        l[j + gap] = t
