# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        next = head.next

        while next:
            newNode = ListNode(val=math.gcd(current.val, next.val), next=next)
            current.next = newNode
            current = next
            next = current.next

        return head