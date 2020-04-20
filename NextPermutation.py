def next_permutation(arr):
    if isinstance(arr, str):  # process strings as array
        arr = list(arr)

    i = len(arr) - 1
    while i > 0 and arr[i] <= arr[i - 1]:  # get inverse point
        i -= 1
    if i == 0:  # array is already the last permutation
        return arr
    inv_point = i - 1

    while i < len(arr) and arr[inv_point] < arr[i]:  # get the index for swapping with inv point
        i += 1
    swap_idx = i - 1

    arr[inv_point], arr[swap_idx] = arr[swap_idx], arr[inv_point]  # swap

    return arr[:inv_point + 1] + list(reversed(arr[inv_point + 1:]))  # reverse the remaining
    # elements after the inverse point


if __name__ == '__main__':
    # arr = [9, 1, 2, 4, 3, 1, 0]
    # arr = [9, 1, 2, 4, 4, 1, 0]
    # arr = [9, 1, 2, 4, 3, 2, 2]
    # arr = [9, 8, 7, 6]
    # arr = [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 5, 4]
    # arr = [1]
    # arr = 'abcde'
    print(next_permutation(arr))
