names = ['Adam', 'Bart', 'Charlie', 'Annie', 'Beth', 'Claire', 'Allan', 'Brad', 'Cain', 'Agnes']
group_size = 3


# for i, name in enumerate(names):
#     print name, i % group_size + 1,
# print ''

# n is number of groups
def group_by(arr, n):
    group_arr = [[] for i in range(n)]
    for i, e in enumerate(arr):
        group_arr[i % n].append(e)
    return group_arr


# n is the size of the group
def group_by_size(arr, n):
    group_arr = []
    for i, e in enumerate(arr):
        q, r = divmod(i, n)
        if r == 0:
            group_arr.append([])
        group_arr[q].append(e)
    return group_arr


# def group_by(arr, n):
#     return [[e for j, e in enumerate(arr) if j % n == i] for i in range(n)]

# def group_by(arr, n):
#     result = []
#     for i in range(n):
#         group_list = [e for j, e in enumerate(arr) if j % n == i]
#         result.append(group_list)
#     return result


# def group_by(arr, n):
#     result = []
#     for i in range(n):
#         group_list = []
#         for j, e in enumerate(arr):
#             if j % n == i:
#                 group_list.append(e)
#         result.append(group_list)
#     return result

# def group_by(arr, n):
#     # out_arr = [['' for _ in range(len(arr) / n + 1)] for _ in range(n)]
#     q, r = divmod(len(arr), n)
#     out_arr = []
#     for _ in range(n):
#         blank_arr = []
#         for j in range(len(arr) / n + 1):
#             if j == len(arr) / n:
#                 if r != 0:
#                     blank_arr.append('')
#                     r -= 1
#             else:
#                 blank_arr.append('')
#         out_arr.append(blank_arr)
#     print out_arr
#
#     for i, e in enumerate(names):
#         q, r = divmod(i, n)
#         out_arr[r][q] = e
#     return out_arr


print(group_by(names, 4))
print(group_by_size(names, 2))

# n = 3
# size = 10
# print [['x'] * 4] * n

# out_arr = [['x'] * 4] * 4 # this does not work
# out_arr = [['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x']]

# arr1 = [[0] * 4] * 2 # this does not work
# print arr1
# arr1[0][0] = 1 # this updates arr1[0][0] and arr1[1][0]
# print arr1
