class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to next node

class LinkedList:
    """
    Singly Linked List:
    - Supports insert at end and reversing the list.
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node  # First node
            return
        current = self.head
        while current.next:
            current = current.next  # Traverse to end
        current.next = new_node  # Insert at end

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        self.head = prev  # New head is the last node

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

# ✅ Example
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print("Linked List:", ll.display())  # [1, 2, 3]
ll.reverse()
print("Reversed List:", ll.display())  # [3, 2, 1]
