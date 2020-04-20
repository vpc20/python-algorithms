# import string
import unittest
from random import randrange, choice
from string import ascii_lowercase, printable


def boyer_moore_search(text, pattern):
    len_text = len(text)
    len_pattern = len(pattern)
    text_pos = len_pattern - 1  # starting point
    pattern_pos = len_pattern - 1
    start_text_pos = text_pos

    while text_pos < len_text:
        pattern_pos = len_pattern - 1
        while pattern_pos > -1:
            if pattern[pattern_pos] == text[text_pos]:
                pattern_pos -= 1
                text_pos -= 1
            else:
                unmatched_char = text[text_pos]
                pattern_pos -= 1
                start_pattern_pos = pattern_pos
                while pattern_pos > -1:
                    if pattern[pattern_pos] == unmatched_char:
                        break
                    else:
                        pattern_pos -= 1
                jump = start_pattern_pos - pattern_pos + 1
                break
        else:
            return text_pos + 1
        start_text_pos += jump
        text_pos = start_text_pos
    return -1


def random_string(maxlen):
    return ''.join([choice(ascii_lowercase) for i in range(randrange(1, maxlen + 1))])


def random_strings(maxlen, maxoccur):
    return ' '.join([random_string(maxlen) for i in range(randrange(1, maxoccur + 1))])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        # generate pattern which matches
        for i in range(10000):
            s = random_strings(12, 10)
            patt_len = randrange(1, 10)
            # print 's', s
            # print 'len(s)', len(s)
            # print 'patt_len', patt_len
            if patt_len >= len(s):
                continue
            patt_idx = randrange(len(s) - patt_len)
            pattern = s[patt_idx:patt_idx + patt_len]
            pattern = pattern.strip()
            if s and pattern:
                print(s, '---', pattern)
                print(boyer_moore_search(s, pattern), s.find(pattern))
                self.assertEqual(boyer_moore_search(s, pattern), s.find(pattern))

        # generate random pattern
        for i in range(10000):
            s = random_strings(12, 10)
            pattern = random_string(10)
            print(s, '---', pattern)
            print(boyer_moore_search(s, pattern), s.find(pattern))
            self.assertEqual(boyer_moore_search(s, pattern), s.find(pattern))


if __name__ == '__main__':
    unittest.main()

# print boyer_moore_search("abcdxxxx", "abcd")
# print boyer_moore_search("xabcdxxx", "abcd")
# print boyer_moore_search("xxabcdxx", "abcd")
# print boyer_moore_search("xxxabcdx", "abcd")
# print boyer_moore_search("xxxxabcd", "abcd")
# print boyer_moore_search("abdabcbadbacabca", "abcd")
# print boyer_moore_search("aababcabcx", "abcd")
