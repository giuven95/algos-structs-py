def stooge_sort(l, start=0, end=None):
    if end is None:
        end = len(l)
    if end < start + 2:
        return

    if l[start] > l[end - 1]:
        l[start], l[end - 1] = l[end - 1], l[start]
    if end >= start + 3:
        i = (end - start) // 3
        stooge_sort(l, start, end - i)
        stooge_sort(l, start + i, end)
        stooge_sort(l, start, end - i)
