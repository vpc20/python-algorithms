import unittest
from random import randrange, choice
from string import ascii_lowercase, printable


# bad character heuristics check only
def bm_search(text, pattern):
    # create bad char table, will be used to compute for skip value
    badch_table = {}
    for ch in printable:
        badch_table[ch] = -1
    for j in range(len(pattern)):
        badch_table[pattern[j]] = j
    for key, val in badch_table.items():
        if key in pattern:
            print(key, val)

    # start searching, matching is done from left to right of pattern
    print(''.join([str(int(i / 10)) if i % 10 == 0 else ' ' for i in range(100)]))
    print(''.join([str(i) for i in range(10)]) * 10)
    print(text)
    print(pattern)
    i = 0  # pointer to text
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # pointer to pattern, find match backwards
        while j > -1 and pattern[j] == text[i + j]:
            j -= 1
        if j == -1:
            return i
        i += max(1, j - badch_table[text[i + j]])
        print(' ' * i + pattern)
    return -1


def random_substring(s, maxlen):
    while True:
        if len(s) == 1:
            return s[0]
        start = randrange(len(s) - 1)
        end = start + randrange(maxlen + 1)
        if start != end:
            return s[start:end]


# def random_strings(maxlen, maxoccur):
#     return ' '.join([random_string(maxlen) for i in range(randrange(1, maxoccur + 1))])
#
#
# def random_string(maxlen):
#     return ''.join([choice(ascii_lowercase) for i in range(randrange(1, maxlen + 1))])
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)
#
#         # generate pattern which matches
#         for i in range(100):
#             s = random_string(80)
#             pattern = random_substring(s, 15)
#             print(s, '---', pattern)
#             print(boyer_moore_search(s, pattern), s.find(pattern))
#             self.assertEqual(boyer_moore_search(s, pattern), s.find(pattern))
#
#
#         # generate random pattern
#         for i in range(100):
#             s = random_string(80)
#             pattern = random_string(15)
#             print(s, '---', pattern)
#             print(boyer_moore_search(s, pattern), s.find(pattern))
#             self.assertEqual(boyer_moore_search(s, pattern), s.find(pattern))
#
#
# if __name__ == '__main__':
#     unittest.main()

# print(bm_search('toothx', 'tooth'))
# print(bm_search('xtooth', 'tooth'))
# print(bm_search('xtoothx', 'tooth'))
print(bm_search('here is a simple example', 'example'))

# print bmh_search('abcqwaebrcyuio', 'abc')
# print bmh_search('abc', 'abc')
# print bmh_search('axabc', 'abc')
# print bmh_search('axbxabc', 'abc')
# print bmh_search('axbxcxabc', 'abc')
# print bmh_search('aaaaabc', 'abc')
# print bmh_search('abcdefghij', 'xxx')
#

#                           1         2         3         4         5
#                 01234567890123456789012345678901234567890123456789012345
# print bmh_search('e enbsrdvjlxd rd uybstrbhqaem gvhr j a h khkcsrbbcma hoo', 'cma h')
#                                                    cma h
#                                                    01234

#                 0         1         2         3         4         5         6         7         8         9
#                 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# print bmh_search('xll j kmsygkla rjgqggkzfrwgz teeabde fekepxwyshz zqa thyyjqojyd u npmvumlcgvtq', 'np')
#                                                                                  np

#                 0         1         2         3         4         5         6         7         8         9
#                 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# print bmh_search('yrnwcn xqkxauko sobbxjhy hqshxdnyvxl ge dfzamsku hdlgez vryeprfbjoz pmk x', 'jlbxphtrbx')
#                            jlbxphtrbx
#                            0123456789


# print bmh_search('av myfcfcuz acxlhh yzfhiowobu rlkeeix usomx xx apzwqsj pvn t', 'xfdozjnadi')


#                 0         1         2         3         4         5         6         7         8         9
#                 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# print bmh_search('tpl wyt t l d vsv z hp xhx j', 'vsv')
#                               vsv
#                               012

#                 0         1         2         3         4         5         6         7         8         9
#                 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# print bmh_search('xi sbbskn f dbyoinuq vdorruq kjm wbwpwwp owpdfz acuuswfs zq', 'wp owp')
#                                                     wp owp
#                                                     012345

# print bmh_search('671111091113298117115999711432117110973297103117106973210111032117110321129710697114', '11110911132')
# print boyer_moore_search('neenleasdfqweneedle', 'needle')
#                            needle
#                            012345 i                   2
#                            012345 bad_char_table  n = 0

# i - table
