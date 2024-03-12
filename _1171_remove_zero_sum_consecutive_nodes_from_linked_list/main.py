# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        prefixSums = {0: newHead}
        prefixSum = 0

        while head:
            prefixSum += head.val
            prefixSums[prefixSum] = head
            head = head.next

        head = newHead
        prefixSum = 0
        while head:
            prefixSum += head.val
            head.next = prefixSums[prefixSum].next
            head = head.next

        return newHead.next
