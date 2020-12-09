#Recursively
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
                
            self.connect(root.left)
            self.connect(root.right)
        return root


#DFS

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return 
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)
        return root

#BFS

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root