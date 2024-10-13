#include <iostream>
using namespace std;


template <typename T>
class StackNode {
public:
    T data;
    StackNode* next;
    StackNode(T data) {
        this->data = data;
        this->next = nullptr;
    }
};

template <typename T>
class StackLinkedList {
private:
    StackNode<T>* top;

public:
    StackLinkedList() {
        top = nullptr;
    }

    ~StackLinkedList() {
        while (top != nullptr) {
            StackNode<T>* temp = top;
            top = top->next;
            delete temp;
        }
    }

    void push(T data) {
        StackNode<T>* newNode = new StackNode<T>(data);
        newNode->next = top;
        top = newNode;
    }

    T pop() {
        if (top == nullptr) {
            cout << "Stack Underflow" << endl;
            exit(EXIT_FAILURE);
        }
        StackNode<T>* temp = top;
        top = top->next;
        T data = temp->data;
        delete temp;
        return data;
    }

    T peek() {
        if (top != nullptr) {
            return top->data;
        } else {
            exit(EXIT_FAILURE);
        }
    }

    bool isEmpty() {
        return top == nullptr;
    }
};
template <typename T>
class QueueNode {
public:
    T data;
    QueueNode* next;
    QueueNode(T data) {
        this->data = data;
        this->next = nullptr;
    }
};

template <typename T>
class QueueLinkedList {
private:
    QueueNode<T>* front;
    QueueNode<T>* rear;

public:
    QueueLinkedList() {
        front = nullptr;
        rear = nullptr;
    }

    ~QueueLinkedList() {
        while (front != nullptr) {
            QueueNode<T>* temp = front;
            front = front->next;
            delete temp;
        }
    }

    void enqueue(T data) {
        QueueNode<T>* newNode = new QueueNode<T>(data);
        if (rear == nullptr) {
            front = rear = newNode;
            return;
        }
        rear->next = newNode;
        rear = newNode;
    }

    T dequeue() {
        if (front == nullptr) {
            cout << "Queue Underflow" << endl;
            exit(EXIT_FAILURE);
        }
        QueueNode<T>* temp = front;
        front = front->next;
        if (front == nullptr) {
            rear = nullptr;
        }
        T data = temp->data;
        delete temp;
        return data;
    }

    T peek() {
        if (front != nullptr) {
            return front->data;
        } else {
            exit(EXIT_FAILURE);
        }
    }

    bool isEmpty() {
        return front == nullptr;
    }
};

// driver code
int main() {
    StackLinkedList<int> stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.push(5);

    cout << "Top element is: " << stack.peek() << endl;

    cout << "Stack: ";
    while (!stack.isEmpty()) {
        cout << stack.pop() << " ";
    }
    cout << endl;

    QueueLinkedList<int> queue;
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);

    cout << "Front element is: " << queue.peek() << endl;

    cout << "Queue: ";
    while (!queue.isEmpty()) {
        cout << queue.dequeue() << " ";
    }
    cout << endl;

    return 0;
}