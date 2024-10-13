#include <iostream>
using namespace std;

template <typename T>
class StackArray {
private:
    T* arr;
    int top;
    int capacity;

public:
    StackArray(int size) {
        arr = new T[size];
        capacity = size;
        top = -1;
    }

    ~StackArray() {
        delete[] arr;
    }

    void push(T data) {
        if (top == capacity - 1) {
            cout << "Stack Overflow" << endl;
            return;
        }
        top++;
        arr[top] = data;
    }

    T pop() {
        if (top == -1) {
            cout << "Stack Underflow" << endl;
            exit(EXIT_FAILURE);
        }
        
        T value = arr[top];
        top--;
        return value;
       
    }

    T peek() {
        if (top != -1) {
            return arr[top];
        } else {
            exit(EXIT_FAILURE);
        }
    }

    bool isEmpty() {
        return top == -1;
    }

    int size() {
        return top + 1;
    }
};
template <typename T>
class QueueArray {
private:
    T* arr;
    int front;
    int rear;
    int capacity;
    int count;

public:
    QueueArray(int size) {
        arr = new T[size];
        capacity = size;
        front = 0;
        rear = -1;
        count = 0;
    }

    ~QueueArray() {
        delete[] arr;
    }

    void enqueue(T data) {
        if (count == capacity) {
            cout << "Queue Overflow" << endl;
            return;
        }
        rear = (rear + 1) % capacity;
        arr[rear] = data;
        count++;
    }

    T dequeue() {
        if (count == 0) {
            cout << "Queue Underflow" << endl;
            exit(EXIT_FAILURE);
        }
        T data = arr[front];
        front = (front + 1) % capacity;
        count--;
        return data;
    }

    T peek() {
        if (count != 0) {
            return arr[front];
        } else {
            exit(EXIT_FAILURE);
        }
    }

    bool isEmpty() {
        return count == 0;
    }

    int size() {
        return count;
    }
};

int main()
{
    StackArray<int> stack(5);
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.push(5);

    cout << "Top element is: " << stack.peek() << endl;
    cout << "Stack size is " << stack.size() << endl;

    cout << stack.pop() << " Popped from stack\n";

    cout << "Top element is: " << stack.peek() << endl;
    cout << "Stack size is " << stack.size() << endl;

    QueueArray<int> queue(5);
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);

    cout << "Front element is: " << queue.peek() << endl;
    cout << "Queue size is " << queue.size() << endl;

    cout << queue.dequeue() << " Dequeued from queue\n";

    cout << "Front element is: " << queue.peek() << endl;
    cout << "Queue size is " << queue.size() << endl;

    return 0;
}