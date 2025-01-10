import unittest
from random import randrange


def merge_sort(lst):
    if len(lst) > 1:
        mid = int(len(lst) / 2)
        left = lst[:mid]
        right = lst[mid:]
        return merge(merge_sort(left), merge_sort(right))
    else:
        return lst


def merge(list1, list2):
    i = 0  # indexes for list1
    j = 0  # index for list2
    sorted_list = []
    len_list1 = len(list1)
    len_list2 = len(list2)

    while i < len_list1 and j < len_list2:
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    while i < len_list1:
        sorted_list.append(list1[i])
        i += 1
    while j < len_list2:
        sorted_list.append(list2[j])
        j += 1
    return sorted_list


# def merge(list1, list2):
#     sorted_list = []
#     while list1 and list2:
#         if list1 and list2:
#             if list1[0] < list2[0]:
#                 sorted_list.append(list1.pop(0))
#             else:
#                 sorted_list.append(list2.pop(0))
#     while list1 and not list2:
#         sorted_list.append(list1.pop(0))
#     while list2 and not list1:
#         sorted_list.append(list2.pop(0))
#     return sorted_list


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for i in range(randrange(max_arr_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(merge_sort([]), [])

        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([1, 2]), [1, 2])
        self.assertEqual(merge_sort([2, 1]), [1, 2])

        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(merge_sort([2, 1, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([2, 3, 1]), [1, 2, 3])
        self.assertEqual(merge_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])

        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([1, 2, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([1, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([1, 3, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([1, 4, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([1, 4, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([2, 1, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([2, 1, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([2, 3, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([2, 3, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([2, 4, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([2, 4, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 1, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 1, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 2, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 2, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 4, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 4, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 1, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 1, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 2, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 2, 3, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 3, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 2, 3, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 2, 4, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 2, 4, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 2, 5, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 2, 5, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 3, 4, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 3, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 3, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 4, 2, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 4, 2, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 4, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 4, 3, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 4, 5, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 5, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 5, 3, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([1, 5, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 1, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 1, 3, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 1, 4, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 1, 4, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 1, 5, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 1, 5, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 3, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 3, 4, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 3, 5, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 3, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 4, 1, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 4, 3, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 4, 5, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 4, 5, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 5, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 5, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 5, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 5, 3, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 5, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([2, 5, 4, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 1, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 1, 2, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 2, 4, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 2, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 2, 5, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 4, 1, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 4, 1, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 4, 2, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 4, 2, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 4, 5, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 4, 5, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 5, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 5, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 5, 2, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 5, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 5, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([3, 5, 4, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 1, 2, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 1, 2, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 1, 3, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 1, 3, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 1, 5, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 1, 5, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 2, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 2, 1, 5, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 2, 3, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 2, 5, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 3, 1, 2, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 3, 1, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 3, 2, 1, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 3, 2, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 3, 5, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 3, 5, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 5, 1, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 5, 2, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 5, 2, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([4, 5, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 1, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 1, 3, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 1, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 2, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 2, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 2, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 2, 3, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 2, 4, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 3, 4, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 4, 1, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 4, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 4, 2, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 4, 2, 3, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        for i in range(10000):
            arr = random_int_array(100, 1000)
            print(arr)
            self.assertEqual(merge_sort(arr), sorted(arr))


if __name__ == '__main__':
    unittest.main()

# lista = [8, 7, 6, 5]
# print merge_sort(lista)
# print lista
