class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        for row in range(len(nums)):
            for column in range(len(nums[row])):
                diagonals[row + column].append(nums[row][column])

        result = []
        for key in diagonals:
            for value in reversed(diagonals[key]):
                result.append(value)

        return result