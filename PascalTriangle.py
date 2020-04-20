

# def pascal(n):
#     """Prints out n rows of Pascal's triangle.
#     It returns False for failure and True for success."""
#     row = [1]
#     k = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [l + r for l, r in zip(row + k, k + row)]
#         # return n>=1


def pascal(n):
    row = [1]
    for _ in range(n):
        print(row)
        row = [sum(e) for e in zip(row + [0], [0] + row)]


pascal(5)

# print(list(zip([1, 4, 6, 4, 1, 0],
#                [0, 1, 4, 6, 4, 1])))
#                 1  5 10 10  5  1  <-- next row
