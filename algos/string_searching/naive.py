# naive string search


def naive_ss(pattern, text):
    def check_equal(start, end):
        j = 0
        for i in range(start, end):
            if text[i] != pattern[j]:
                return False
            j += 1
        return True
    
    start = 0
    end = start + len(pattern)
    while end <= len(text):
        if check_equal(start, end):
            return start
            
        start += 1
        end += 1
    return None

