#include<iostream>
#include<stack>
using namespace std;

int main()
{
    cout<<"\n.......Stack Calculator.....\n";
    cout<<"1.Enter an integer to add..\n";
    cout<<"2.Enter that operand for calculation\n";
    cout<<"3.Enter ? to display..\n";
    cout<<"4.Enter ^ to remove top element..\n";
    cout<<"5.Enter ! to exit..\n";
    stack<int> myStack;
    
    string input;
    while (true)
    {
        cout << "Enter an integer or operand: ";
        cin >> input;
        // convert string to integer if possible otherwise return 0
        if (input == "?")
        {
            // display all elements in stack
            stack<int> tempStack = myStack;
            while (!tempStack.empty())
            {
                cout << tempStack.top() << " ";
                tempStack.pop();
            }
        }
        else if (input == "^")
        {
            //remove top element from stack and display it
            int temp = myStack.top();
            myStack.pop();
            cout << "Removed element is: " << temp << endl;
        }
        else if (input == "!")
        {
            break;
        }
        else if(input == "+")
        {
           int sum = 0;
           int a = myStack.top();
              myStack.pop();
              int b = myStack.top();
                myStack.pop();
                sum = a + b;
                myStack.push(sum);    
        }
        
        else if(input == "-")
        {
           int sub = 0;
           int a = myStack.top();
              myStack.pop();
              int b = myStack.top();
                myStack.pop();
                sub = a - b;
                myStack.push(sub);    
        }
        
        else if(input == "*")
        {
           int mul = 0;
           int a = myStack.top();
              myStack.pop();
              int b = myStack.top();
                myStack.pop();
                mul = a * b;
                myStack.push(mul);    
        }
       
        else if(input == "/")
        {
           int mul = 0;
           int a = myStack.top();
              myStack.pop();
              int b = myStack.top();
                myStack.pop();
                mul = a / b;
                myStack.push(mul);    
        }
        
        else if(input == "%")
        {
           int mul = 0;
           int a = myStack.top();
              myStack.pop();
              int b = myStack.top();
                myStack.pop();
                mul = a % b;
                myStack.push(mul);    
        }
        else
        {
            try
            {
                int num = stoi(input);
                myStack.push(num);
                
            }
            catch(const std::exception& e)
            {
                cout << "Invalid input" << endl;
            }
            
        }

       
       
        
    }

}
