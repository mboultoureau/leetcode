class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return

        if self.size[parent_x] < self.size[parent_y]:
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x]
        else:
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]

        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # With Neetcode video help: https://www.youtube.com/watch?v=jZ-RVp5CVYY
        union = UnionFind(len(nums))

        factor_index = {}
        for i, n in enumerate(nums):
            factor = 2
            while factor * factor <= n:
                if n % factor == 0:
                    if factor in factor_index:
                        union.union(i, factor_index[factor])
                    else:
                        factor_index[factor] = i

                    while n % factor == 0:
                        n = n // factor

                factor += 1

            if n > 1:
                if n in factor_index:
                    union.union(i, factor_index[n])
                else:
                    factor_index[n] = i

        return union.count == 1