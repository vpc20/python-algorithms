from unittest import TestCase
from Search.BinarySearch2dSorted1 import binary_search_2d1


class TestBinarySearch2dA(TestCase):
    def test_binary_search_2da(self):
        arr2d = [[2, 3, 4, 5],
                 [7, 8, 9, 10],
                 [12, 13, 14, 15]]
        self.assertEqual(-1, binary_search_2d1(1, arr2d))
        self.assertEqual(-1, binary_search_2d1(6, arr2d))
        self.assertEqual(-1, binary_search_2d1(16, arr2d))
        self.assertEqual((0, 0), binary_search_2d1(2, arr2d))
        self.assertEqual((0, 1), binary_search_2d1(3, arr2d))
        self.assertEqual((0, 2), binary_search_2d1(4, arr2d))
        self.assertEqual((0, 3), binary_search_2d1(5, arr2d))
        self.assertEqual((1, 0), binary_search_2d1(7, arr2d))
        self.assertEqual((1, 1), binary_search_2d1(8, arr2d))
        self.assertEqual((1, 2), binary_search_2d1(9, arr2d))
        self.assertEqual((1, 3), binary_search_2d1(10, arr2d))
        self.assertEqual((2, 0), binary_search_2d1(12, arr2d))
        self.assertEqual((2, 1), binary_search_2d1(13, arr2d))
        self.assertEqual((2, 2), binary_search_2d1(14, arr2d))
        self.assertEqual((2, 3), binary_search_2d1(15, arr2d))
