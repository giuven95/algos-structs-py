# knuth - morris - pratt string search


def kmp_ss(pattern, text):
    def prepare(pattern):
        jumps = [0]

        for i in range(1, len(pattern)):
            j = next_to_check(text, jumps, i, jumps[i - 1])
            jumps.append(j)
        return jumps
        
    def next_to_check(text, jumps, i, j):
        while j > 0 and text[i] != pattern[j]:
            j = jumps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        return j

    j = 0
    jumps = prepare(pattern)
    for i in range(len(text)):
        j = next_to_check(text, jumps, i, j)
        if j == len(pattern): 
            return i - j + 1
    return None
