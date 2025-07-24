#include <iostream>
#include <stack>
using namespace std;

// ✅ Use-case of built-in stack
int main() {
    stack<int> st;

    // Push elements onto stack
    st.push(10);  // Stack: [10]
    st.push(20);  // Stack: [10, 20]
    st.push(30);  // Stack: [10, 20, 30]

    cout << "Top element: " << st.top() << endl;  // Output: 30

    st.pop();  // Remove 30
    cout << "After pop, top: " << st.top() << endl;  // Output: 20
}
