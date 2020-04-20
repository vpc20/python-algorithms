from collections import deque


def josephus(n, k):
    surv = deque([i for i in range(1, n + 1)])
    while len(surv) > 1:
        surv.rotate(- k + 1)
        surv.popleft()
    return surv[0]


def josephus_permutation(n, k):
    jperm = []
    surv = deque([i for i in range(1, n + 1)])
    while surv:
        surv.rotate(-k + 1)
        jperm.append(surv.popleft())
    return jperm


# [3,6,2,7,5,1,4] seq of elimination

# print(josephus(1, 2))
# print(josephus(2, 2))
# print(josephus(3, 2))
# print(josephus(4, 2))
# print(josephus(5, 2))
# print(josephus(6, 2))
# print(josephus(7, 2))
# print(josephus(8, 2))
print(josephus(41, 2))
print(josephus_permutation(41, 2))
#
# print(josephus(7, 3))
# print(josephus_permutation(7, 3))

# print(josephus(3, 5))
