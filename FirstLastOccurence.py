# Find the first occurence of n in a sorted array
def first_occurence(arr, n):
    left = 0
    right = int(len(arr) - 1)
    mid = int((left + right) / 2)

    while left <= right:
        if n <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = int((left + right) / 2)
    return left


# Find the last occurence of n in an array
def last_occurence(arr, n):
    left = 0
    right = int(len(arr) - 1)
    mid = int((left + right) / 2)

    while left <= right:
        if n < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = int((left + right) / 2)
    return right


# arr = [1, 2, 3, 4, 5]
arr = [1, 2, 3, 3, 3, 4, 5]
# arr = [3, 3, 3, 4, 5, 6]
# arr = [1, 2, 3, 3, 3]
print(first_occurence(arr, 3))
print(last_occurence(arr, 3))
