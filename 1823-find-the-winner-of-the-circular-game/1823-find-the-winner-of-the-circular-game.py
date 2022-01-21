class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = Node(1)
        cur_node = head
        if n == 1:
            return 1
        
        for i in range(2,n+1):
            node = Node(i)
            cur_node.next = node
            cur_node = cur_node.next
        
        cur_node.next = head
        dirty_fix = cur_node
        prev,count,cur_node = None,1,head
        
        while cur_node.next:
            if count == k:
                if not prev:
                    next_node = cur_node.next
                    if next_node.next.value == cur_node.value:
                        next_node.next = None
                    cur_node.next = None
                    if dirty_fix.value != next_node.value:
                        dirty_fix.next = next_node
                    cur_node = next_node
                elif prev.value == cur_node.next.value:
                    cur_node = prev
                    prev.next = None
                    cur_node.next = None
                else:
                    next_node = cur_node.next
                    prev.next = next_node
                    cur_node = next_node
                count = 1                    
            else:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
        return cur_node.value
                    
       
        
        
