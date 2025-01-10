# Search array is 2d. Rows are sorted in ascending order.
# Columns are sorted in ascending order.


def binary_search_2d2(needle, haystack):
    i = len(haystack) - 1  # last row
    j = 0  # first column
    while i > -1 and j < len(haystack[0]):
        if needle == haystack[i][j]:
            return i, j
        elif needle > haystack[i][j]:
            j += 1  # move to the right
        else:
            i -= 1  # go up
    return -1


if __name__ == '__main__':
    arr2d = [[2, 6, 10, 12],
             [3, 9, 11, 14],
             [5, 16, 19, 20]]
    print(binary_search_2d2(1, arr2d))
    print(binary_search_2d2(17, arr2d))
    print(binary_search_2d2(4, arr2d))
    print(binary_search_2d2(15, arr2d))

    print(binary_search_2d2(2, arr2d))
    print(binary_search_2d2(6, arr2d))
    print(binary_search_2d2(10, arr2d))
    print(binary_search_2d2(12, arr2d))
    print(binary_search_2d2(3, arr2d))
    print(binary_search_2d2(9, arr2d))
    print(binary_search_2d2(11, arr2d))
    print(binary_search_2d2(14, arr2d))
    print(binary_search_2d2(5, arr2d))
    print(binary_search_2d2(16, arr2d))
    print(binary_search_2d2(19, arr2d))
    print(binary_search_2d2(20, arr2d))
