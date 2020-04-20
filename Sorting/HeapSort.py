import unittest
from random import randrange


def is_max_heap(arr):
    for child_idx in range(1, len(arr)):
        parent_idx = (child_idx - 1) / 2
        if arr[child_idx] > arr[parent_idx]:
            return False
    return True


# def max_sift_up(arr, child_idx):
#     while child_idx != 0:
#         parent_idx = (child_idx - 1) / 2
#         if arr[child_idx] > arr[parent_idx]:
#             arr[child_idx], arr[parent_idx] = arr[parent_idx], arr[child_idx]
#             child_idx = parent_idx
#         else:
#             break
#

def max_sift_down(arr, parent_idx, last_idx):
    while True:
        left_idx = 2 * parent_idx + 1
        if left_idx > last_idx:
            break  # no children
        right_idx = 2 * parent_idx + 2
        if right_idx > last_idx:
            larger_child_idx = left_idx  # there is only left child
        elif arr[left_idx] > arr[right_idx]:
            larger_child_idx = left_idx
        else:
            larger_child_idx = right_idx

        if arr[larger_child_idx] > arr[parent_idx]:
            arr[parent_idx], arr[larger_child_idx] = arr[larger_child_idx], arr[parent_idx]
            parent_idx = larger_child_idx
        else:
            break


def max_heapify(arr):
    len_arr = len(arr)
    for i in range(len_arr / 2, -1, -1):
        max_sift_down(arr, i, len_arr - 1)


# def max_heapify(arr):
#     for i in range(1, len(arr)):
#         max_sift_up(arr, i)


def heapsort(arr):
    max_heapify(arr)
    last_idx = len(arr) - 1
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        last_idx -= 1
        max_sift_down(arr, 0, last_idx)


def random_int_array(max_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        # for i in range(10000):
        #     a1 = random_int_array(20, 100)
        #     max_heapify(a1)
        #     print a1
        #     self.assertEqual(is_max_heap(a1), True)
        #
        # for i in range(10000):
        #     a1 = random_int_array(20, 100)
        #     a2 = list(a1)
        #     print a1
        #     heapsort(a1)
        #     self.assertEqual(a1, sorted(a2))


if __name__ == '__main__':
    unittest.main()

# a = [2, 1, 3]
# a = [4, 3, 2, 5]
# print max_sift_up(a, 3)
# print a

# a = [21, 91, 99, 89, 1, 6, 70, 49, 7, 33, 10, 69]
# print a
# max_heapify(a)
# print a
# print is_max_heap(a)
# heapsort(a)
# print a
# print sorted(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# max_heapify(a)
# print a
# print is_max_heap(a)
