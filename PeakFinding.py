def slow_peak_find(a):
    for i in range(len(a)):
        if i == 0:
            if a[i] >= a[i + 1]:
                return i
        else:
            if i == len(a) - 1:
                if a[i] >= a[i - 1]:
                    return i
            elif a[i] >= a[i - 1] and a[i] >= a[i + 1]:
                return i


# a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# a1 = [1, 8, 3, 6, 5, 4, 7, 2, 9]
# a1 = [9, 2, 7, 4, 5, 6, 3, 8, 1]
a1 = [1, 3, 5, 7, 9, 8, 6, 4, 2]
print(slow_peak_find(a1))
