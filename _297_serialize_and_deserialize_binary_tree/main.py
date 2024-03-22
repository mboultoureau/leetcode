# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = deque([root])

        while queue:
            length = len(queue)
            empty = True
            line = []

            while length != 0:
                node = queue.popleft()
                if node:
                    line.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                    empty = False
                else:
                    line.append("null")
                length -= 1

            if empty:
                return ",".join(result)

            result.append(",".join(line))

        return ""
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        dataQueue = deque(data.split(","))
        headValue = dataQueue.popleft()
        headNode = TreeNode(headValue)
        nodeQueue = deque([headNode])

        while dataQueue:
            length = len(nodeQueue)
            while length:
                node = nodeQueue.popleft()
                leftVal = dataQueue.popleft()
                rightVal = dataQueue.popleft()

                if leftVal != "null":
                    leftNode = TreeNode(int(leftVal))
                    node.left = leftNode
                    nodeQueue.append(leftNode)

                if rightVal != "null":
                    rightNode = TreeNode(int(rightVal))
                    node.right = rightNode
                    nodeQueue.append(rightNode)

                length -= 1

        return headNode

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))