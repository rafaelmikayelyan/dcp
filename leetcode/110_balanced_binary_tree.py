# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
    
    def dfs(self, root: Optional[TreeNode]) -> list[bool, int]:
        if not root:
            return [True, 0]
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) < 2

        return [balanced, 1 + max(left[1], right[1])]
