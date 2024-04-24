# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        previous = dummy
        current = head

        while current and current.next:
            next = current.next

            # The next node to visit
            previous.next = next
            current.next = next.next
            next.next = current

            # Reaffect
            previous = current
            current = current.next

        return dummy.next