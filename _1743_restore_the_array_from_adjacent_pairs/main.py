class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        numbers = defaultdict(list)

        for pair in adjacentPairs:
            numbers[pair[0]].append(pair[1])
            numbers[pair[1]].append(pair[0])

        end_candidates = []
        for key, value in numbers.items():
            if len(value) == 1:
                end_candidates.append(key)
        
        nums = [end_candidates[0]]
        while nums[-1] != end_candidates[1]:
            nums.append(numbers[nums[-1]][0])
            numbers[nums[-1]].remove(nums[-2])

        return nums

        # Solution 1: too slow...
        # numbers = {}
        # end_candidates = []

        # for pair in adjacentPairs:
        #     if pair[0] in numbers:
        #         numbers[pair[0]].append(pair[1])
        #         end_candidates.remove(pair[0])
        #     else:
        #         numbers[pair[0]] = [pair[1]]
        #         end_candidates.append(pair[0])

        #     if pair[1] in numbers:
        #         numbers[pair[1]].append(pair[0])
        #         end_candidates.remove(pair[1])
        #     else:
        #         numbers[pair[1]] = [pair[0]]
        #         end_candidates.append(pair[1])

        # nums = [end_candidates[0]]
        # while nums[-1] != end_candidates[1]:
        #     nums.append(numbers[nums[-1]][0])
        #     numbers[nums[-1]].remove(nums[-2])

        # return nums