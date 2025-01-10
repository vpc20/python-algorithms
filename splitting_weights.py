# Split weights into two sets of equal weights
# NP-complete problem, no known polynomial time solution
from itertools import combinations


def split_weights(arr):
    set_idx = set(range(len(arr)))
    for r in range(1, (len(arr) // 2) + 1):
        for comb in combinations(range(len(arr)), r):
            set1_idx = set(comb)
            set2_idx = set_idx.difference(set1_idx)
            set1_elems = [arr[i] for i in set1_idx]
            set2_elems = [arr[j] for j in set2_idx]
            if sum(set1_elems) == sum(set2_elems):
                return set1_elems, set2_elems, sum(set1_elems)
    return None


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 7]
    # arr = [1, 2, 3, 4, 5]
    print(split_weights(arr))
