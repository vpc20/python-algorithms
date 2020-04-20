# Count the negative numbers in row/columnwise sorted matrix


def count_negative(matrix):
    count = 0
    for subarr in matrix:
        left = 0
        right = int(len(subarr) - 1)
        mid = int((left + right) / 2)

        while left <= right:
            if 0 <= subarr[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = int((left + right) / 2)
        count += left  # left will contain the index of the leftmost zero
    return count


# matrix = [[-3, -2, -1, 1],
#           [-2, 2, 3, 4],
#           [4, 5, 7, 8]]
# matrix = [[-3, -2, -1, 1],
#           [-2, -1, 3, 4],
#           [4, 5, 7, 8]]
matrix = [[-3, -2, -1, 1],
          [-2, -1, 3, 4],
          [-1, 5, 7, 8]]
# matrix = [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0]]
# matrix = [[-1, -1, -1, -1],
#           [-1, -1, -1, -1],
#           [-1, -1, -1, -1]]
print(count_negative(matrix))
