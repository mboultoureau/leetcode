# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Add new node at left
        list1 = ListNode(val=0, next=list1)

        b = b - a + 2

        # Get the a node
        aNode = list1

        while a != 0:
            aNode = aNode.next
            a -= 1

        # Get the b node
        bNode = aNode

        while b != 0:
            bNode = bNode.next
            b -= 1

        # Get the end of list2
        end = list2
        while end.next:
            end = end.next

        aNode.next = list2
        end.next = bNode

        return list1.next