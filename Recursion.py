import unittest
# from random import randrange
from random import randrange

from random_data import random_int_array, random_string


def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def initial(lst):
    return lst[:-1]


def last(lst):
    return lst[-1]


def length(lst):
    if not lst:
        return 0
    return 1 + length(tail(lst))


def same(lst):  # returns the same string
    if not lst:
        return []
    return [head(lst)] + same(tail(lst))


def reverse(lst):
    if not lst:
        return []
    return [last(lst)] + reverse(initial(lst))


# def reverse(lst):
#     rev = []
#     while lst:
#         rev += [last(lst)]
#         lst = initial(lst)
#     return rev


def nth_element(lst, n):
    if not lst or n < 0 or n >= len(lst):
        return None
    if n == 0:
        return head(lst)
    return nth_element(tail(lst), n - 1)


def repeat(s, n):
    if n < 1:
        return ''
    return s + repeat(s, n - 1)


def pop_in_list(lst, n):
    if not lst:
        return []
    if n == 0:
        return tail(lst)
    else:
        return [head(lst)] + pop_in_list(tail(lst), n - 1)


def remove_in_list(lst, x):
    if not lst:
        return []
    if head(lst) == x:
        return tail(lst)
    else:
        return [head(lst)] + remove_in_list(tail(lst), x)


def insert_in_list(lst, s, n):
    if lst:
        if n == 0:
            return [s] + [head(lst)] + insert_in_list(tail(lst), s, n - 1)
        else:
            return [head(lst)] + insert_in_list(tail(lst), s, n - 1)
    else:
        return []


def invert_aux(list_of_two):
    list_of_two[0], list_of_two[1] = list_of_two[1], list_of_two[0]
    return list_of_two


def invert(lst):
    if lst:
        return [invert_aux(head(lst))] + invert(tail(lst))
    else:
        return []


def count_occurences(lst, s):
    if lst:
        if head(lst) == s:
            return 1 + count_occurences(tail(lst), s)
        else:
            return count_occurences(tail(lst), s)
    else:
        return 0


def swapper_helper(s, s1, s2):
    if s == s1:
        return s2
    elif s == s2:
        return s1
    else:
        return s


def swapper(lst, s1, s2):
    if lst:
        return [swapper_helper(head(lst), s1, s2)] + swapper(tail(lst), s1, s2)
    else:
        return []


def prod_aux(item, lst):
    if lst:
        # print  str([item]) + " + " + str([head(lst)]) + " + " + "prod_aux(" + str(item) + ", tail(" + str(lst) + "))"
        return [item] + [head(lst)] + prod_aux(item, tail(lst))
    else:
        return []


def product(list1, list2):
    if list1 and list2:
        print('prod_aux(head(' + str(list1) + ', ' + str(list2) + ') + product(tail(' + str(list1) + '), ' + str(
            list2) + ')')
        return prod_aux(head(list1), list2) + product(tail(list1), list2)
    else:
        return []


def zipit(list1, list2):
    if list1 and list2:
        return [[head(list1)] + [head(list2)]] + zipit(tail(list1), tail(list2))
    else:
        return []


def scale_list(list1, scale):
    if list1:
        return [head(list1) * scale] + scale_list(tail(list1), scale)
    else:
        return []


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(length([]), 0)
        self.assertEqual(length([1]), 1)
        self.assertEqual(length([1, 2]), 2)
        self.assertEqual(length([1, 2, 3]), 3)
        for _ in range(1000):
            arr = random_int_array(20, 100)
            # print(arr)
            self.assertEqual(length(arr), len(arr))

        self.assertEqual(same([]), [])
        self.assertEqual(same([1]), [1])
        self.assertEqual(same([1, 2]), [1, 2])
        self.assertEqual(same([1, 2, 3]), [1, 2, 3])
        for _ in range(1000):
            arr = random_int_array(20, 100)
            # print(arr)
            self.assertEqual(same(arr), arr)

        self.assertEqual(reverse([]), [])
        self.assertEqual(reverse([1]), [1])
        self.assertEqual(reverse([1, 2]), [2, 1])
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
        for _ in range(1000):
            arr = random_int_array(20, 100)
            # print(arr)
            arr1 = list(arr)
            arr1.reverse()
            self.assertEqual(reverse(arr), arr1)

        self.assertEqual(nth_element([], 1), None)
        self.assertEqual(nth_element([1, 2, 3], -1), None)
        self.assertEqual(nth_element([1, 2, 3], 3), None)
        self.assertEqual(nth_element([1, 2, 3], 0), 1)
        self.assertEqual(nth_element([1, 2, 3], 1), 2)
        self.assertEqual(nth_element([1, 2, 3], 2), 3)
        for _ in range(1000):
            arr = random_int_array(20, 100)
            if arr:
                i = randrange(len(arr))
                # print(arr, i)
                self.assertEqual(nth_element(arr, i), arr[i])

        self.assertEqual(repeat('ha', -1), '')
        self.assertEqual(repeat('ha', 0), '')
        self.assertEqual(repeat('ha', 1), 'ha')
        self.assertEqual(repeat('ha', 2), 'haha')
        self.assertEqual(repeat('ha', 3), 'hahaha')
        for _ in range(1000):
            s = random_string(10)
            i = randrange(10)
            # print(s, i)
            self.assertEqual(repeat(s, i), s * i)

        self.assertEqual(pop_in_list([], 0), [])
        self.assertEqual(pop_in_list([1, 2, 3, 4, 5], 0), [2, 3, 4, 5])
        self.assertEqual(pop_in_list([1, 2, 3, 4, 5], 1), [1, 3, 4, 5])
        self.assertEqual(pop_in_list([1, 2, 3, 4, 5], 2), [1, 2, 4, 5])
        self.assertEqual(pop_in_list([1, 2, 3, 4, 5], 3), [1, 2, 3, 5])
        self.assertEqual(pop_in_list([1, 2, 3, 4, 5], 4), [1, 2, 3, 4])
        self.assertEqual(pop_in_list([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

# print head([1, 2, 3])
# print tail([1, 2, 3])
# print initial([1, 2, 3])
# print last([1, 2, 3])

# print(list_length([1, 2, 3, 4, 5]))
# print(list_length([]))

# print same([1, 2, 3, 4, 5])
# print(reverse([1, 2, 3, 4, 5]))
# print(reverse_iter([1, 2, 3, 4, 5]))

# print nth_element([1, 2, 3, 4, 5], 0)
# print nth_element([1, 2, 3, 4, 5], 1)
# print nth_element([1, 2, 3, 4, 5], 2)

# print remove_in_list([1, 2, 3, 4, 5], 1)
# print remove_in_list([1, 2, 3, 4, 5], 2)
# print remove_in_list([1, 2, 3, 4, 5], 3)
# print remove_in_list([1, 2, 3, 4, 5], 4)
# print remove_in_list([1, 2, 3, 4, 5], 5)

# print duple(0, "ha")
# print duple(1, "ha")
# print duple(2, "ha'")
# print duple(2, [1,2,3])

# print invert([])
# print invert([[1, 2], [3, 4]])

# print count_occurences([], 3)
# print count_occurences([8, 1, 2, 8, 3, 4, 5, 8], 8)

# print swapper([], 1, 2)
# print swapper([1, 2, 3, 4, 5], 1, 2)

# print insert_in_list([], 3, 2)
# print insert_in_list([1, 2, 3, 4, 5], 9, 0)
# print insert_in_list([1, 2, 4, 5], 3, 2)
# print insert_in_list([1, 2, 3, 4, 5], 9, 4)

# print prod_aux(1, [4, 5, 6])
# print product([1, 2, 3], [4, 5, 6])

# print(zipit([1, 2, 3], [4, 5, 6]))

# print(scale_list([1, 2, 3, 4, 5], 10))
