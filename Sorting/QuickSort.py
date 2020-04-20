from random import randrange


def quicksort(arr):
    qsort(arr, 0, len(arr) - 1)


def qsort(arr, start, end):
    if start < end:
        part_idx = randomized_partition(arr, start, end)
        qsort(arr, start, part_idx - 1)
        qsort(arr, part_idx + 1, end)


def partition(arr, l, r):
    """
    Partition algorithm for an array. The pivot element selected in this algorithm
    is the last element of the array.  The array will be partitioned into three sets:
    those less than or equal to pivot element, those greater than pivot element,
    and a singleton set containing the pivot element.

    :param arr: array to partition
    :param l: left index, the starting point for array partitioning
    :param r: right index, the end point for array partitioning
    :return: pivot index - the final position of the pivot element
    """
    pvt_ix = l - 1  # pivot index
    for i in range(l, r):
        if arr[i] <= arr[r]:  # pivot = arr[end], the last element of arr
            pvt_ix += 1
            arr[i], arr[pvt_ix] = arr[pvt_ix], arr[i]
    pvt_ix += 1
    arr[r], arr[pvt_ix] = arr[pvt_ix], arr[r]
    return pvt_ix


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


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    quicksort(arr)
    print(arr)

    a1 = [1, 2, 3, 3, 3]
    print(partition(a1, 0, 4))
