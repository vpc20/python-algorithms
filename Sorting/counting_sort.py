def counting_sort(arr):
    count_arr = [0] * max(len(arr) + 1, max(arr)+1)
    for num in arr:
        count_arr[num] += 1
    print(count_arr)
    k = -1
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            k += 1
            arr[k] = i
    return arr


a1 = [25, 5, 4, 4, 3, 3, 2, 2, 1, 1]
print(a1)
print(counting_sort(a1))
