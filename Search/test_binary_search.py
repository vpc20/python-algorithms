from unittest import TestCase
from Search.BinarySearch import binary_search
from random import randrange, choice
from random_data import random_int_array


class TestBinarySearch(TestCase):
    def test_binary_search(self):
        arr = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
        self.assertEqual(-1, binary_search(' ', arr))
        self.assertEqual(-1, binary_search('a', arr))
        self.assertEqual(-1, binary_search('ab', arr))
        self.assertEqual(-1, binary_search('bc', arr))
        self.assertEqual(-1, binary_search('cd', arr))
        self.assertEqual(-1, binary_search('de', arr))
        self.assertEqual(-1, binary_search('ef', arr))
        self.assertEqual(0, binary_search('aaa', arr))
        self.assertEqual(1, binary_search('bbb', arr))
        self.assertEqual(2, binary_search('ccc', arr))
        self.assertEqual(3, binary_search('ddd', arr))
        self.assertEqual(4, binary_search('eee', arr))

        # needle exists in haystack
        for _ in range(1000):
            arr1 = random_int_array(20, 1000)
            if arr1:
                arr1 = list(set(arr1))
                arr1.sort()
                needle = choice(arr1)
                print(arr1, needle)
                self.assertEqual(arr1.index(needle), binary_search(needle, arr1))

        # random needle value in haystack
        for _ in range(1000):
            arr1 = random_int_array(20, 1000)
            if arr1:
                arr1 = list(set(arr1))
                arr1.sort()
                needle = randrange(1000)
                print(arr1, needle)
                try:
                    index_val = arr1.index(needle)
                except ValueError:
                    index_val = -1
                print(binary_search(needle, arr1), index_val)
                self.assertEqual(index_val, binary_search(needle, arr1))