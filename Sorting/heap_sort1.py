import unittest
from random import randrange


def is_max_heap(arr):
    for child_idx in range(1, len(arr)):
        parent_idx = int((child_idx - 1) / 2)
        if arr[child_idx] > arr[parent_idx]:
            return False
    return True


def max_sift_down(arr, parent_idx):
    end_idx = len(arr) - 1
    largest_idx = end_idx
    while parent_idx <= end_idx:
        left_idx = 2 * parent_idx + 1
        right_idx = 2 * parent_idx + 2
        if left_idx <= end_idx and arr[left_idx] > arr[parent_idx]:
            largest_idx = left_idx
        else:
            largest_idx = parent_idx
        if right_idx <= end_idx and arr[right_idx] > arr[largest_idx]:
            largest_idx = right_idx
        if largest_idx != parent_idx:
            arr[parent_idx], arr[largest_idx] = arr[largest_idx], arr[parent_idx]
            parent_idx = largest_idx
        else:
            break


def max_heapify(arr):
    for i in range(int(len(arr) / 2), -1, -1):
        max_sift_down(arr, i)



def random_int_array(max_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        for i in range(10000):
            a1 = random_int_array(20, 100)
            max_heapify(a1)
            print(a1)
            self.assertEqual(is_max_heap(a1), True)

        # for i in range(100000):
        #     a1 = random_int_array(20, 100)
        #     a2 = list(a1)
        #     print a1
        #     heapsort(a1)
        #     self.assertEqual(a1, sorted(a2))


if __name__ == '__main__':
    unittest.main()



# arr = []
# arr = [1]
# arr = [1, 2]
# arr = [2, 1]
# arr = [1, 2, 3]
# arr = [1, 3, 2]
# arr = [2, 1, 3]
# arr = [2, 3, 1]
# arr = [3, 1, 2]
# arr = [3, 2, 1]
# max_sift_down(arr, 0)

# a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# a = [1, 2, 3, 4]
# max_heapify(a)
# print a
# print is_max_heap(a)

# a = [1, 4, 3, 2]
# max_sift_down(a, 0)
