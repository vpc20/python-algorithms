def matrix_multiply(a, b):
    c = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = 0
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c


if __name__ == '__main__':
    a = [[1, 2, 3],
         [4, 5, 6]]
    b = [[2, 3],
         [4, 5],
         [6, 7]]
    print(matrix_multiply(a, b))
