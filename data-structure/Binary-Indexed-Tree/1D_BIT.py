class Binary_Indexed_Tree:
    def __init__(self, n) -> None:
        self._n = n
        self.data = [0] * (n+1)
        self.depth = n.bit_length()

    def add(self, p, x) -> None:
        """任意の要素ai←ai+xを行う O(logn)"""
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p-1] += x
            p += p & (-p)
    
    def sum(self, l, r) -> int:
        """区間[l,r)で計算"""
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    
    def _sum(self, d) -> int:
        sm = 0
        while d > 0:
            sm += self.data[d-1]
            d -= d & (-d)
        return sm
    
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self._n and sum_ + self.data[k-1] < x:
                sum_ += self.data[k-1]
                pos += 1 << i
        return pos, sum_

n = 8
data = [0, 1, 2, 3, 4, 5, 6, 7]
BIT = Binary_Indexed_Tree(n)
for idx, num in enumerate(data):
    BIT.add(idx, num)
print(BIT._sum(3))
print(BIT._sum(5))
print(BIT.sum(2, 4)) # 5
print(BIT.sum(6, 7)) # 6
BIT.add(2, 6) # a[2]+=6
BIT.add(5, -1)
print(BIT.sum(0, 3)) # 9
print(BIT.sum(3, 7)) # 17
