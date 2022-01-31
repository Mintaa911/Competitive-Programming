# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow_ptr = ListNode() 
        slow_ptr.next = head
        fast_ptr = head.next
        head = slow_ptr
        while fast_ptr:
         
            fast_nxt = fast_ptr.next
            slow_nxt = slow_ptr.next
            
            slow_ptr.next = fast_ptr
            fast_ptr.next = slow_nxt
            slow_nxt.next = fast_nxt
            fast_ptr = slow_nxt
            
            gap = 0
            while fast_ptr and gap < 2:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
                
                gap += 1
    
        return head.next
    
    
    '''
        using fast and slow pointer, with gap of two
        slow pointer start at dummy node 
        fast pointer start at head.next
        
        move the pointers to right most till fast pointer rich None
        
        in every traverse
            fast_nxt = fast.next
            slow_nxt = slow.next
            slow.next = fast
            slow.next.next = slow_nxt
            slow_nxt.next = fast_nxt
            
    '''