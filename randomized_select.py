from random import randrange


def randomized_partition(arr, l, r):
    """
    Randomized partition algorithm for an array. This is the same as the partition
    function used in quicksort except that it uses a random value for its pivot.
    The array will be partitioned into three sets: those less than or equal to pivot element,
    those greater than pivot element, and a singleton set containing the pivot element.

    :param arr: array to partition
    :param l: left index, the starting point for array partitioning
    :param r: right index, the end point for array partitioning
    :return: pivot index - the final position of the pivot element
    """
    rnd = randrange(l, r + 1)  # random pivot
    arr[r], arr[rnd] = arr[rnd], arr[r]

    pvt_ix = l - 1  # pivot index
    for i in range(l, r):
        if arr[i] <= arr[r]:  # pivot = arr[end], the last element of arr
            pvt_ix += 1
            arr[i], arr[pvt_ix] = arr[pvt_ix], arr[i]
    pvt_ix += 1
    arr[r], arr[pvt_ix] = arr[pvt_ix], arr[r]
    return pvt_ix


def randomized_select(arr, i):
    """
    Select the ith order statistic from a set of n distinct numbers.
    The ith order statistic of a set of n elements is the ith smallest element. For
    example, the minimum of a set of elements is the first order statistic (i = 1),
    and the maximum is the nth order statistic (i = n).

    :param arr: a set of n numbers
    :param i: position of the element to look for in the array --> 1 <= i <= n
    :return: the ith element in the array
    """

    def _randomized_select(arr, left, right, i):
        pvt_ix = randomized_partition(arr, left, right)
        if i - 1 == pvt_ix:
            return arr[pvt_ix]
        elif i - 1 < pvt_ix:
            return _randomized_select(arr, left, pvt_ix - 1, i)
        else:
            return _randomized_select(arr, left + 1, right, i)

    if not arr or i < 1 or i > len(arr):
        return None
    return _randomized_select(arr, 0, len(arr) - 1, i)


def randomized_select_iter(arr, i):
    if not arr or i < 1 or i > len(arr):
        return None
    left = 0
    right = len(arr) - 1
    while True:
        pvt_ix = randomized_partition(arr, left, right)
        if i - 1 == pvt_ix:
            return arr[pvt_ix]
        elif i - 1 < pvt_ix:
            right = pvt_ix - 1
        else:
            left += 1


if __name__ == '__main__':
    print(randomized_select([1], 1))
    print(randomized_select([2], 1))
    print(randomized_select([3], 1))
    #
    print(randomized_select([1, 2], 1))
    print(randomized_select([1, 2], 2))
    #
    print(randomized_select([1, 2, 3], 1))
    print(randomized_select([1, 2, 3], 2))
    print(randomized_select([1, 2, 3], 3))
    #
    print(randomized_select([1, 2, 3, 4], 1))
    print(randomized_select([1, 2, 3, 4], 2))
    print(randomized_select([1, 2, 3, 4], 3))
    print(randomized_select([1, 2, 3, 4], 4))
    #
    print(randomized_select([1, 2, 3, 4, 5], 1))
    print(randomized_select([1, 2, 3, 4, 5], 2))
    print(randomized_select([1, 2, 3, 4, 5], 3))
    print(randomized_select([1, 2, 3, 4, 5], 4))
    print(randomized_select([1, 2, 3, 4, 5], 5))

    print(randomized_select([], 1))
    print(randomized_select([1], 2))
