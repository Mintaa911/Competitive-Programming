# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast = head,head
        i = 1
        while i <= n:
            fast = fast.next
            i += 1
        if not slow.next:
            return slow.next
        elif not fast:
            return slow.next
        
        slow,fast = head,fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        next_node = slow.next
        slow.next = slow.next.next
        next_node.next = None
        
        return head
        