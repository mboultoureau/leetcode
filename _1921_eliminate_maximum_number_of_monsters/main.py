class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Reuse same array to save some memory
        dist = [math.ceil(dist[i] / speed[i]) for i in range(len(dist))]
        dist.sort()

        for i in range(1, len(dist)):
            if dist[i] - i <= 0:
                return i

        return len(dist)