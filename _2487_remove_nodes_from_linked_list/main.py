# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 2
        current = head
        stack = deque([])

        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()

            stack.append(current)
            current = current.next

        if not stack:
            return None

        next = None
        while stack:
            current = stack.pop()
            current.next = next
            next = current

        return current


        # Solution 1
        # current = head
        # stack = deque([])

        # while current:
        #     while stack and stack[-1].val < current.val:
        #         stack.pop()

        #     stack.append(current)
        #     current = current.next

        # if not stack:
        #     return None

        # head = stack.popleft()
        # current = head
        # while stack:
        #     node = stack.popleft()
        #     current.next = node
        #     current = current.next

        # return head




        # Solution 3 : Too slow...
        # dummy = ListNode()
        # dummy.next = head

        # previous = dummy
        # current = head

        # while current.next:
        #     if current.next.val > current.val:
        #         previous.next = current.next
        #         previous = dummy
        #         current = dummy.next
        #     else:
        #         previous = current
        #         current = current.next

        # return dummy.next