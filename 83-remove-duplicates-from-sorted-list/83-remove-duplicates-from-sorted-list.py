# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node,next_node = None,None
        
        if not head:
            return None
        
        cur_node = head
        counter = dict()
        
        while cur_node:
            next_node = cur_node.next
            
            if cur_node.val in counter:
                prev_node.next = next_node
                cur_node.next = None
            else:
                counter[cur_node.val] = 1   
                prev_node = cur_node
            cur_node = next_node
        return head