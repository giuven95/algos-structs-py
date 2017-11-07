from swap import swap


def cocktail_sort(l):
    if len(l) < 2:
        return

    start = 0
    end = len(l)
    over = False
    while (not over) and end > start + 1:
        over = cocktail_sort_internal(l, start, end)
        end -= 1
        start += 1


def cocktail_sort_internal(l, start, end):
    flag = True
    for i in range(start, end - 1):
        if l[i] > l[i + 1]:
            swap(l, i, i + 1)
            flag = False
    for j in range(end - 1, start, -1):  # decreasing index
        if l[j] < l[j - 1]:
            swap(l, j, j - 1)
            flag = False
    return flag


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    cocktail_sort(l)
    print(l)
