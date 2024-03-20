# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # With NeetCode video solution
        dummy = ListNode(val=0, next=head)
        previousGroup = dummy

        while True:
            # Get kth element
            kth = self.getKth(previousGroup, k)
            if not kth:
                break
            nextGroup = kth.next

            # Reverse group
            previous, current = kth.next, previousGroup.next
            while current != nextGroup:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp

            # Link group
            tmp = previousGroup.next
            previousGroup.next = kth
            previousGroup = tmp

        return dummy.next

    def getKth(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1

        return current
