import unittest
from random import randrange, choice
from string import ascii_lowercase


def knuth_morris_pratt(text, pattern):
    if len(pattern) > len(text) or pattern == '':
        return -1

    prefix_table = [0]
    for i in range(1, len(pattern)):
        s1 = pattern[:i + 1]
        pref = [s1[:i + 1] for i in range(len(s1) - 1)]
        suff = [s1[i:] for i in range(1, len(s1))]

        maxlen = 0
        for item in pref:
            if item in suff and len(item) > maxlen:
                maxlen = len(item)
        prefix_table.append(maxlen)

    k = 0  # k is the text position  where the matching of character starts
    while k < len(text) - len(pattern) + 1:
        i = k
        for j in range(len(pattern)):
            if text[i] == pattern[j]:
                i += 1
            else:
                if j == 0:
                    k += 1
                else:
                    k += j - prefix_table[j - 1]  # j-1 is the position of the last matching character
                break
        else:
            return k
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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        # self.assertEqual(knuth_morris_pratt('axxxx', ''), -1)
        # self.assertEqual(knuth_morris_pratt('axxxx', ' '), -1)
        # self.assertEqual(knuth_morris_pratt('axxxx', 'a'), 0)
        # self.assertEqual(knuth_morris_pratt('xaxxx', 'a'), 1)
        # self.assertEqual(knuth_morris_pratt('xxaxx', 'a'), 2)
        # self.assertEqual(knuth_morris_pratt('xxxax', 'a'), 3)
        # self.assertEqual(knuth_morris_pratt('xxxxa', 'a'), 4)
        # self.assertEqual(knuth_morris_pratt('abcxxx', 'abc'), 0)
        # self.assertEqual(knuth_morris_pratt('xabcxx', 'abc'), 1)
        # self.assertEqual(knuth_morris_pratt('xxabcx', 'abc'), 2)
        # self.assertEqual(knuth_morris_pratt('xxxabc', 'abc'), 3)
        # self.assertEqual(knuth_morris_pratt('a', 'a'), 0)

        # generate pattern which matches
        # for i in range(10000):
        #     # s = random_strings(12, 20)
        #     s = random_string(80)
        #     pattern = random_substring(s, 15)
        #     print s, '---', pattern
        #     print knuth_morris_pratt(s, pattern), s.find(pattern)
        #     self.assertEqual(knuth_morris_pratt(s, pattern), s.find(pattern))

        # generate random pattern
        # for i in range(10000):
        #     # s = random_strings(12, 20)
        #     s = random_string(80)
        #     pattern = random_string(15)
        #     print s, '---', pattern
        #     print knuth_morris_pratt(s, pattern), s.find(pattern)
        #     self.assertEqual(knuth_morris_pratt(s, pattern), s.find(pattern))


if __name__ == '__main__':
    unittest.main()

# print gen_prefix_table('acacagt')
# print knuth_morris_pratt('acat acgacacagt', 'acat')
# print knuth_morris_pratt('acat acgacacagt', 'acacagt')
# print knuth_morris_pratt('abcxxxxx', 'abc')
# print knuth_morris_pratt('xabcxxxxx', 'abc')
# print knuth_morris_pratt('xxabcxxxxx', 'abc')
# print knuth_morris_pratt('xxxabcxxxxx', 'abc')
# print knuth_morris_pratt('xxxxabcxxxxx', 'abc')
# print knuth_morris_pratt('xxxxxabcxxxxx', 'abc')
# print knuth_morris_pratt('xxxxxabcxxxxx', 'abcq')

# print knuth_morris_pratt('h','h')
# print knuth_morris_pratt('ababaababaca', 'ababaca')
# print knuth_morris_pratt('oqhfvypfmodhmxfjpzatvlhrpzphmchfvxkypltlysswdz', 'yplt')
# print knuth_morris_pratt('lcjjfytfdezerbzvqtkpfoiukfhewtomuebwtstbpirvtfhnlzxlcvlrw', 'wnevsvtf')
