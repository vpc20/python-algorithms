class QuickUnionDS:
    def __init__(self, n):
        self.n = n
        self.qu_arr = []
        for i in range(self.n):
            self.qu_arr.append(i)
        print(self.qu_arr)

    def root(self, a):
        while self.qu_arr[a] != a:
            a = self.qu_arr[a]
        return a

    def is_connected(self, a, b):
        return self.root(a) == self.root(b)

    def union(self, a, b):
        roota = self.root(a)
        rootb = self.root(b)
        self.qu_arr[roota] = rootb
        print(self.qu_arr)


qu_data = QuickUnionDS(10)
print(qu_data.root(2))

qu_data.union(1, 2)
qu_data.union(3, 1)

# qf_data.union(1, 3)
# qf_data.union(1, 4)
# print(qf_data.is_connected(1, 2))
# print(qf_data.is_connected(1, 3))
# print(qf_data.is_connected(2, 3))
# print(qf_data.is_connected(1, 4))
print(qu_data.is_connected(1, 3))
