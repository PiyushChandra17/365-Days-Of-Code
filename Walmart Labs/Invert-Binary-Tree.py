# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursively
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

#DFS

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left,node.right = node.right,node.left
                stack.extend([node.right,node.left])
        return root

#BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                
                node.left,node.right = node.right,node.left
                queue.append(node.left)
                queue.append(node.right)
        return root