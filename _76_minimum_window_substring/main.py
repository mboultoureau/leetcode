class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        current = defaultdict(int)
        nb = 0
        left = 0
        right = 0
        bestLeft = 0
        bestLength = sys.maxsize

        while left < len(s):

            # Increment right until match or end
            while nb != len(t) and right < len(s):
                current[s[right]] += 1
                if current[s[right]] <= target[s[right]]:
                    nb += 1

                right += 1

            # Best match
            if nb == len(t) and right - left < bestLength:
                bestLeft = left
                bestLength = right - left

            # Decrement
            current[s[left]] -= 1
            if current[s[left]] < target[s[left]]:
                nb -= 1
                left += 1
                continue

            left += 1

        return "" if bestLength == sys.maxsize else s[bestLeft:bestLeft + bestLength]