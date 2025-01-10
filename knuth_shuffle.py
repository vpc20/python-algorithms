from random import randrange


def knuth_shuffle(arr):
    for i in range(1, len(arr)):
        r = randrange(i + 1)
        arr[i], arr[r] = arr[r], arr[i]


arr = [1, 2, 3, 4, 5]
knuth_shuffle(arr)
print(arr)

