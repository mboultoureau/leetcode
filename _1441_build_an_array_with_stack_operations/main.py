class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            result.append("Push")
            
            if i not in target:
                result.append("Pop")

            if i == target[-1]:
                return result

        # result = []
        # stack = []

        # for i in range(1, n + 1):
        #     stack.append(i)
        #     result.append("Push")
            
        #     if stack[-1] not in target:
        #         stack.pop()
        #         result.append("Pop")

        #     if stack == target:
        #         return result