import unittest
from random import randrange


def selection_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

# def selection_sort(lst):
#     for i in range(len(lst) - 1):
#         minval = lst[i]
#         for j in range(i + 1, len(lst)):
#             if lst[j] < minval:
#                 minval = lst[j]
#         lst[i] = minval


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_arr_size + 1))]


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for _ in range(10000):
            arr = random_int_array(100, 1000)
            print('')
            print('Random array - ', arr)
            selection_sort(arr)
            print('Sorted array - ', arr)
            self.assertEqual(is_sorted(arr), True)


if __name__ == '__main__':
    unittest.main()

# xList = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
# xList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# xList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# xList = [1, 10, 3, 8, 5, 6, 7, 4, 9, 2]
# xList = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
# xList = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print "\nUnsorted List"
# print xList
# selection_sort(xList)
# print "Selection Sort"
# print xList
# # import random
#
# arr = [random.randrange(100000) for i in range(1000)]
# selection_sort(arr)
# print arr
