import unittest
from random import randrange


def shell_sort(arr):
    h = 1
    while h < len(arr) / 3:
        h = 3 * h + 1
    print(h)

    while h > 0:  # h-sort
        for i in range(h, len(arr)):
            num = arr[i]  # number to be inserted
            j = i
            while (j >= h) and (arr[j - h] > num):  # look for the insertion point
                arr[j] = arr[j - h]  # move values to the right to create space for the insert
                j -= h
            arr[j] = num  # actual insertion
        h = int(h / 3)

    return arr  # for testing only, sorting is done in-place so this is not necessary


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for i in range(randrange(max_arr_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(shell_sort([]), [])

        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([1, 2]), [1, 2])
        self.assertEqual(shell_sort([2, 1]), [1, 2])

        self.assertEqual(shell_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(shell_sort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(shell_sort([2, 1, 3]), [1, 2, 3])
        self.assertEqual(shell_sort([2, 3, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])

        self.assertEqual(shell_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([1, 2, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([1, 3, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([1, 4, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([1, 4, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([2, 1, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([2, 1, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([2, 3, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([2, 3, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([2, 4, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([2, 4, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([3, 1, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([3, 1, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([3, 2, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([3, 2, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([3, 4, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([3, 4, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([4, 1, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([4, 1, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([4, 2, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([4, 2, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([4, 3, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([4, 3, 2, 1]), [1, 2, 3, 4])

        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 3, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 4, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 4, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 5, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 5, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 3, 4, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 3, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 3, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 4, 2, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 4, 2, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 4, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 4, 3, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 4, 5, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 5, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 5, 3, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 5, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 1, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 1, 3, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 1, 4, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 1, 4, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 1, 5, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 1, 5, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 3, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 3, 4, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 3, 5, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 3, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 4, 1, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 4, 3, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 4, 5, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 4, 5, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 5, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 5, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 5, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 5, 3, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 5, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([2, 5, 4, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 1, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 1, 2, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 2, 4, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 2, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 2, 5, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 4, 1, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 4, 1, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 4, 2, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 4, 2, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 4, 5, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 4, 5, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 5, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 5, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 5, 2, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 5, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 5, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([3, 5, 4, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 1, 2, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 1, 2, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 1, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 1, 3, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 1, 5, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 1, 5, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 2, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 2, 1, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 2, 3, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 2, 5, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 3, 1, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 3, 1, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 3, 2, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 3, 2, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 3, 5, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 3, 5, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 5, 1, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 5, 2, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 5, 2, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([4, 5, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 1, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 1, 3, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 1, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 2, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 2, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 2, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 2, 3, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 2, 4, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 1, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 2, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 2, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        for i in range(10000):
            arr = random_int_array(100, 1000)
            print(arr)
            self.assertEqual(shell_sort(arr), sorted(arr))


if __name__ == '__main__':
    unittest.main()


# xList = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
# xList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# xList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# xList = [1, 10, 3, 8, 5, 6, 7, 4, 9, 2]
# xList = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
#
# print "\nUnsorted List"
# print xList
# insertion_sort(xList)
# print "Insertion Sort"
# print xList
