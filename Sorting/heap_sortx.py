def heapify(lst):
    lst_len = heap_size = len(lst)

    for i in range(lst_len - 1, -1, -1):  # max heapify, bottom-up
        print('curr idx - max heapify - bottom up ', i)
        larger_idx = i  # sift down
        while True:
            curr_idx = larger_idx

            left_idx = 2 * curr_idx + 1
            if left_idx >= lst_len: # no left and right child
                break

            right_idx = 2 * curr_idx + 2
            if right_idx >= lst_len: # no right child, left child only
                larger_idx = left_idx
            elif lst[left_idx] > lst[right_idx]: # has both left and right child
                larger_idx = left_idx
            else:
                larger_idx = right_idx

            if lst[curr_idx] < lst[larger_idx]: # swap values if the child has larger value
                lst[curr_idx], lst[larger_idx] = lst[larger_idx], lst[curr_idx]

    print(lst)
    # sort


lst = [1, 2, 3, 4, 5, 6, 7]
# lst = [7,6,5,4,3,2,1]
heapify(lst)
