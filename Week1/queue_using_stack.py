from collections import deque
class MyQueue:
    
    def __init__(self):
        self.dque = deque([],100)
    
    def push(self, x: int) -> None:
        self.dque.append(x)

    def pop(self) -> int:
        if len(self.dque) > 0:
            return self.dque.popleft()

    def peek(self) -> int:
        if len(self.dque) > 0:
            return list(self.dque)[0]

    def empty(self) -> bool:
        return len(self.dque) == 0