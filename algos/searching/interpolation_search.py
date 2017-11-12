def interpolation_search(l, key, start=0, end=None):
    if end is None:
        end = len(l)
    if end <= start:
        return None

    ratio = (end - start) / (l[end - 1] - l[start])
    guess = int(start + (key - l[start]) * ratio)
    if l[guess] > key:
        return interpolation_search(l, key, start, guess)
    elif l[guess] < key:
        return interpolation_search(l, key, guess + 1, end)
    else:
        return guess


l = [-3.6, 0, 1, 2, 2, 2, 3, 3, 4, 11, 11.1, 11.1, 15, 15, 16, 22.3]
print("list l is {}".format(l))
print("(the list has to be sorted already " +
      "for interpolation search to work)")
k = 11
i = interpolation_search(l, k)
if i is None:
    print("value {} was not found in l".format(k))
else:
    print("value {} is placed at index {} in l".format(k, i))
