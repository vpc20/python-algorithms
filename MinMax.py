# Find both the minimum and the maximum of a set of n elements
import sys
from datetime import datetime
from random import randrange


def min_max(arr):
    minval = sys.maxsize
    maxval = -sys.maxsize

    for num in arr:
        if num < minval:
            minval = num
        if num > maxval:
            maxval = num
    return minval, maxval


def min_max1(arr):
    if len(arr) % 2 == 0:
        if arr[0] < arr[1]:
            minval = arr[0]
            maxval = arr[1]
        else:
            minval = arr[1]
            maxval = arr[0]
        start = 2
    else:
        minval = arr[0]
        maxval = arr[0]
        start = 1

    for i in range(start, len(arr), 2):
        if arr[i] < arr[i + 1]:
            if arr[i] < minval:
                minval = arr[i]
            if arr[i + 1] > maxval:
                maxval = arr[i + 1]
        else:
            if arr[i] > maxval:
                maxval = arr[i]
            if arr[i + 1] < minval:
                minval = arr[i + 1]
    return minval, maxval


# arr = [5, 1, 3, 7, 9, 2, 10, 4, 8, 6]
# arr = [1, 5, 3, 7, 9, 2, 10, 4, 8, 6]
# arr = [5, 1, 3, 7, 9, 2, 4, 8, 6]
# arr = [1, 5, 3, 7, 9, 2, 4, 8, 6]
# arr = [5]
# arr = [5, 5]
# arr = [6, 5]
# arr = [5, 6]
arr = [randrange(1, 100000) for _ in range(1000000)]
print(datetime.now())
print(min_max(arr))
print(datetime.now())

print(datetime.now())
print(min_max1(arr))
print(datetime.now())
# print((min(arr), max(arr)))
