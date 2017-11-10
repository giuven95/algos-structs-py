# knuth - morris - pratt algo
# WORK IN PROGRESS

def kmp(pattern, text):
    def prepare(pattern):
        end = len(pattern)
        jumps = [1] * end
        for i in range(1,len(pattern)):
            k = last_equal(pattern, pattern, i, end-i)
            jumps[i] = i - k + 1
        return jumps
    
    def last_equal(pattern, text, start, end)
        j = 0
        for i in range(start, end):
            if text[i] != pattern[j]:
                break
            j += 1
        return j
    
    start = 0    
    plen = len(pattern)
    tlen = len(text)
    jumps = prepare(pattern)
    while start + plen <= tlen:
        k = last_equal(pattern, text, start, start + plen)
        if k == plen:
            return start
        start += jumps[k]
    return None
#
