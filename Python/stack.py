class Stack:
    """
    Stack Data Structure (LIFO):
    - Supports push (add to top) and pop (remove from top).
    - Uses Python list internally.
    - Time Complexity: O(1) for push/pop
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)  # Add element to top

    def pop(self):
        if self.is_empty():
            return None  # Return None if stack is empty
        return self.stack.pop()  # Remove top element

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]  # Return top element without removing

    def is_empty(self):
        return len(self.stack) == 0

# ✅ Example
s = Stack()
s.push(10)
s.push(20)
print("Top:", s.peek())  # 20
print("Popped:", s.pop())  # 20
print("Top After Pop:", s.peek())  # 10
