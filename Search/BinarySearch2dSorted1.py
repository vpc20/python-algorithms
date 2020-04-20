# Search array is 2d. Rows are sorted in ascending order.
# First value of each row is greater than the last value of preceding row


def binary_search_2d1(needle, haystack):
    start = 0
    end = len(haystack) * len(haystack[0])
    mid = int((start + end) / 2)

    while start <= end:
        i, j = divmod(mid, len(haystack[0]))
        if i > len(haystack) - 1:
            return -1
        if needle == haystack[i][j]:
            return i, j
        elif needle < haystack[i][j]:
            end = mid - 1
        else:
            start = mid + 1
        mid = int((start + end) / 2)
    return -1


if __name__ == '__main__':
    arr2d = [[2, 3, 4, 5],
             [7, 8, 9, 10],
             [12, 13, 14, 15]]
    print(binary_search_2d1(1, arr2d))
    print(binary_search_2d1(16, arr2d))
    print(binary_search_2d1(6, arr2d))
    print(binary_search_2d1(11, arr2d))
    print(binary_search_2d1(2, arr2d))
    print(binary_search_2d1(3, arr2d))
    print(binary_search_2d1(4, arr2d))
    print(binary_search_2d1(5, arr2d))
    print(binary_search_2d1(7, arr2d))
    print(binary_search_2d1(8, arr2d))
    print(binary_search_2d1(9, arr2d))
    print(binary_search_2d1(10, arr2d))
    print(binary_search_2d1(12, arr2d))
    print(binary_search_2d1(13, arr2d))
    print(binary_search_2d1(14, arr2d))
    print(binary_search_2d1(15, arr2d))
