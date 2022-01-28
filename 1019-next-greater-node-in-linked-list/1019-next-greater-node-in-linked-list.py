# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        cur_node = head
        node_array = []
        
        while cur_node:
            node_array.append(cur_node.val)
            cur_node = cur_node.next
        
        nge = [0] * len(node_array)
        idx = 0   
        cur_node = head
        dec_array = []
        
        while cur_node:
            
            while dec_array and node_array[dec_array[-1]] < cur_node.val:
                nge[dec_array.pop()] = cur_node.val
                
            dec_array.append(idx)
            idx += 1
            cur_node = cur_node.next
        
        return nge
        
        
        
        
        