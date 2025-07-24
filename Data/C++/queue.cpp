#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    // Enqueue elements
    q.push(1);  // Queue: [1]
    q.push(2);  // Queue: [1, 2]
    q.push(3);  // Queue: [1, 2, 3]

    cout << "Front: " << q.front() << endl;  // Output: 1

    q.pop();  // Remove 1
    cout << "After pop, front: " << q.front() << endl;  // Output: 2
}
