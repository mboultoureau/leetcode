class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        middle = []
        after = []

        for n in nums:
            if n < pivot:
                before.append(n)
            elif n == pivot:
                middle.append(n)
            else:
                after.append(n)

        before.extend(middle)
        before.extend(after)

        return before