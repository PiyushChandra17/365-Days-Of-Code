# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val < root.val:
            return self.inorderSuccessor(root.left,p) or root
        return self.inorderSuccessor(root.right,p)


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val < root.val:
            return self.inorderSuccessor(root.left,p) or root
        return self.inorderSuccessor(root.right,p)