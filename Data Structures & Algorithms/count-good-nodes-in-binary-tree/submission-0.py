# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curMax):
            if not node:
                return 0
            if node.val >= curMax:
                count = 1
            else:
                count = 0
            
            curMax = max(curMax, node.val)

            count += dfs(node.left, curMax)
            count += dfs(node.right, curMax)
            return count

        return dfs(root, root.val)



        