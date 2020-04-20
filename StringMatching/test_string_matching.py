from unittest import TestCase
from StringMatching.BoyerMooreHorspool import bmh_search
from StringMatching.BruteForceSearch import brute_force_search
from StringMatching.KnuthMorrisPratt import kmp_search

from random_data import random_string, random_substring


class TestStringMatching(TestCase):
    def test_bmh_search(self):
        self.assertEqual(-1, bmh_search('', ''))
        self.assertEqual(-1, bmh_search('', 'x'))
        self.assertEqual(-1, bmh_search('axxxx', ''))
        self.assertEqual(-1, bmh_search('axxxx', ' '))
        self.assertEqual(0, bmh_search('axxxx', 'a'))
        self.assertEqual(1, bmh_search('xaxxx', 'a'))
        self.assertEqual(2, bmh_search('xxaxx', 'a'))
        self.assertEqual(3, bmh_search('xxxax', 'a'))
        self.assertEqual(4, bmh_search('xxxxa', 'a'))
        self.assertEqual(0, bmh_search('abcxxx', 'abc'))
        self.assertEqual(1, bmh_search('xabcxx', 'abc'))
        self.assertEqual(2, bmh_search('xxabcx', 'abc'))
        self.assertEqual(3, bmh_search('xxxabc', 'abc'))
        self.assertEqual(0, bmh_search('a', 'a'))

        # generate pattern which matches
        for i in range(1000):
            # s = random_strings(12, 20)
            s = random_string(80)
            pattern = random_substring(s, 15)
            print(s, '---', pattern)
            print(s.find(pattern, bmh_search(s, pattern)))
            self.assertEqual(s.find(pattern), bmh_search(s, pattern))

        # generate random pattern
        for i in range(1000):
            # s = random_strings(12, 20)
            s = random_string(80)
            pattern = random_string(15)
            print(s, '---', pattern)
            print(s.find(pattern, bmh_search(s, pattern)))
            self.assertEqual(s.find(pattern), bmh_search(s, pattern))

    def test_kmp_search(self):
        self.assertEqual(-1, kmp_search('', ''))
        self.assertEqual(-1, kmp_search('', 'x'))
        self.assertEqual(-1, kmp_search('axxxx', ''))
        self.assertEqual(-1, kmp_search('axxxx', ' '))
        self.assertEqual(0, kmp_search('axxxx', 'a'))
        self.assertEqual(1, kmp_search('xaxxx', 'a'))
        self.assertEqual(2, kmp_search('xxaxx', 'a'))
        self.assertEqual(3, kmp_search('xxxax', 'a'))
        self.assertEqual(4, kmp_search('xxxxa', 'a'))
        self.assertEqual(0, kmp_search('abcxxx', 'abc'))
        self.assertEqual(1, kmp_search('xabcxx', 'abc'))
        self.assertEqual(2, kmp_search('xxabcx', 'abc'))
        self.assertEqual(3, kmp_search('xxxabc', 'abc'))
        self.assertEqual(0, kmp_search('a', 'a'))

        # generate pattern which matches
        for i in range(1000):
            s = random_string(80)
            pattern = random_substring(s, 15)
            print(s, '---', pattern)
            print(s.find(pattern), kmp_search(s, pattern))
            self.assertEqual(s.find(pattern), kmp_search(s, pattern))

        # generate random pattern
        for i in range(1000):
            s = random_string(80)
            pattern = random_string(15)
            print(s, '---', pattern)
            print(s.find(pattern), kmp_search(s, pattern))
            self.assertEqual(s.find(pattern), kmp_search(s, pattern))

    def test_brute_force_search(self):
        self.assertEqual(-1, brute_force_search('', ''))
        self.assertEqual(-1, brute_force_search('', 'x'))
        self.assertEqual(-1, brute_force_search('axxxx', ''))
        self.assertEqual(-1, brute_force_search('axxxx', ' '))
        self.assertEqual(0, brute_force_search('axxxx', 'a'))
        self.assertEqual(1, brute_force_search('xaxxx', 'a'))
        self.assertEqual(2, brute_force_search('xxaxx', 'a'))
        self.assertEqual(3, brute_force_search('xxxax', 'a'))
        self.assertEqual(4, brute_force_search('xxxxa', 'a'))
        self.assertEqual(0, brute_force_search('abcxxx', 'abc'))
        self.assertEqual(1, brute_force_search('xabcxx', 'abc'))
        self.assertEqual(2, brute_force_search('xxabcx', 'abc'))
        self.assertEqual(3, brute_force_search('xxxabc', 'abc'))
        self.assertEqual(0, brute_force_search('a', 'a'))

        # generate pattern which matches
        for i in range(1000):
            s = random_string(80)
            pattern = random_substring(s, 15)
            print(s, '---', pattern)
            print(s.find(pattern), kmp_search(s, pattern))
            self.assertEqual(s.find(pattern), brute_force_search(s, pattern))

        # generate random pattern
        for i in range(1000):
            s = random_string(80)
            pattern = random_string(15)
            print(s, '---', pattern)
            print(s.find(pattern), kmp_search(s, pattern))
            self.assertEqual(s.find(pattern), brute_force_search(s, pattern))
