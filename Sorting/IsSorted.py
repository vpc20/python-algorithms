import unittest
from random import randrange


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_arr_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        for i in range(1000):
            arr = random_int_array(100, 1000)
            print(arr)
            self.assertEqual(is_sorted(sorted(arr)), True)


if __name__ == '__main__':
    unittest.main()
