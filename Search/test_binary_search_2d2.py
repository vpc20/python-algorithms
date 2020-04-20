from unittest import TestCase
from Search.BinarySearch2dSorted2 import binary_search_2d2


class TestBinarySearch2d2(TestCase):
    def test_binary_search_2d2(self):
        arr2d = [[2, 6, 10, 12],
                 [3, 9, 11, 14],
                 [5, 16, 19, 20]]
        self.assertEqual(-1, binary_search_2d2(1, arr2d))
        self.assertEqual(-1, binary_search_2d2(17, arr2d))
        self.assertEqual(-1, binary_search_2d2(4, arr2d))
        self.assertEqual(-1, binary_search_2d2(15, arr2d))

        self.assertEqual((0, 0), binary_search_2d2(2, arr2d))
        self.assertEqual((0, 1), binary_search_2d2(6, arr2d))
        self.assertEqual((0, 2), binary_search_2d2(10, arr2d))
        self.assertEqual((0, 3), binary_search_2d2(12, arr2d))
        self.assertEqual((1, 0), binary_search_2d2(3, arr2d))
        self.assertEqual((1, 1), binary_search_2d2(9, arr2d))
        self.assertEqual((1, 2), binary_search_2d2(11, arr2d))
        self.assertEqual((1, 3), binary_search_2d2(14, arr2d))
        self.assertEqual((2, 0), binary_search_2d2(5, arr2d))
        self.assertEqual((2, 1), binary_search_2d2(16, arr2d))
        self.assertEqual((2, 2), binary_search_2d2(19, arr2d))
        self.assertEqual((2, 3), binary_search_2d2(20, arr2d))
