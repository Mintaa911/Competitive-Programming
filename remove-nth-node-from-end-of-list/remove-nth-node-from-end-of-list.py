# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        empty_node = ListNode()
        slow,fast = empty_node,empty_node
        slow.next, fast.next = head,head
        
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        
        
        fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        next_node = slow.next
        slow.next = next_node.next
        next_node.next = None
        
        return empty_node.next
        