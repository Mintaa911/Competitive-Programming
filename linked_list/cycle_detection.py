def has_cycle(head):
    if not head and not head.next:
        return 0
    
    slow,fast = head,head.next.next
    
    while fast and fast.next:
        if slow == fast:
            return 1
        
        slow = slow.next
        fast = fast.next.next
        
    return 0