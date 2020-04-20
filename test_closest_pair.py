from unittest import TestCase
from random import randrange

from ClosestPairOfPoints import closest_pair, brute_cp


class TestClosestPpair(TestCase):
    def test_closest_pair(self):
        for _ in range(10000):
            arr = []
            for i in range(100):
                pt = (randrange(-500, 500), randrange(-500, 500))
                arr.append(pt)
            print(arr)
            self.assertEqual(brute_cp(arr)[2], closest_pair(arr)[2])
