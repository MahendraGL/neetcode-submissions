# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l_d = [0]
        def h(root):
            if not root:
                return 0

            diameter  = h(root.left) + h(root.right)
            l_d[0] = max(diameter, l_d[0])

            return (1 + max(h(root.left), h(root.right)))

        h(root)
        return l_d[0]
