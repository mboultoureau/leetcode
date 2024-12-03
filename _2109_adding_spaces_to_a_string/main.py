class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        arrayIndex = 0
        strIndex = 0
        iterations = 0

        while arrayIndex < len(spaces) or strIndex < len(s):
            if arrayIndex < len(spaces) and iterations == spaces[arrayIndex] + arrayIndex:
                result.append(' ')
                arrayIndex += 1
            else:
                result.append(s[strIndex])
                strIndex += 1

            iterations += 1
        
        return ''.join(result)

        # Too slow
        # s = list(s)
        # for i in range(len(spaces)):
        #     s.insert(spaces[i] + i, ' ')

        # return ''.join(s)