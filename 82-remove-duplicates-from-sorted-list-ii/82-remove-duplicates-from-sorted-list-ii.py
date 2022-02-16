# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        empty_node = ListNode()
        empty_node.next = head
        slow = head
        fast = head.next
        prev = empty_node

        
        while fast:
            if fast.val == slow.val:
                while fast and fast.val == slow.val:
                    fast = fast.next

                slow = fast
                prev.next = fast  
                
                if fast:
                    fast = fast.next 
            else:
                prev = slow
                slow = fast
                fast = fast.next
                
        return empty_node.next