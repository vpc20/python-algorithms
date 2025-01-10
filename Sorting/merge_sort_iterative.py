# Iterative mergesort function to
# sort arr[0...n-1]


def merge_sort(a):
    if len(a) > 1:
        step = 2
        prev_step = step
        while step <= len(a):
            for l in range(0, len(a), step):
                r = l + step - 1
                m = int((l + r) / 2)
                if r > len(a) - 1:
                    r = len(a) - 1
                if m > r:
                    m = r
                merge(a, l, m, r)
            prev_step = step
            step *= 2
        merge(a, 0, prev_step - 1, len(a) - 1)


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


# a = [12, 11, 13, 5, 6, 7]
# a = [2, 1,4,3,6]
a = [7, 2, 1, 8, 4, 9,  5, 10, 3, 6]

# a = [567, -213, 336, 237, 654, -782, 821, 489, -740, 887, -953, 756, 918, 533]
# a = [-193, -188, -569, -326, 415, -109, -671, 57, 805, 216, -132]
merge_sort(a)
print(a)
