class Solution(object):
    def maxPathSum(self, root):
        def find_max(node):
            if not node: return 0
            left, right = find_max(node.left), find_max(node.right)
            v = max(node.val, node.val + max(left, right))
            self.ans = max(self.ans, v, left + node.val + right)
            return v
        self.ans = None
        find_max(root)
        return self.ans