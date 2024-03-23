# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second part of the list
        current = slow.next
        prev = None

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        # Unlink two lists
        slow.next = None

        # Merge two lists
        firstList = head
        secondList = prev

        while secondList != None:
            tmp1 = firstList.next
            tmp2 = secondList.next
            firstList.next = secondList
            secondList.next = tmp1
            firstList = tmp1
            secondList = tmp2