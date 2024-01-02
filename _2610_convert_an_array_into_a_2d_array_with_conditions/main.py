class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Solution 2
        count = Counter(nums)
        result = [[] for _ in range(count.most_common(1)[0][1])]

        for value, count in count.items():
            for i in range(count):
                result[i].append(value)

        return result

        # Solution 1
        # nums.sort()
        # result = [[nums[0]]]

        # row = 0
        # for i in range(1, len(nums)):
        #     if result[row][-1] == nums[i]:
        #         row += 1
        #         if row >= len(result):
        #             result.append([nums[i]])
        #         else:
        #             result[row].append(nums[i])
        #     else:
        #         row = 0
        #         result[row].append(nums[i])
        
        # return result
