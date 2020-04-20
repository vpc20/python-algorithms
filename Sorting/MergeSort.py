import sys


def merge(arr, left, mid, right):
    left_arr = [arr[left + i] for i in range(mid - left)] + [sys.maxsize]
    right_arr = [arr[mid + j] for j in range(right - mid)] + [sys.maxsize]

    i, j = 0, 0
    for k in range(left, right):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1


# def merge(arr, left, mid, right):
#     # left_arr = []
#     # right_arr = []
#     #
#     # for i in range(mid - left):
#     #     left_arr.append(arr[left + i])
#     # left_arr.append(sys.maxsize)  # sentinel value
#     #
#     # for j in range(right - mid):
#     #     right_arr.append(arr[mid + j])
#     # right_arr.append(sys.maxsize)  # sentinel value
#
#     i = 0
#     j = 0
#     for k in range(left, right):
#         if left_arr[i] <= right_arr[j]:
#             arr[k] = left_arr[i]
#             i += 1
#         else:
#             arr[k] = right_arr[j]
#             j += 1


def _merge_sort(arr, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        _merge_sort(arr, left, mid)
        _merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def merge_sort(arr):
    _merge_sort(arr, 0, len(arr))


if __name__ == '__main__':
    a = [4, 3, 2, 1]
    merge_sort(a)

    # a = [4, 3]
    # merge_sort(a, 0, 2)

    # a = [4]
    # merge_sort(a, 0, 1)

    # a = []
    # merge_sort(a)

    print(a)
