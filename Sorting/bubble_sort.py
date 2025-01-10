import unittest


# def bubble_sort(lst):
#     for i in range(len(lst) - 1):
#         for j in range(len(lst) - 1 - i):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


if __name__ == '__main__':
    # arr = []
    # arr = [2, 1]
    # arr = [3, 2, 1]
    arr = [2, 4, 1, 3]
    bubble_sort(arr)
    print(arr)
