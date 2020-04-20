import unittest
from random import randrange


def quicksort(arr):
    start = 0
    end = len(arr) - 1
    queue = [(start, end)]
    while queue:
        start, end = queue.pop(0)
        pivot = arr[start]
        left = start + 1
        right = end
        while left < right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        if arr[start] > arr[right]:
            arr[start], arr[right] = arr[right], arr[start]
        if start < right - 1:
            queue.append((start, right - 1))
        if right + 1 < end:
            queue.append((right + 1, end))


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for i in range(randrange(max_arr_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(quicksort([]), [])
        #
        # self.assertEqual(quicksort([1]), [1])
        # self.assertEqual(quicksort([1, 2]), [1, 2])
        # self.assertEqual(quicksort([2, 1]), [1, 2])
        #
        # self.assertEqual(quicksort([1, 2, 3]), [1, 2, 3])
        # self.assertEqual(quicksort([1, 3, 2]), [1, 2, 3])
        # self.assertEqual(quicksort([2, 1, 3]), [1, 2, 3])
        # self.assertEqual(quicksort([2, 3, 1]), [1, 2, 3])
        # self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])
        # self.assertEqual(quicksort([3, 2, 1]), [1, 2, 3])
        #
        # self.assertEqual(quicksort([1, 2, 3, 4]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([1, 2, 4, 3]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([1, 3, 2, 4]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([1, 3, 4, 2]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([1, 4, 2, 3]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([1, 4, 3, 2]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([2, 1, 3, 4]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([2, 1, 4, 3]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([2, 3, 1, 4]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([2, 3, 4, 1]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([2, 4, 1, 3]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([2, 4, 3, 1]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([3, 1, 2, 4]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([3, 1, 4, 2]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([3, 2, 1, 4]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([3, 2, 4, 1]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([3, 4, 1, 2]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([3, 4, 2, 1]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([4, 1, 2, 3]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([4, 1, 3, 2]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([4, 2, 1, 3]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([4, 2, 3, 1]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([4, 3, 1, 2]), [1, 2, 3, 4])
        # self.assertEqual(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])
        #
        # self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 2, 3, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 2, 4, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 2, 4, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 2, 5, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 2, 5, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 3, 4, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 3, 4, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 3, 5, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 4, 2, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 4, 2, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 4, 3, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 4, 3, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 4, 5, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 5, 3, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 5, 3, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([1, 5, 4, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 1, 3, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 1, 3, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 1, 4, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 1, 4, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 1, 5, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 1, 5, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 3, 1, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 3, 4, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 3, 5, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 3, 5, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 4, 1, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 4, 3, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 4, 5, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 4, 5, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 5, 1, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 5, 1, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 5, 3, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 5, 3, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 5, 4, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([2, 5, 4, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 1, 2, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 1, 2, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 2, 4, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 2, 4, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 2, 5, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 4, 1, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 4, 1, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 4, 2, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 4, 2, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 4, 5, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 4, 5, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 5, 1, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 5, 1, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 5, 2, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 5, 2, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 5, 4, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([3, 5, 4, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 1, 2, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 1, 2, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 1, 3, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 1, 3, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 1, 5, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 1, 5, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 2, 1, 3, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 2, 1, 5, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 2, 3, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 2, 5, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 3, 1, 2, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 3, 1, 5, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 3, 2, 1, 5]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 3, 2, 5, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 3, 5, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 3, 5, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 5, 1, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 5, 2, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 5, 2, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([4, 5, 3, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 1, 3, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 1, 3, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 1, 4, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 2, 1, 3, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 2, 1, 4, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 2, 3, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 2, 3, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 2, 4, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 4, 1, 2, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 4, 1, 3, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 4, 2, 1, 3]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 4, 2, 3, 1]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])
        # self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        for _ in range(10000):
            a1 = random_int_array(25, 10000)
            if a1:
                sorted_a1 = sorted(a1)
                print(sorted_a1)
                quicksort(a1)
                self.assertEqual(sorted_a1, a1)


if __name__ == '__main__':
    unittest.main()

# arr1 = [3, 4, 6, 1, 2, 5]
# print quicksort(arr1)
