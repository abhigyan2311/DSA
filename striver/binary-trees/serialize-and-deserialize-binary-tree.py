# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue


class Codec:
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     serializedStr = ""
    #     q = Queue()
    #     q.put(root)
    #     while q.qsize() > 0:
    #         curr = q.get()
    #         if not curr: serializedStr += "#,"
    #         else: 
    #             serializedStr += str(curr.val) + ","
    #             q.put(curr.left)
    #             q.put(curr.right)

    #     if serializedStr[-1] == ",": serializedStr = serializedStr[:-1]
    #     return serializedStr

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     serializedStr = str(data)
    #     if not serializedStr: return None
    #     serializedArr = serializedStr.split(",")
    #     if serializedArr[0] == "#": return None
    #     root = TreeNode(int(serializedArr[0]))
    #     i = 1
    #     q = Queue()
    #     q.put(root)
    #     while q.qsize()>0:
    #         curr = q.get()
    #         if serializedArr[i] != "#":
    #             newLeftNode = TreeNode(int(serializedArr[i]))
    #             curr.left = newLeftNode
    #             q.put(newLeftNode)
    #         i += 1
    #         if serializedArr[i] != "#":
    #             newRightNode = TreeNode(int(serializedArr[i]))
    #             curr.right = newRightNode
    #             q.put(newRightNode)
    #         i += 1
    #     return root

    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append("#")
        vals = []
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        def preorder():
            val = next(vals)
            if val == "#":
                return None
            else:
                node = TreeNode(int(val))
                node.left = preorder()
                node.right = preorder()
            return node
        vals = iter(data.split())
        return preorder()
        
root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = ser.serialize(root)
print(ans)
# ans = deser.deserialize(ans)
# print(ans)
# ans = deser.deserialize(ser.serialize(root))