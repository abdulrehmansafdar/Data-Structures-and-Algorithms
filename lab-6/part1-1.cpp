#include<iostream>
using namespace std;
template <typename T> 
class Node
{
    public:
        T data;
        Node* next;
        Node(T data){this->data = data; next = NULL;}
    
};
template <typename T>
class LinkList
{
private:
    /* data */
    Node<T>* head;
    int size;
public:
    LinkList(void){head = NULL;size = 0; }
    ~LinkList(void){
        // delete all  nodes in the list
        Node<T>* temp = head;
        while (temp != NULL)
        {
            Node<T>* next = temp->next;
            delete temp;
            temp = next;
        }
        head = NULL;
    }
    bool isEmpty(){
        return head == NULL;
    }
    Node<T>* insertNode(int index, T data)
    {
        if (index < 0 || index > size)
        {
            return NULL;
        }
        Node<T>* newNode = new Node<T>(data);
        if (index == 0)
        {
            newNode->next = head;
            head = newNode;
        }
        else
        {
            Node<T>* temp = head;
            for (int i = 0; i < index - 1; i++)
            {
                temp = temp->next;
            }
            newNode->next = temp->next;
            temp->next = newNode;
        }
        size++;
        return newNode;
    }
    Node<T>* insertAtHead(T data)
    {
        return insertNode(0, data);
    }
    Node<T>* insertAtEnd(T data)
    {
        return insertNode(size, data);
    }
    bool findNode(T data)
    {
        Node<T>* temp = head;
        while (temp != NULL)
        {
            if (temp->data == data)
            {
                return true;
            }
            temp = temp->next;
        }
        return false;
    }
    bool deleteNode(T data)
    {
        Node<T>* temp = head;
        if (temp->data == data)
        {
            head = temp->next;
            delete temp;
            size--;
            return true;
        }
        while (temp->next != NULL)
        {
            if (temp->next->data == data)
            {
                Node<T>* del = temp->next;
                temp->next = temp->next->next;
                delete del;
                size--;
                return true;
            }
            temp = temp->next;
        }
        return false;
    }
    void display(void)
    {
        Node<T>* temp = head;
        while (temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
    bool DeleteFromStart()
    {
        if (head == NULL)
        {
            return false;
        }
        Node<T>* temp = head;
        head = head->next;
        delete temp;
        size--;
        return true;
    }
    
    bool DeleteFromEnd()
    {
        if (head == NULL)
        {
            return false;
        }
         if (head->next == NULL) { // Handle case where there is only one node
            delete head;
            head = NULL;
            size--;
            return true;
        }
        Node<T>* temp = head;
        while (temp->next->next != NULL)
        {
            temp = temp->next;
        }
        delete temp->next;
        temp->next = NULL;
        size--;
        return true;
    }
    Node<T> * reverseList()
    {
        Node<T>* prev = NULL;
        Node<T>* current = head;
        Node<T>* next = NULL;
        while (current != NULL)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
        return head;
    }
    Node<T> * sortList()
    {
        Node<T>* temp1 = head;
        Node<T>* temp2 = NULL;
        T temp;
        while (temp1 != NULL)
        {
            temp2 = temp1->next;
            while (temp2 != NULL)
            {
                if (temp1->data > temp2->data)
                {
                    temp = temp1->data;
                    temp1->data = temp2->data;
                    temp2->data = temp;
                }
                temp2 = temp2->next;
            }
            temp1 = temp1->next;
        }
        return head;
    }
    Node<T> * mergeList(Node<T> *list1, Node<T> *list2)
    {
        Node<T>* temp = list1;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = list2;
        return list1;
    }
    Node<T> * removeDuplicates(Node<T> *LinkList)
    {
        Node<T> * temp1 = LinkList;
        Node<T> * temp2 = NULL;
        Node<T> * temp3 = NULL;
        while (temp1 != NULL && temp1->next != NULL)
        {
            temp2 = temp1;
            while (temp2->next != NULL)
            {
                if (temp1->data == temp2->next->data)
                {
                    temp3 = temp2->next;
                    temp2->next = temp2->next->next;
                    delete temp3;
                }
                else
                {
                    temp2 = temp2->next;
                }
            }
            temp1 = temp1->next;
        }
        return LinkList;
    }
    Node<T> * interestList(Node<T> *list1, Node<T> *list2)
    {
        Node<T>* temp1 = list1;
        Node<T>* temp2 = list2;
        Node<T>* result = NULL;
        Node<T>* temp = NULL;
        while (temp1 != NULL && temp2 != NULL)
        {
            if (temp1->data == temp2->data)
            {
                if (result == NULL)
                {
                    result = new Node<T>(temp1->data);
                    temp = result;
                }
                else
                {
                    temp->next = new Node<T>(temp1->data);
                    temp = temp->next;
                }
                temp1 = temp1->next;
                temp2 = temp2->next;
            }
            else if (temp1->data < temp2->data)
            {
                temp1 = temp1->next;
            }
            else
            {
                temp2 = temp2->next;
            }
        }
        return result;
    }

};


    


int main()
{
    LinkList<int> list;
    list.insertNode(0, 1);
    list.insertAtEnd(1);
    list.insertAtEnd(2);
    list.insertAtEnd(3);
    list.insertAtEnd(4);
    list.insertAtEnd(5);
    list.insertAtEnd(6);
    list.insertAtEnd(7);
    list.insertAtEnd(8);
    list.insertAtEnd(9);
    list.insertAtEnd(10);
    list.display();
    list.reverseList();
    list.display();
    list.sortList();
    list.display();
    list.DeleteFromStart();
    list.display();
    list.DeleteFromEnd();
    list.display();

}