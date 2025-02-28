class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        previous = [''] * (len(str2) + 1)

        for j in range(len(str2)):
            previous[j] = str2[j:]

        for i in reversed(range(len(str1))):
            current = [''] * len(str2)
            current.append(str1[i:])

            for j in reversed(range(len(str2))):
                if str1[i] == str2[j]:
                    current[j] = str1[i] + previous[j + 1]
                else:
                    sol1 = str1[i] + previous[j]
                    sol2 = str2[j] + current[j + 1]
                    if len(sol1) > len(sol2):
                        current[j] = sol2
                    else:
                        current[j] = sol1

            previous = current

        return current[0]


    # Solution 1: TOO SLOW
    #     return self.explore(str1, str2, 0, 0)

    # @lru_cache(None)
    # def explore(self, str1: str, str2: str, i: int, j: int) -> str:
    #     if i >= len(str1):
    #         return str2[j:]

    #     if j >= len(str2):
    #         return str1[i:]

    #     if str1[i] == str2[j]:
    #         return str1[i] + self.explore(str1, str2, i + 1, j + 1)

    #     sol1 = str1[i] + self.explore(str1, str2, i + 1, j)
    #     sol2 = str2[j] + self.explore(str1, str2, i, j + 1)
    #     if len(sol1) > len(sol2):
    #         return sol2
    #     else:
    #         return sol1
