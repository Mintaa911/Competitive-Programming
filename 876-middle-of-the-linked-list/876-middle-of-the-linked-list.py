# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        cur_node = head
        
        while cur_node != None:
            counter += 1
            cur_node = cur_node.next
            
        cur_node = head
        
        middle = (counter // 2)
        i = 0
        while i < middle:
            cur_node = cur_node.next
            i += 1
        return cur_node