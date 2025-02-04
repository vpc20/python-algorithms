from random import randrange, choices
from unittest import TestCase

from Sorting.MergeSortIterative import merge_sort
from SumInArray import sum_in_array
from random_data import random_int_array


class TestAlgorithms(TestCase):
    def test_sum_in_array(self):
        # the sum equals parameter passed to function
        for _ in range(1000):
            arr1 = random_int_array(20, 1000)
            if arr1:
                int1, int2 = choices(arr1, k=2)
                if int1 != int2:
                    print(arr1, int1, int2, int1 + int2)
                    l, r = sum_in_array(arr1, int1 + int2)
                    self.assertEqual(arr1[l] + arr1[r], int1 + int2)
        # the sum does no equal parameter passed to function
        for _ in range(1000):
            arr1 = random_int_array(20, 1000)
            sum_arr = []
            if arr1:
                for i in range(len(arr1)):
                    for j in range(i + 1, len(arr1)):
                        sum_arr.append(arr1[i] + arr1[j])
                x = randrange(-5000, 5000)
                while x in sum_arr:
                    x = randrange(-5000, 5000)
                print(sum_arr)
                print(arr1, x)
                self.assertEqual(sum_in_array(arr1, x), (-1, -1))

    def test_merge_sort(self):
        # self.assertEqual(merge_sort([]), [])

        # self.assertEqual(merge_sort([1]), [1])
        # self.assertEqual(merge_sort([1, 2]), [1, 2])
        # self.assertEqual(merge_sort([2, 1]), [1, 2])
        #
        # self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        # self.assertEqual(merge_sort([1, 3, 2]), [1, 2, 3])
        # self.assertEqual(merge_sort([2, 1, 3]), [1, 2, 3])
        # self.assertEqual(merge_sort([2, 3, 1]), [1, 2, 3])
        # self.assertEqual(merge_sort([3, 1, 2]), [1, 2, 3])
        # self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])
        #
        # self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([1, 2, 4, 3]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([1, 3, 2, 4]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([1, 3, 4, 2]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([1, 4, 2, 3]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([1, 4, 3, 2]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([2, 1, 3, 4]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([2, 1, 4, 3]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([2, 3, 1, 4]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([2, 3, 4, 1]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([2, 4, 1, 3]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([2, 4, 3, 1]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([3, 1, 2, 4]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([3, 1, 4, 2]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([3, 2, 1, 4]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([3, 2, 4, 1]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([3, 4, 1, 2]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([3, 4, 2, 1]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([4, 1, 2, 3]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([4, 1, 3, 2]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([4, 2, 1, 3]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([4, 2, 3, 1]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([4, 3, 1, 2]), [1, 2, 3, 4])
        # self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        #
        # self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 2, 3, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 2, 4, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 2, 4, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 2, 5, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 2, 5, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 3, 4, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 3, 4, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 3, 5, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 4, 2, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 4, 2, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 4, 3, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 4, 3, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 4, 5, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 5, 3, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 5, 3, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([1, 5, 4, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 1, 3, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 1, 3, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 1, 4, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 1, 4, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 1, 5, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 1, 5, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 3, 1, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 3, 4, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 3, 5, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 3, 5, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 4, 1, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 4, 3, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 4, 5, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 4, 5, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 5, 1, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 5, 1, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 5, 3, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 5, 3, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 5, 4, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([2, 5, 4, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 1, 2, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 1, 2, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 2, 4, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 2, 4, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 2, 5, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 4, 1, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 4, 1, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 4, 2, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 4, 2, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 4, 5, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 4, 5, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 5, 1, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 5, 1, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 5, 2, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 5, 2, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 5, 4, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([3, 5, 4, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 1, 2, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 1, 2, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 1, 3, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 1, 3, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 1, 5, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 1, 5, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 2, 1, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 2, 1, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 2, 3, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 2, 5, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 3, 1, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 3, 1, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 3, 2, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 3, 2, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 3, 5, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 3, 5, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 5, 1, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 5, 2, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 5, 2, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([4, 5, 3, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 1, 3, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 1, 3, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 1, 4, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 2, 1, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 2, 1, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 2, 3, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 2, 3, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 2, 4, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 4, 1, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 4, 1, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 4, 2, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 4, 2, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        for i in range(1000):
            arr = random_int_array(100, 1000)
            print(arr)
            sorted_arr = sorted(arr)
            print(sorted_arr)
            merge_sort(arr)
            print(arr)
            self.assertEqual(sorted_arr, arr)
