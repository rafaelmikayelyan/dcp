# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lowest = root

        while lowest:
            if lowest.val > p.val and lowest.val > q.val:
                lowest = lowest.left
            elif lowest.val < p.val and lowest.val < q.val:
                lowest = lowest.right
            else:
                return lowest
