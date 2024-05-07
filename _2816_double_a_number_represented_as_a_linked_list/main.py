# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)

        acc = 0
        current = ListNode(next=head)
        
        while current.next:
            sum = current.next.val * 2 + acc
            current.next.val = sum % 10
            acc = (sum - current.next.val) // 10
            current = current.next

        if acc != 0:
            current.next = ListNode(val=acc)

        head = self.reverse(head)

        return head

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev
