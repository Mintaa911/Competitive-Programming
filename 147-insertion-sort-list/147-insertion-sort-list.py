# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head and not head.next:
            return head
        
        dummy_head = ListNode(-5001,head)
        last_sorted = head
        cur_node = head.next
        
        while cur_node:
            
            if cur_node.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                prev_node = dummy_head
                while prev_node.next.val <= cur_node.val:
                    prev_node = prev_node.next

                last_sorted.next = cur_node.next

                cur_node.next = prev_node.next
                prev_node.next = cur_node
            
            cur_node = last_sorted.next
            
        return dummy_head.next
            
        '''
            cur_node: head
            
            tranverse the linked list
                traverse the linked list starting from the head up to the cur_node
                    swap every time condition met
                
            
        '''