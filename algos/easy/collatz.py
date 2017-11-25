def collatz(n):
    def _collatz(n):
        print(n)
        
        if n == 1:
            return 1
        elif n % 2 == 0:
            return _collatz(n // 2)
        else:
            return _collatz(3 * n + 1)
            
    if n < 1:
        raise Exception("Integer n must be >= 1")    
    else:
        return _collatz(int(n))
    
    
COLLATZ_MEM = {1: 1} 
def collatz_mem(n):
    def _collatz_mem(n):
        print(n)
        
        if n not in COLLATZ_MEM:
            if n % 2 == 0:
                COLLATZ_MEM[n] = _collatz_mem(n // 2)
            else:
                COLLATZ_MEM[n] = _collatz_mem(3 * n + 1)

        return COLLATZ_MEM[n]
        
    if n < 1:
        raise Exception("Integer n must be >= 1")
    else:
        return _collatz_mem(int(n))


def collatz_iter(n):
    if n < 1:
        raise Exception("Integer n must be >= 1")
    
    print(n)    
    while (n != 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        
    return n
