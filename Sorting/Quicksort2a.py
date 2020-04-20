def quicksort(arr):
    qsort(arr, 0, len(arr) - 1)


def qsort(arr, start, end):
    if start < end:
        split_pos = partition(arr, start, end)
        qsort(arr, start, split_pos - 1)
        qsort(arr, split_pos + 1, end)


def partition(arr, start, end):
    out_arr = arr[start:end + 1]
    pivot = out_arr[0]
    out_arr = [n for n in out_arr if n < pivot] + \
              [n for n in out_arr if n == pivot] + \
              [n for n in out_arr if n > pivot]
    arr[start:end+1] = out_arr
    return start + out_arr.index(pivot)


# arr = [5, 3, 7, 1, 9]
# arr = [5, 4, 3, 2, 1]
arr = [4, 1, 8, 2, 7, 6, 5, 3]
# arr = [1,2,3,4,6,5,7,8]
# arr = [2]
# arr = [1,2]
# arr = [2,1]
quicksort(arr)
print(arr)
# print arr
# print partition(arr, 0, len(arr) - 1)
# print arr
