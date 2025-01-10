def brute_force_search(text, pattern):
    if not text or not pattern:
        return -1
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if pattern[j] != text[i + j]:
                break
        else:
            return i
    return -1


# def brute_force_search_recur(text, pattern, pos=0):
#     if not text or not pattern or len(text) < len(pattern):
#         return -1
#     for i in range(len(pattern)):
#         if pattern[i] != text[i]:
#             return brute_force_search_recur(text[1:], pattern, pos + 1)
#     return pos


if __name__ == '__main__':
    print(brute_force_search("", ""))
    print(brute_force_search("", "x"))
    print(brute_force_search("x", ""))
    print(brute_force_search("abcdxxxx", "abcy"))
    print(brute_force_search("xxxxabcd", "abcy"))
    print(brute_force_search("abcdxxxx", "abcd"))
    print(brute_force_search("xabcdxxx", "abcd"))
    print(brute_force_search("xxabcdxx", "abcd"))
    print(brute_force_search("xxxabcdx", "abcd"))
    print(brute_force_search("xxxxabcd", "abcd"))
    print(brute_force_search("aababcdabcx", "abcd"))
    print(brute_force_search("aababcdab cx", "b c"))

    # print(brute_force_search_recur("", ""))
    # print(brute_force_search_recur("", "x"))
    # print(brute_force_search_recur("x", ""))
    # print(brute_force_search_recur("abcdxxxx", "abcy"))
    # print(brute_force_search_recur("xxxxabcd", "abcy"))
    # print(brute_force_search_recur("abcdxxxx", "abcd"))
    # print(brute_force_search_recur("xabcdxxx", "abcd"))
    # print(brute_force_search_recur("xxabcdxx", "abcd"))
    # print(brute_force_search_recur("xxxabcdx", "abcd"))
    # print(brute_force_search_recur("xxxxabcd", "abcd"))
