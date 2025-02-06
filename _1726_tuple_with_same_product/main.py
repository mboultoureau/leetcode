class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                products[nums[i] * nums[j]] += 1

        tuples = 0
        for product in products.values():
            tuples += 8 * ((product * (product - 1) // 2))

        return tuples