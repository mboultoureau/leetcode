class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 2, -1, -1):
            results[i] = 1
            j = i + 1

            while (temperatures[j] <= temperatures[i]):
                if results[j] == 0:
                    results[i] = 0
                    break

                results[i] += results[j]
                j += results[j]

        return results