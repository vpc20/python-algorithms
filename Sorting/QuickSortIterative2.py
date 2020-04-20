import unittest


def quicksort(arr):
    if not arr:
        return []
    queue = [(0, len(arr) - 1)]
    while queue:
        start = queue[0][0]
        end = queue[0][1]
        split_pos = partition(arr, start, end)
        if start <= split_pos - 1:
            queue.append((start, split_pos - 1))
        if split_pos + 1 <= end:
            queue.append((split_pos + 1, end))
        queue.pop(0)
    return arr  # for testing only, sorting is done in-place so this is not necessary


# def qsort(arr, start, end):
#     if start < end:
#         split_pos = partition(arr, start, end)
#         qsort(arr, start, split_pos - 1)
#         qsort(arr, split_pos + 1, end)


def partition(arr, start, end):
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
    return right


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


# arr = [5, 3, 7, 1, 9]
# arr = [5, 4, 3, 2, 1]
# arr = [2, 1, 4, 3, 6, 5, 8]
# arr = [2]
# arr = [1,2]
# arr = [2,1]
# print(quicksort(arr))
# print arr

# arr = [2, 1]
# print partition(arr, 0, len(arr) - 1)
# print arr
