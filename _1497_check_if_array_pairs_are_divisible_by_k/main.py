class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        table = defaultdict(int)
        for n in arr:
            table[n % k] += 1

        for value, count in table.items():
            if table[(k - value) % k] != count:
                return False

            if (k - value) % k == value and count % 2 != 0:
                return False

        return True 