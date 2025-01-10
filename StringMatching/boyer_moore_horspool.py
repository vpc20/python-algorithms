from string import printable


# def bmh_search(text, pattern):
#     text_len = len(text)
#     patt_len = len(pattern)
#
#     # create skip table, it tells you how many characters to skip if there is unmatched char
#     skip_table = {}
#     for ch in printable:
#         skip_table[ch] = patt_len
#     for i in range(patt_len - 1):
#         skip_table[pattern[i]] = patt_len - 1 - i
#
#     # start searching, matching is done from last char of pattern to the first
#     j = 0  # pointer to text
#     while j <= text_len - patt_len:
#         i = patt_len - 1  # pointer to pattern, find match backwards
#         while i > -1 and pattern[i] == text[j + i]:
#             i -= 1
#         if i == -1:
#             return j
#         j += skip_table[text[j + patt_len - 1]]
#
#     return -1


def bmh_search(text, pattern):
    if not text or not pattern:
        return -1

    skip_table = {}
    for ch in printable:
        skip_table[ch] = len(pattern)
    for j in range(len(pattern) - 1):
        skip_table[pattern[j]] = len(pattern) - 1 - j

    # start searching, matching is done from last char of pattern to the first
    i = 0  # pointer to text
    # print(text)
    # print(pattern)
    while i <= len(text) - len(pattern):
        for j in range(len(pattern) - 1, -1, -1):  # pointer to pattern
            if pattern[j] != text[i + j]:
                i += skip_table[text[i + len(pattern) - 1]]  # text character is the char
                # print(i * ' ' + pattern)
                break  # aligned with the last char in pattern
        else:
            return i
    return -1


if __name__ == '__main__':
    # print(bmh_search('', ''))
    # print(bmh_search('', 'x'))
    # print(bmh_search('axxxx', ''))
    # print(bmh_search('axxxx', ' '))
    # print(bmh_search('axxxx', 'a'))
    # print(bmh_search('xaxxx', 'a'))
    # print(bmh_search('xxaxx', 'a'))
    # print(bmh_search('xxxax', 'a'))
    # print(bmh_search('xxxxa', 'a'))
    # print(bmh_search('abcxxx', 'abc'))
    # print(bmh_search('xabcxx', 'abc'))
    # print(bmh_search('xxabcx', 'abc'))
    # print(bmh_search('xxxabc', 'abc'))
    # print(bmh_search('a', 'a'))
    # print(bmh_search('a', 'abc'))

    # print(bmh_search('toothx', 'tooth'))
    # print(bmh_search('xtooth', 'tooth'))
    # print(bmh_search('xtoothx', 'tooth'))
    # print bmh_search('abcqwaebrcyuio', 'abc')
    # print bmh_search('abc', 'abc')
    # print bmh_search('axabc', 'abc')
    # print bmh_search('axbxabc', 'abc')
    # print bmh_search('axbxcxabc', 'abc')
    # print bmh_search('aaaaabc', 'abc')
    # print bmh_search('abcdefghij', 'xxx')
    print(bmh_search('here is a simple example', 'example'))
    print(''.join([str(i) + ' ' * 9 for i in range(10)]))
    print('0123456789' * 10)
    #   0                                       1                                       2
    #   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
    # │ h │ e │ r │ e │   │ i │ s │   │ a │   │ s │ i │ m │ p │ l │ e │   │ e │ x │ a │ m │ p │ l │ e │
    # └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┐
    # │ e │ x │ a │ m │ p │ l │ e │
    # └───┴───┴───┴───┴───┴───┴───┘
    #                             ┌───┬───┬───┬───┬───┬───┬───┐
    #                             │ e │ x │ a │ m │ p │ l │ e │
    #                             └───┴───┴───┴───┴───┴───┴───┘
    #                                     ┌───┬───┬───┬───┬───┬───┬───┐
    #                                     │ e │ x │ a │ m │ p │ l │ e │
    #                                     └───┴───┴───┴───┴───┴───┴───┘
    #                                                             ┌───┬───┬───┬───┬───┬───┬───┐
    #                                                             │ e │ x │ a │ m │ p │ l │ e │
    #                                                             └───┴───┴───┴───┴───┴───┴───┘
    #                                                                     ┌───┬───┬───┬───┬───┬───┬───┐
    #                                                                     │ e │ x │ a │ m │ p │ l │ e │
    #                                                                     └───┴───┴───┴───┴───┴───┴───┘
