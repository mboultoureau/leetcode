class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        best = len(count)

        for _, nb in count.most_common()[::-1]:
            if nb > k:
                return best
            else:
                k -= nb
                best -= 1

        return best