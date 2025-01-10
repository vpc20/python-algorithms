def kmp_search(text, pattern):
    if not pattern or not text:
        return -1

    prefix_table, prefval, j = [0], 0, -1
    for i in range(1, len(pattern)):
        j += 1
        if pattern[i] == pattern[j]:
            prefval += 1
        else:
            prefval = 0
            j = -1
        prefix_table.append(prefval)

    j = 0
    print(text)
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = prefix_table[j - 1]  # last matched char
        if j == 0:
            print(' ' * i + pattern)
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1


if __name__ == '__main__':
    # print(kmp_search('', ''))
    # print(kmp_search('', 'x'))
    # print(kmp_search('axxxx', ''))
    # print(kmp_search('axxxx', ' '))
    # print(kmp_search('axxxx', 'a'))
    # print(kmp_search('xaxxx', 'a'))
    # print(kmp_search('xxaxx', 'a'))
    # print(kmp_search('xxxax', 'a'))
    # print(kmp_search('xxxxa', 'a'))
    # print(kmp_search('abcxxx', 'abc'))
    # print(kmp_search('xabcxx', 'abc'))
    # print(kmp_search('xxabcx', 'abc'))
    # print(kmp_search('xxxabc', 'abc'))
    # print(kmp_search('a', 'a'))
    # print(kmp_search('a', 'abc'))

    print(kmp_search('acat acgacacagt', 'acacagt'))
    # idx      0  1  2  3  4  5  6
    # pattern  a  c  a  c  a  g  t
    # pfxtbl   0  0  1  2  3  0  0

    print(kmp_search('another simple example', 'example'))
