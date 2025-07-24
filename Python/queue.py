from collections import deque

class Queue:
    """
    Queue Data Structure (FIFO):
    - Supports enqueue (add to end) and dequeue (remove from front).
    - Python deque gives O(1) time for both ends.
    """
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)  # Add to back

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()  # Remove from front

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]  # Front element

# ✅ Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print("Front:", q.peek())  # 1
print("Dequeued:", q.dequeue())  # 1
print("Front After Dequeue:", q.peek())  # 2
