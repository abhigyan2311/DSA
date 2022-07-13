class Solution:
    def preInPostorderTraversal(root):
        preorder, inorder, postorder = [], [], []
        st = []
        if not root: return
        st.append((root, 1))
        while st:
            node, category = st.pop()
            if category == 1:
                preorder.append(node.val)
                st.append((node, category+1))
                if node.left:
                    st.append((node.left, 1))
            elif category == 2:
                inorder.append(node.val)
                st.append((node, category+1))
                if node.right:
                    st.append((node.right, 1))
            else:
                postorder.append(node.val)
        
        return inorder, preorder, postorder
            

