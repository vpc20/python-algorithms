from random import randrange
from random_data import random_int_array
import unittest


def linear_search(needle, haystack):
    """Linear search function

    :param needle: search argument
    :param haystack: array where search is performed
    :return: index of the needle, -1 if not found
    """
    for i, item in enumerate(haystack):
        if item == needle:
            return i
    return -1


# def linear_search(needle, haystack):
#     for i in range(len(haystack)):
#         if needle == haystack[i]:
#             return i
#     return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        self.assertEqual(linear_search(0, []), -1)

        a = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(0, a), -1)
        self.assertEqual(linear_search(1, a), 0)
        self.assertEqual(linear_search(2, a), 1)
        self.assertEqual(linear_search(3, a), 2)
        self.assertEqual(linear_search(4, a), 3)
        self.assertEqual(linear_search(5, a), 4)
        self.assertEqual(linear_search(6, a), -1)

        # needle found in haystack
        for _ in range(10000):
            a1 = []
            while not a1:
                a1 = random_int_array(100, 1000)
            n = a1[randrange(len(a1))]
            print(a1)
            print(n)
            self.assertEquals(linear_search(n, a1), a1.index(n))

        # random needle
        for _ in range(10000):
            a1 = []
            while not a1:
                a1 = random_int_array(100, 1000)
            n = randrange(1000)
            print(a1)
            print(n)
            try:
                ret = a1.index(n)
            except ValueError:
                ret = -1
            print(ret)
            self.assertEquals(linear_search(n, a1), ret)


if __name__ == '__main__':
    unittest.main()
