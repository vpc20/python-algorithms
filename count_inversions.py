import sys


def count_inv_brute(arr):
    inv_count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def merge_count(arr, left, mid, right):
    inv_count = 0
    left_arr = []
    right_arr = []

    for i in range(mid - left):
        left_arr.append(arr[left + i])
    left_arr.append(sys.maxsize)  # sentinel value

    for j in range(right - mid):
        right_arr.append(arr[mid + j])
    right_arr.append(sys.maxsize)  # sentinel value

    i = 0
    j = 0
    for k in range(left, right):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]  # count the number of inversion for each swap
            inv_count += (mid + j) - k  # mid + j is the actual index of right_arr[j] in arr
            j += 1
    return inv_count


def count_inv(arr):
    def _merge_sort(arr, left, right):
        nonlocal total_count
        if right - left > 1:
            mid = (left + right) // 2
            _merge_sort(arr, left, mid)
            _merge_sort(arr, mid, right)
            mcount = merge_count(arr, left, mid, right)
            total_count += mcount

    total_count = 0
    _merge_sort(arr, 0, len(arr))
    return total_count


if __name__ == '__main__':
    a = [4, 3, 2, 1]
    print(count_inv_brute(a))
    print(count_inv(a))

    # a = [4, 3]
    # merge_sort(a, 0, 2)

    # a = [4]
    # merge_sort(a, 0, 1)

    # a = []
    # merge_sort(a)
    print(a)

    for i in range(10):
        arr = [i for i in range(i, -1, -1)]
        print(count_inv_brute(arr))
        print(count_inv(arr))
