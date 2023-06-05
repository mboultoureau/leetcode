# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numbers = []
        while head != None:
            numbers.append(head.val)
            head = head.next

        length = len(numbers)
        for i in range(length // 2):
            if numbers[i] != numbers[length - i - 1]:
                return False

        return True