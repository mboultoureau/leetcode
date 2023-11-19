"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        newHead = Node(head.val)
        newPrevious = newHead
        current = head.next

        correspondances = {}
        correspondances[head] = newHead

        while current:
            newNode = Node(current.val)
            newPrevious.next = newNode
            newPrevious = newNode
            correspondances[current] = newNode
            current = current.next

        newCurrent = newHead
        current = head

        while current:
            if current.random:
                newCurrent.random = correspondances[current.random]
            newCurrent = newCurrent.next
            current = current.next

        return newHead