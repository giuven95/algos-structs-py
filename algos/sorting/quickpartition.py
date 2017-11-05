from swap import swap


def lamuto_partition(l, start, end):
    p = m3pivot(l, start, end)
    swap(l, p, end - 1)

    pval = l[end - 1]
    bls = start
    for i in range(start, end - 1):
        if l[i] < pval:
            swap(l, i, bls)
            bls += 1

    swap(l, bls, end - 1)
    return bls


def hoare_partition(l, start, end):
    p = m3pivot(l, start, end)
    swap(l, p, end - 1)

    pval = l[end - 1]
    bls = start
    agr = end - 2

    while True:
        while l[bls] < pval:
            bls += 1
        while l[agr] > pval:
            agr -= 1

        if bls >= agr:
            break
        else:
            swap(l, bls, agr)
            bls += 1
            agr -= 1

    swap(l, bls, end - 1)
    return bls


def m3pivot(l, start, end):
    mid = (start + end) // 2  # integer division
    if l[start] > l[end - 1]:
        swap(l, start, end - 1)
    if l[start] > l[mid]:
        swap(l, start, mid)
    if l[mid] > l[end - 1]:
        swap(l, mid, end - 1)
    return mid


if __name__ == "__main__":
    l = [8, 8, 8, 8, 16, 8, 8, 0, 0, 8, 8, 8,
         8, 12, 8, 8, 1, 8, 8, 8, 2, 3, 8, 15]
    partition(l, 0, len(l))
    print(l)
