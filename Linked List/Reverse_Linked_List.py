#Iteratively
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None,head
        while cur:
            cur.next,cur,prev = prev,cur.next,cur
        return prev

#Recursively

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head,None)
    def helper(self,head,node):
        if not head:
            return node
        tmp = head.next
        head.next = node
        return self.helper(tmp,head)