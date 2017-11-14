# a series of fibonacci variants


def fib_naive(n):
    if n <= 1:
        return n
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)


FIB_MEM = {0: 0, 1: 1}
def fib_memoised(n):
    if n not in FIB_MEM:
        FIB_MEM[n] = fib_memoised(n - 1) + fib_memoised(n - 2)

    return FIB_MEM[n]
    
    
FIB_FAST_MEM = {0: 0, 1: 1, 2: 1}
def fib_fast_mem(n):
    if n not in FIB_FAST_MEM:
        k = n // 2
        fk = fib_fast_mem(k)
        fkp1 = fib_fast_mem(k + 1)
        if n % 2 == 0:
            FIB_FAST_MEM[n] = fk * (2 * fkp1 - fk)
        else:
            FIB_FAST_MEM[n] = fkp1 ** 2 + fk ** 2
            
    return FIB_FAST_MEM[n]
    
        
def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        t = a
        a += b
        b = t
    return a
    

def fib_iter2(n):
    a = 0
    b = 1
    for i in range(n // 2):
        a += b
        b += a
        
    if n % 2 == 0:
        return a
    else:
        return b


def fib_fast(n):
    if n <= 1:
        return n
    
    a = 1
    b = 2
    k = 2
    while k <= n // 2:
        t = a * (2 * b - a)
        b = a ** 2 + b ** 2
        a = t                    
        k *= 2
    
    for k in range(k//2 + 1, n // 2 + 1):
        a += b
        b += a    
    if n % 2 == 0:
        return a
    else:
        return b    


from math import sqrt
SQRT5 = sqrt(5)
PHI = (1 + SQRT5) / 2
PSI = 1 - PHI  # also, - 1 / PHI
def fib_formula(n):
    return int((PHI**n - PSI**n) / SQRT5)


FIB_FORMULA_MEM = {}
def fib_formula_mem(n):
    if n not in FIB_FORMULA_MEM:
        if n < 72:
            FIB_FORMULA_MEM[n] = int((PHI**n - PSI**n) / SQRT5)
        else:
            k = n // 2
            fk = fib_formula_mem(k)
            fkp1 = fib_formula_mem(k + 1)
            if n % 2 == 0:
                FIB_FORMULA_MEM[n] = fk * (2 * fkp1 - fk)
            else:
                FIB_FORMULA_MEM[n] = fkp1 ** 2 + fk ** 2
    
    return FIB_FORMULA_MEM[n]
