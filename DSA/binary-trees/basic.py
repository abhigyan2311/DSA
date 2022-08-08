from queue import Queue
from typing import List

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
    # O(N), O(N)
    def insert(self, val) -> None:
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    # O(N), O(N)
    def preorder(self, root, preorder) -> None:
        if root == None: return
        preorder.append(root.val)
        self.preorder(root.left, preorder)
        self.preorder(root.right, preorder)
    
    # O(N), O(N)
    def inorder(self, root, inorder) -> None:
        if root == None: return
        self.inorder(root.left, inorder)
        inorder.append(root.val) 
        self.inorder(root.right, inorder)
    
    # O(N), O(N)
    def postorder(self, root, postorder) -> None:
        if root == None: return
        self.postorder(root.left, postorder)
        self.postorder(root.right, postorder)
        postorder.append(root.val)
    
    # O(N), O(N)
    def levelorder(self, root):
        levelorder = []
        if root is None: return levelorder
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            level = []
            for _ in range(size):
                node = q.get()
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
                level.append(node.val)
            levelorder.append(level)
        return levelorder
    
    # O(N), O(N)
    def iterPreorder(self, root) -> List[int]:
        preorder = []
        if root is None: return preorder
        st = []
        st.append(root)
        while(st):
            root = st.pop()
            preorder.append(root.val)
            if root.right: st.append(root.right)
            if root.left: st.append(root.left)
        return preorder
    
    def iterInorder(self, root) -> List[int]:
        inorder = []
        if root is None: return inorder
        st = []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            inorder.append(root.val)
            root = root.right
        return inorder

    def iterPostorder2Stacks(self, root) -> List[int]:
        postorder = []
        if root is None: return postorder
        st1, st2 = [], []
        st1.append(root)
        while st1:
            root = st1.pop()
            st2.append(root)
            if root.left: st1.append(root.left)
            if root.right: st1.append(root.right)
        while st2:
            postorder.append(st2.pop().val)
        return postorder
    
    def iterPostorder1Stack(self, root) -> List[int]:
        postorder = []
        if root is None: return postorder
        st = []
        curr = root
        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                temp = st[-1].right
                if temp:
                    curr = temp
                else:
                    temp = st.pop()
                    postorder.append(temp.val)
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        postorder.append(temp.val)
        return postorder

    def preInPostorder(self, root):
        preorder, inorder, postorder = [], [], []
        if root is None: return
        st = []
        st.append([root, 1])
        while st:
            node = st.pop()
            if node[1] == 1:
                preorder.append(node[0].val)
                node[1] += 1
                st.append(node)
                if node[0].left:
                    st.append([node[0].left, 1])
            elif node[1] == 2:
                inorder.append(node[0].val)
                node[1] += 1
                st.append(node)
                if node[0].right:
                    st.append([node[0].right, 1])
            else:
                postorder.append(node[0].val)

        return preorder, inorder, postorder

        

root = TreeNode(10)
root.insert(20)
root.insert(5)
root.insert(6)
root.insert(7)

print("Preorder:")
preorder = []
root.preorder(root, preorder)
print(preorder)

print("Inorder:")
inorder = []
root.inorder(root, inorder)
print(inorder)

print("Postorder:")
postorder = []
root.postorder(root, postorder)
print(postorder)

print("Level order:")
print(root.levelorder(root))


print("##### Iterative #####")
print("Preorder:")
print(root.iterPreorder(root))
print("Inorder:")
print(root.iterInorder(root))
print("Postorder:")
print(root.iterPostorder2Stacks(root))
print("Postorder:")
print(root.iterPostorder1Stack(root))
print("Pre/In/Postorder:")
print(root.preInPostorder(root))