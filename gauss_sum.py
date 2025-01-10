# write a function to return the sum of numbers from 1 to n

from functools import reduce


# def gauss_sum_naive(n):
#     gsum = 0
#     for i in range(1, n + 1):
#         gsum += i
#     return gsum


# def gauss_sum_naive(n):
#     return reduce(lambda x, y: x + y, range(1, n + 1))


def gauss_sum_naive(n):
    return sum([i for i in range(1, n + 1)])


def gauss_sum_recur(n):
    if n < 2:
        return n
    return n + gauss_sum_recur(n - 1)


def gauss_sum(n):
    return (n + 1) * int(n / 2)


print(gauss_sum_naive(100))
print(gauss_sum_recur(100))
print(gauss_sum(100))
