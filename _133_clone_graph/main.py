"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Solution 2
        if not node:
            return None

        visited = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            root = queue.popleft()

            for neighbor in root.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[root].neighbors.append(visited[neighbor])

        return visited[node]

        # Solution 1
        # visited = {}

        # def explore(root):
        #     nonlocal visited

        #     if root in visited:
        #         return visited[root]

        #     newNode = Node(root.val)
        #     visited[root] = newNode

        #     for neighbor in root.neighbors:
        #         newNode.neighbors.append(explore(neighbor))

        #     return newNode

        # if node:
        #     return explore(node)
        # else:
        #     return None