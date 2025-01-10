# CLRS version
# import unittest
from random import randrange, choice
from string import ascii_lowercase, printable


def compute_prefix_function(pattern):
    prefix_table = [0] * len(pattern)
    prefix_table[0] = 0
    k = 0
    for i in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix_table[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        prefix_table[i] = k
    return prefix_table


def kmp_matcher(text, pattern):
    prefix_table = compute_prefix_function(pattern)
    q = 0
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = prefix_table[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            return i - len(pattern) + 1
    return -1


def random_substring(s, maxlen):
    while True:
        if len(s) == 1:
            return s[0]
        start = randrange(len(s) - 1)
        end = start + randrange(maxlen + 1)
        if start != end:
            return s[start:end]


def random_strings(maxlen, maxoccur):
    return ' '.join([random_string(maxlen) for i in range(randrange(1, maxoccur + 1))])


def random_string(maxlen):
    return ''.join([choice(ascii_lowercase) for i in range(randrange(1, maxlen + 1))])


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)
#         # self.assertEqual(kmp_matcher('axxxx', ''), -1)
#         # self.assertEqual(kmp_matcher('axxxx', ' '), -1)
#         # self.assertEqual(kmp_matcher('axxxx', 'a'), 0)
#         # self.assertEqual(kmp_matcher('xaxxx', 'a'), 1)
#         # self.assertEqual(kmp_matcher('xxaxx', 'a'), 2)
#         # self.assertEqual(kmp_matcher('xxxax', 'a'), 3)
#         # self.assertEqual(kmp_matcher('xxxxa', 'a'), 4)
#         # self.assertEqual(kmp_matcher('abcxxx', 'abc'), 0)
#         # self.assertEqual(kmp_matcher('xabcxx', 'abc'), 1)
#         # self.assertEqual(kmp_matcher('xxabcx', 'abc'), 2)
#         # self.assertEqual(kmp_matcher('xxxabc', 'abc'), 3)
#         # self.assertEqual(kmp_matcher('a', 'a'), 0)
#
#         # generate pattern which matches
#         # for i in range(10000):
#         #     # s = random_strings(12, 20)
#         #     s = random_string(80)
#         #     pattern = random_substring(s, 15)
#         #     print s, '---', pattern
#         #     print kmp_matcher(s, pattern), s.find(pattern)
#         #     self.assertEqual(kmp_matcher(s, pattern), s.find(pattern))
#
#         # generate random pattern
#         # for i in range(10000):
#         #     # s = random_strings(12, 20)
#         #     s = random_string(80)
#         #     pattern = random_string(15)
#         #     print s, '---', pattern
#         #     print kmp_matcher(s, pattern), s.find(pattern)
#         #     self.assertEqual(kmp_matcher(s, pattern), s.find(pattern))
#
#
# if __name__ == '__main__':
#     unittest.main()

# print(gen_prefix_table('acacagt'))
# print(kmp_matcher('acat acgacacagt', 'acat'))
print(kmp_matcher('acat acgacacagt', 'acacagt'))

# print kmp_matcher('abcxxxxx', 'abc')
# print kmp_matcher('xabcxxxxx', 'abc')
# print kmp_matcher('xxabcxxxxx', 'abc')
# print kmp_matcher('xxxabcxxxxx', 'abc')
# print kmp_matcher('xxxxabcxxxxx', 'abc')
# print kmp_matcher('xxxxxabcxxxxx', 'abc')
# print kmp_matcher('xxxxxabcxxxxx', 'abcq')

# print kmp_matcher('h', 'h')
# print kmp_matcher('ababaababaca', 'ababaca')
# print kmp_matcher('oqhfvypfmodhmxfjpzatvlhrpzphmchfvxkypltlysswdz', 'yplt')
# print kmp_matcher('lcjjfytfdezerbzvqtkpfoiukfhewtomuebwtstbpirvtfhnlzxlcvlrw', 'wnevsvtf')
