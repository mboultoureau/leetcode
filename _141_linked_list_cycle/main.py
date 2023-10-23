# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Solution 2
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

        # Solution 1
        # if head == None or head.next == None:
        #     return False

        # slow = head
        # fast = head.next.next

        # while slow != fast and fast != None and fast.next != None:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow == fast