import unittest


def quicksort(arr):
    if len(arr) < 2:
        return arr
    split_pos = partition(arr)
    return quicksort(arr[:split_pos]) + quicksort(arr[split_pos:])


def partition(arr):
    pivot = arr[0]
    arr = [n for n in arr if n < pivot] + \
          [n for n in arr if n == pivot] + \
          [n for n in arr if n > pivot]
    if arr.index(pivot) == 0:
        split_pos = 1
    else:
        split_pos = arr.index(pivot)
    return split_pos



# def quicksort(arr):
#     if len(arr) < 2:
#         return arr
#     arr1, split_pos = partition(arr)
#     return quicksort(arr1[:split_pos]) + quicksort(arr1[split_pos:])
#
#
# def partition(arr):
#     pivot = arr[0]
#     out_arr = [n for n in arr if n < pivot] + \
#               [n for n in arr if n == pivot] + \
#               [n for n in arr if n > pivot]
#     if out_arr.index(pivot) == 0:
#         split_pos = 1
#     else:
#         split_pos = out_arr.index(pivot)
#     return out_arr, split_pos


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(quicksort([]), [])

        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([1, 2]), [1, 2])
        self.assertEqual(quicksort([2, 1]), [1, 2])

        self.assertEqual(quicksort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(quicksort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(quicksort([2, 1, 3]), [1, 2, 3])
        self.assertEqual(quicksort([2, 3, 1]), [1, 2, 3])
        self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(quicksort([3, 2, 1]), [1, 2, 3])

        self.assertEqual(quicksort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([1, 2, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(quicksort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([1, 3, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(quicksort([1, 4, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(quicksort([1, 4, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(quicksort([2, 1, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([2, 1, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(quicksort([2, 3, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([2, 3, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(quicksort([2, 4, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(quicksort([2, 4, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(quicksort([3, 1, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([3, 1, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(quicksort([3, 2, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([3, 2, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(quicksort([3, 4, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(quicksort([3, 4, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 1, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 1, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 2, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 2, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 3, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])

        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 3, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 4, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 4, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 5, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 5, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 3, 4, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 3, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 3, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 4, 2, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 4, 2, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 4, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 4, 3, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 4, 5, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 5, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 5, 3, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 5, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 1, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 1, 3, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 1, 4, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 1, 4, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 1, 5, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 1, 5, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 3, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 3, 4, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 3, 5, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 3, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 4, 1, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 4, 3, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 4, 5, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 4, 5, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 5, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 5, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 5, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 5, 3, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 5, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([2, 5, 4, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 1, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 1, 2, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 4, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 5, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 4, 1, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 4, 1, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 4, 2, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 4, 2, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 4, 5, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 4, 5, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 5, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 5, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 5, 2, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 5, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 5, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 5, 4, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 1, 2, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 1, 2, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 1, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 1, 3, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 1, 5, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 1, 5, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 2, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 2, 1, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 2, 3, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 2, 5, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 3, 1, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 3, 1, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 3, 2, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 3, 2, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 3, 5, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 3, 5, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 5, 1, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 5, 2, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 5, 2, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([4, 5, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 1, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 1, 3, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 1, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 3, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 4, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 1, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 2, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 2, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

import random

# print partition(arr)
# arr = [4, 1, 8, 2, 7, 6, 5, 3]
# arr = [9,8,7,6,5,4,3,2,1]
# arr = [2,4,6,8,1,3,5,7,9]
# arr = [9,7,5,3,1,8,6,4,2]
# arr = [random.randrange(100000) for i in range(10000)]
# print quicksort(arr)

# print quicksort([1])
# print quicksort([2,3])
