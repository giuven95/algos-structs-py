# knuth - morris - pratt algo
####### WORK IN PROGRESS !!!

def kmp(pattern, text):
    def prepare(pattern):
        i = 1
        plen = len(pattern)
        steps = [1] * end
        while start < end:
            k = last_equal(pattern, pattern, i, plen)
            steps[i] = i - k + 1
            i += steps[k]
        return steps
    
    def last_equal(pattern, text, start, end)
        j = 0
        for i in range(start, end):
            if text[i] != pattern[j]:
                break
            j += 1
        return j + 1
    
    start = 0    
    plen = len(pattern)
    tlen = len(text)
    steps = prepare(pattern)
    while start + plen <= tlen:
        k = last_equal(pattern, text, start, start + plen)
        if k == plen:
            return start
        start += steps[k]
    return None
