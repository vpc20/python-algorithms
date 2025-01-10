class QuickFindDS:
    # def __init__(self, n):
    #     self.n = n
    #     self.qf_arr = []
    #     for i in range(n):
    #         self.qf_arr.append(i)
    #     print(self.qf_arr)
    #
    # def is_connected(self, a, b):
    #     return self.qf_arr[a] == self.qf_arr[b]
    #
    # def union(self, a, b):
    #     aval = self.qf_arr[a]
    #     bval = self.qf_arr[b]
    #     for i in range(self.n):
    #         if self.qf_arr[i] == aval:
    #             self.qf_arr[i] = bval
    #     print(self.qf_arr)

    def __init__(self, n):
        self.connections = [i for i in range(n)]

    def union(self, a, b):
        aconn = self.connections[a]
        bconn = self.connections[b]
        for i in range(len(self.connections)):
            if self.connections[i] == aconn:
                self.connections[i] = bconn

    def is_connected(self, a, b):
        return self.connections[a] == self.connections[b]

qf_data = QuickFindDS(10)
qf_data.union(1, 2)
qf_data.union(1, 3)
qf_data.union(1, 4)
print(qf_data.is_connected(1, 2))
print(qf_data.is_connected(1, 3))
print(qf_data.is_connected(2, 3))
print(qf_data.is_connected(1, 4))
print(qf_data.is_connected(1, 5))
