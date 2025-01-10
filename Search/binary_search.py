# from random import randrange
# from random_data import random_int_array
# import unittest


def binary_search(needle, haystack):
    lo = 0
    hi = len(haystack) - 1
    mid = (lo + hi) // 2

    while lo <= hi:
        if needle == haystack[mid]:
            return mid
        if needle < haystack[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
        mid = (lo + hi) // 2
    return -1


# recursive binary search
# def binary_search(needle, haystack):
#     def _binary_search(needle, haystack, start, end):
#         if start > end:
#             return -1
#
#         mid = int((start + end) / 2)
#         if needle == haystack[mid]:
#             return mid
#
#         if needle < haystack[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#         return _binary_search(needle, haystack, start, end)
#
#     return _binary_search(needle, haystack, 0, len(haystack) - 1)

# recursive binary search  - does not return position of string,
# will indicate only whether the needle exists in the haystack
#
# def binary_search(needle, haystack):
#     if haystack:
#         mid = len(haystack) / 2
#         if needle == haystack[mid]:
#             return True
#         elif needle < haystack[mid]:
#             haystack = haystack[:mid]
#         else:
#             haystack = haystack[mid + 1:]
#         return binary_search(needle, haystack)
#     return False


if __name__ == '__main__':
    # list1 = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(binary_search(3, list1))
    arr = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    print(binary_search('ddd', arr))
    # arr = []
    # print(binary_search('ddd', arr))
