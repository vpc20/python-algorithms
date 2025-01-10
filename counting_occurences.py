# Count the number of times a given number n occurs in a given sorted array


def count_occurences(arr, n):
    return binary_search_boundary(n, arr, right_bound=True) \
           - binary_search_boundary(n, arr, right_bound=False)


def binary_search_boundary(needle, haystack, right_bound=True):
    """
    Search for the left or right boundary of needle in haystack

    :param needle: search argument
    :param haystack: array to perform search on
    :param right_bound: True  will return the right boundary,
                        False will return left boundary
    :return: index of left or right boundary
    """
    left = 0
    right = int(len(haystack) - 1)
    mid = int((left + right) / 2)

    while left <= right:
        if right_bound:
            if needle < haystack[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if needle <= haystack[mid]:
                right = mid - 1
            else:
                left = mid + 1
        mid = int((left + right) / 2)
    return left


# def binary_search_right_boundary(needle, haystack):
#     left = 0
#     right = int(len(haystack) - 1)
#     mid = int((left + right) / 2)
#
#     while left <= right:
#         if needle < haystack[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#         mid = int((left + right) / 2)
#     return left
#
#
# def binary_search_left_boundary(needle, haystack):
#     left = 0
#     right = int(len(haystack) - 1)
#     mid = int((left + right) / 2)
#
#     while left <= right:
#         if needle <= haystack[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#         mid = int((left + right) / 2)
#     return left


# list1 = [1, 2, 4, 5, 6, 7, 8, 9, 10]
# list1 = [3, 3, 3, 3, 3, 6, 7, 8, 9, 10]

list1 = [1, 2, 3, 3, 3, 5, 6, 7, 8, 9, 10]
# list1 = [1, 3, 3, 3, 3, 3, 3, 3, 3, 10]

# print(binary_search_boundary(3, list1, right_bound=True))
# print(binary_search_boundary(3, list1, right_bound=False))
print(count_occurences(list1, 12))
