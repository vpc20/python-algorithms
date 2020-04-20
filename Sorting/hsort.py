# modified insertion sort used by shell sort
def hsort(arr, h):
    for i in range(h, len(arr)):
        num = arr[i]  # number to be inserted
        j = i
        while j >= h and arr[j - h] > num:  # look for the insertion point
            arr[j] = arr[j - h]  # move values to the right to create space for the insert
            j -= h
        arr[j] = num  # actual insertion
    return arr


print(hsort(['s', 'o', 'r', 't', 'e', 'x', 'a', 'm', 'p', 'l', 'e'], 7))
print(hsort(['m', 'o', 'l', 'e', 'e', 'x', 'a', 's', 'p', 'r', 't'], 3))
print(hsort(['a', 'e', 'l', 'e', 'o', 'p', 'm', 's', 'x', 'r', 't'], 1))
