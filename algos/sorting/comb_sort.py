SHRINK_FACTOR = 1.3


def comb_sort(l):
    gap = len(l)
    over = False

    # notice: if the gap is greater than 1, we have to keep going
    # otherwise it depends on the "over" flag
    while gap > 1 and not over:
        gap = max(1, int(gap / SHRINK_FACTOR))
        over = comb_sort_internal(l, gap)


def comb_sort_internal(l, gap):
    flag = True  # True if the loop makes no swaps, otherwise False
    for i in range(len(l) - gap):
        if l[i] > l[i + gap]:
            l[i], l[i + gap] = l[i + gap], l[i]
            flag = False
    return flag
