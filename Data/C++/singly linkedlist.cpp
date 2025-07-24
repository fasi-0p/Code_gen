#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }
};

void insertAtEnd(Node*& head, int val) {
    Node* newNode = new Node(val);

    if (!head) {
        head = newNode;
        return;
    }

    Node* curr = head;
    while (curr->next) curr = curr->next;
    curr->next = newNode;
}

void reverse(Node*& head) {
    Node* prev = nullptr;
    Node* curr = head;
    Node* next;

    while (curr) {
        next = curr->next;     // Store next
        curr->next = prev;     // Reverse pointer
        prev = curr;           // Move prev forward
        curr = next;           // Move curr forward
    }
    head = prev;
}

void printList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
}

// ✅ Use-case
int main() {
    Node* head = nullptr;
    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);

    cout << "Original List: ";
    printList(head);  // 10 20 30

    reverse(head);
    cout << "\nReversed List: ";
    printList(head);  // 30 20 10
}
