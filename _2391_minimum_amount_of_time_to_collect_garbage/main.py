class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        metal = 0
        paper = 0
        glass = 0

        for i in range(len(garbage) - 1, -1, -1):
            for c in garbage[i]:
                if c == "M":
                    metal += 1
                elif c == "P":
                    paper += 1
                else:
                    glass += 1

            if i <= 0:
                continue
            
            if metal != 0:
                metal += travel[i - 1]
            
            if paper != 0:
                paper += travel[i - 1]

            if glass != 0:
                glass += travel[i - 1]

        return metal + paper + glass