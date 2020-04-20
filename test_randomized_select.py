from unittest import TestCase

from RandomizedSelect import randomized_select, randomized_select_iter
from random_data import random_int_array


class TestRandomizedSelect(TestCase):
    def test_randomized_select(self):
        for _ in range(1000):
            arr = random_int_array(100, 1000)
            print(arr)
            sorted_arr = sorted(arr)
            for i in range(len(arr)):
                self.assertEqual(sorted_arr[i], randomized_select(arr, i + 1))

    def test_randomized_select_iter(self):
        for _ in range(1000):
            arr = random_int_array(100, 1000)
            print(arr)
            sorted_arr = sorted(arr)
            for i in range(len(arr)):
                self.assertEqual(sorted_arr[i], randomized_select_iter(arr, i + 1))
