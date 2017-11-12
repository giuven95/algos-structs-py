FIB = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
46368, 75025, 121393, 196418, 317811, 514229, 832040,
1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
24157817, 39088169, 63245986, 102334155, 165580141,
267914296, 433494437, 701408733, 1134903170, 1836311903]


def fibonacci_search(l, key):
    k = 0
    while FIB[k] < len(l): 
        k += 1
    
    if k == 0:
        return None
    else:
        return fibonacci_search_internal(l, key, 0, len(l), k - 1)


def fibonacci_search_internal(l, key, start, end, index):
    if index < 0:
        return None
   
    guess = start + FIB[index]
    if guess >= end or l[guess] > key:
        index -= 1
    elif l[guess] < key:
        start = guess + 1
        index -= 2
    else:  # l[guess] == key
        return guess
    
    return fibonacci_search_internal(l, key, start, end, index)
    

if __name__ == "__main__":
    l = [-3.6, 0, 1, 2, 2, 2, 3, 3, 4, 11, 11.1, 11.1, 15, 15, 16, 22.3]
    print("list l is {}".format(l))
    print("(the list has to be sorted already for fibonacci search to work)")
    k = 11
    i = fibonacci_search(l, k)
    if i is None:
        print("value {} was not found in l".format(k))
    else:
        print("value {} is placed at index {} in l".format(k, i))
