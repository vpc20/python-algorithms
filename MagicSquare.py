from itertools import permutations
from random import shuffle


def is_magic_square(arr):
    n = len(arr)
    magic_sum = n * (n ** 2 + 1) // 2

    sum_diag1 = 0  # diagonals ↘
    sum_diag2 = 0  # diagonals ↙
    for i in range(n):
        sum_row = 0
        sum_col = 0
        for j in range(n):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        if sum_row != magic_sum or sum_col != magic_sum:
            return False

        sum_diag1 += arr[i][i]
        sum_diag2 += arr[i][n - 1 - i]

    return sum_diag1 == magic_sum and sum_diag2 == magic_sum  # check diagonals ↘ and ↙


def is_magic_square1(arr):
    n = len(arr)
    magic_sum = n * (n ** 2 + 1) // 2
    transposed = [[arr[j][i] for j in range(n)] for i in range(n)]

    if not all([sum(subarr) == magic_sum for subarr in arr]) or \
            not all([sum(subarr) == magic_sum for subarr in transposed]) or \
            sum([arr[i][i] for i in range(n)]) != magic_sum or \
            sum([arr[i][n - 1 - i] for i in range(n)]) != magic_sum:
        return False
    return True


def is_magic_square2(arr):
    n = len(arr)
    magic_sum = n * (n ** 2 + 1) // 2
    transposed = [[arr[j][i] for j in range(n)] for i in range(n)]

    if not all(map(lambda e: sum(e) == magic_sum, arr)) or \
            not all(map(lambda e: sum(e) == magic_sum, transposed)) or \
            sum(map(lambda i: arr[i][i], range(n))) != magic_sum or \
            sum(map(lambda i: arr[i][n - 1 - i], range(n))) != magic_sum:
        return False
    return True


def magic_square(n):
    arr = [num for num in range(1, n ** 2 + 1)]
    for perm in permutations(arr):
        # square_arr = [perm[i:i + n] for i in range(0, len(perm), n)]
        square_arr = [perm[i * n:i * n + n] for i in range(n)]
        # print(square_arr)
        if is_magic_square(square_arr):
            # assert is_magic_square(square_arr) == is_magic_square1(square_arr)
            # assert is_magic_square(square_arr) == is_magic_square2(square_arr)
            print('magic square')
            for item in square_arr:
                print(item)


def magic_square_random(n):
    arr = [num for num in range(1, n ** 2 + 1)]
    while True:
        shuffle(arr)
        square_arr = [arr[i:i + n] for i in range(0, len(arr), n)]
        if is_magic_square(square_arr):
            print('magic square')
            for item in square_arr:
                print(item)
            break


if __name__ == '__main__':
    # arr = [[8, 1, 6],
    #        [3, 5, 7],
    #        [4, 9, 2]]
    # print(is_magic_square(arr))

    print(magic_square(3))
    # print(magic_square(4))
