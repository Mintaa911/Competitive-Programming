# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        rem,quotient =0, 0
         
        rem = (cur_l1.val + cur_l2.val) % 10
        quotient = (cur_l1.val + cur_l2.val)//10
        cur_output = ListNode(rem)
        
        outputHead = cur_output
        
        cur_l1 = cur_l1.next
        cur_l2 = cur_l2.next
        
        while cur_l1 != None and cur_l2 != None:               
            rem = (cur_l1.val + cur_l2.val+quotient) % 10
            
            new_node = ListNode(rem)
            cur_output.next = new_node
            cur_output = new_node
            
            quotient = (cur_l1.val + cur_l2.val+quotient)//10
                
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            

        while cur_l1 != None:   
            rem = (cur_l1.val+quotient) % 10
            new_node = ListNode(rem)
            cur_output.next = new_node
            cur_output = new_node
            
            quotient = (cur_l1.val+quotient)//10
            cur_l1 = cur_l1.next

        while cur_l2 != None:             
            rem = (cur_l2.val+quotient) % 10
            new_node = ListNode(rem)
            cur_output.next = new_node
            cur_output = new_node
            
            quotient = (cur_l2.val+quotient)//10
            cur_l2 = cur_l2.next
            
        if quotient > 0:
            new_node = ListNode(quotient)
            cur_output.next = new_node
            cur_output = new_node
                
        return outputHead   
                
                
                
                