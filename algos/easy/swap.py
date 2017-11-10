# swaps the place of two elements in a list

def swap(l, i, j):
    t = l[i]
    l[i] = l[j]
    l[j] = t
