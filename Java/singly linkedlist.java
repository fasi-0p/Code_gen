public class LinkedListExample {

    // Node class
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    // Insert node at end
    public static Node insert(Node head, int val) {
        Node newNode = new Node(val);
        if (head == null) return newNode;

        Node temp = head;
        while (temp.next != null)
            temp = temp.next;
        temp.next = newNode;
        return head;
    }

    // Reverse linked list
    public static Node reverse(Node head) {
        Node prev = null, curr = head;
        while (curr != null) {
            Node next = curr.next;  // Store next
            curr.next = prev;       // Reverse pointer
            prev = curr;
            curr = next;
        }
        return prev;
    }

    // Print list
    public static void printList(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Node head = null;

        head = insert(head, 1);
        head = insert(head, 2);
        head = insert(head, 3);

        System.out.print("Original list: ");
        printList(head);  // 1 2 3

        head = reverse(head);
        System.out.print("Reversed list: ");
        printList(head);  // 3 2 1
    }
}
