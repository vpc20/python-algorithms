from itertools import permutations
from unittest import TestCase

from NextPermutation import next_permutation


class TestNextPermutation(TestCase):
    def test_next_permutation(self):
        arr = [1]
        # perm_list = list([p for p in permutations(arr)])
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))

        arr = [1, 2]
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))

        arr = [1, 2, 3]
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))

        arr = [1, 2, 3, 4]
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))

        arr = [1, 2, 3, 4, 5]
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))

        arr = [5, 4, 3, 2, 1]
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))

        arr = [1, 2, 2, 3, 3]
        perm_list = sorted(list(set(list([p for p in permutations(arr)]))))
        print(perm_list)
        for i in range(len(perm_list) - 1):
            print(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
            self.assertEqual(perm_list[i + 1], tuple(next_permutation(list(perm_list[i]))))
