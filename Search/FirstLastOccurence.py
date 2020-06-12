# Find the first occurence of n in a sorted array
def first_occurence(arr, n):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if n <= arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


# Find the last occurence of n in a sorted array
def last_occurence(arr, n):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if n < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi


arr = [1, 2, 3, 4, 5]
assert first_occurence(arr, 1) == 0
assert first_occurence(arr, 2) == 1
assert first_occurence(arr, 3) == 2
assert first_occurence(arr, 4) == 3
assert first_occurence(arr, 5) == 4

arr = [3, 3, 3, 4, 5, 6]
assert first_occurence(arr, 3) == 0
assert last_occurence(arr, 3) == 2
assert last_occurence(arr, 4) == 3
assert last_occurence(arr, 5) == 4
assert last_occurence(arr, 6) == 5

arr = [1, 2, 3, 3, 3]
assert first_occurence(arr, 3) == 2
assert last_occurence(arr, 3) == 4
assert first_occurence(arr, 1) == 0
assert last_occurence(arr, 1) == 0
assert first_occurence(arr, 2) == 1
assert last_occurence(arr, 2) == 1

arr = [1, 2, 3, 3, 3, 4, 5]
assert first_occurence(arr, 3) == 2
assert last_occurence(arr, 3) == 4
