# Describe a Θ(n lg n)-time algorithm that, given a set/list S of n integers and another
# integer x, determines whether or not there exist two elements in S whose sum is
# exactly x.

# returns the indexes of the numbers


def sum_in_array_brute(arr, x):
    len_list1 = len(arr)
    for i in range(len_list1):
        for j in range(i + 1, len_list1):
            if x == arr[i] + arr[j]:
                return i, j
    return -1, -1


def sum_in_array(arr, x):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        sum_lr = arr[left] + arr[right]
        if sum_lr == x:
            return left, right
        elif sum_lr > x:
            right -= 1
        else:
            left += 1
    return -1, -1


# def sum_in_array_linear(arr, x):
#     seen = {}
#     for i, num in enumerate(arr):
#         diff = x - num
#         if diff in seen:
#             return seen[diff], i
#         seen[num] = i
#     return -1, -1


def sum_in_array_linear(arr, x):
    seen = {}
    for i, num in enumerate(arr):
        if num in seen:
            return seen[num], i
        if x - num not in seen:
            seen[x - num] = i
    return -1, -1


# return true or false
def sum_in_array1(arr, x):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        if x - num not in seen:
            seen.add(x - num)
    return False


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_in_array_brute(a, 12))
print(sum_in_array(a, 12))
print(sum_in_array_linear(a, 12))
print(sum_in_array1(a, 12))
