import unittest


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j > -1 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:  # look for the insertion point
            arr[j] = arr[j - 1]  # move values to the right to create space for the insert
            j -= 1
        arr[j] = key



if __name__ == '__main__':
    # arr = []
    # arr = [1]
    # arr = [5, 2]
    # arr = [5, 2, 4]
    # arr = [5, 2, 4, 6]
    # arr = [5, 2, 4, 6, 1]
    arr = [5, 2, 4, 6, 1, 3]
    insertion_sort(arr)
    print(arr)
