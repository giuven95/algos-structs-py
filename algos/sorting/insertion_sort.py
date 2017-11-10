def insertion_sort(l, start=0, end=None):
    if end is None:
        end = len(l)

    for mid in range(start + 1, end):
        t = l[mid]
        j = mid - 1
        while j >= start and l[j] > t:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = t


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    insertion_sort(l)
    print(l)
