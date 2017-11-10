def naive_string_search(pattern, text):
    def check_equal(pattern, text, start, end):
        j = 0
        for i in range(start, end):
            if text[i] != pattern[j]:
                return False
            j += 1
        return True
    
    start = 0    
    plen = len(pattern)
    tlen = len(text)
    while start + plen <= tlen:
        if check_equal(pattern, text, start, start + plen):
            return start
        start += 1
    return None

