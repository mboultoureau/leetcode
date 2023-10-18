# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        merged = ListNode()
        current = merged
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                newNode = ListNode(val=list1.val)
                current.next = newNode
                current = newNode
                list1 = list1.next
            else:
                newNode = ListNode(val=list2.val)
                current.next = newNode
                current = newNode
                list2 = list2.next

        if list1 == None:
            current.next = list2
        else:
            current.next = list1

        return merged.next
