class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 0
        for length in range(len(strs[0])):
            for i in range(1, len(strs)):
                if len(strs[i]) < length + 1 or strs[i][length] != strs[0][length]:
                    return strs[0][:length]


        return strs[0][:length + 1]
    

        # length = 0
        # while True:
        #     if len(strs[0]) < length + 1:
        #         return strs[0][:length]

        #     character = strs[0][length]

        #     for i in range(1, len(strs)):
        #         if len(strs[i]) < length + 1 or strs[i][length] != character:
        #             return strs[0][:length]

        #     length += 1