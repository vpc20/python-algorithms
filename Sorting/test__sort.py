from unittest import TestCase

from Sorting.BubbleSort import bubble_sort
from Sorting.InsertionSort import insertion_sort
from Sorting.MergeSort import merge_sort
from Sorting.QuickSort import quicksort
from random_data import random_int_array


class TestSort(TestCase):
    def test_merge_sort(self):
        arr = []
        merge_sort(arr)
        self.assertEqual([], arr)

        arr = [1]
        merge_sort(arr)
        self.assertEqual([1], arr)

        arr = [1, 2]
        merge_sort(arr)
        self.assertEqual([1, 2], arr)
        arr = [2, 1]
        merge_sort(arr)
        self.assertEqual([1, 2], arr)

        arr = [1, 2, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [1, 3, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 1, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 3, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 1, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 2, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3], arr)

        arr = [1, 2, 3, 4]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 2, 4, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 2, 4]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 4, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 2, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 3, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 3, 4]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 4, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 1, 4]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 4, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 1, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 3, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 2, 4]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 4, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 1, 4]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 4, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 1, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 2, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 2, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 3, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 1, 3]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 3, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 1, 2]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 2, 1]
        merge_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)

        for i in range(5000):
            arr = random_int_array(100, 1000)
            print(arr)
            merge_sort(arr)
            self.assertEqual(sorted(arr), arr)

    def test_bubble_sort(self):
        arr = []
        bubble_sort(arr)
        self.assertEqual([], arr)

        arr = [1]
        bubble_sort(arr)
        self.assertEqual([1], arr)

        arr = [1, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2], arr)
        arr = [2, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2], arr)

        arr = [1, 2, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [1, 3, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 1, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 3, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 1, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 2, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3], arr)

        arr = [1, 2, 3, 4]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 2, 4, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 2, 4]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 4, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 2, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 3, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 3, 4]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 4, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 1, 4]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 4, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 1, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 3, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 2, 4]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 4, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 1, 4]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 4, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 1, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 2, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 2, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 3, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 1, 3]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 3, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 1, 2]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)

        for i in range(5000):
            arr = random_int_array(100, 1000)
            print(arr)
            bubble_sort(arr)
            self.assertEqual(sorted(arr), arr)

    def test_insertion_sort(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual([], arr)

        arr = [1]
        insertion_sort(arr)
        self.assertEqual([1], arr)

        arr = [1, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2], arr)
        arr = [2, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2], arr)

        arr = [1, 2, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [1, 3, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 1, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 3, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 1, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 2, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3], arr)

        arr = [1, 2, 3, 4]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 2, 4, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 2, 4]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 4, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 2, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 3, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 3, 4]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 4, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 1, 4]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 4, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 1, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 3, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 2, 4]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 4, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 1, 4]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 4, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 1, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 2, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 2, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 3, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 1, 3]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 3, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 1, 2]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual([1, 2, 3, 4], arr)

        for i in range(5000):
            arr = random_int_array(100, 1000)
            print(arr)
            insertion_sort(arr)
            self.assertEqual(sorted(arr), arr)

    def test_quicksort(self):
        arr = []
        quicksort(arr)
        self.assertEqual([], arr)

        arr = [1]
        quicksort(arr)
        self.assertEqual([1], arr)

        arr = [1, 2]
        quicksort(arr)
        self.assertEqual([1, 2], arr)
        arr = [2, 1]
        quicksort(arr)
        self.assertEqual([1, 2], arr)

        arr = [1, 2, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [1, 3, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 1, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [2, 3, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 1, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3], arr)
        arr = [3, 2, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3], arr)

        arr = [1, 2, 3, 4]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 2, 4, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 2, 4]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 3, 4, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 2, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [1, 4, 3, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 3, 4]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 1, 4, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 1, 4]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 3, 4, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 1, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [2, 4, 3, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 2, 4]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 1, 4, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 1, 4]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 2, 4, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 1, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [3, 4, 2, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 2, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 1, 3, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 1, 3]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 2, 3, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 1, 2]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)
        arr = [4, 3, 2, 1]
        quicksort(arr)
        self.assertEqual([1, 2, 3, 4], arr)

        for i in range(5000):
            arr = random_int_array(100, 1000)
            print(arr)
            quicksort(arr)
            self.assertEqual(sorted(arr), arr)
