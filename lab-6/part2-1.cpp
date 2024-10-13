#include<iostream>
#include<stack>
using namespace std;

int main()
{
    stack<char> charstack;
    string reversed ="";
    string input ="I am from University of Engineering and Technology Lahore";
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] != ' ')
        {
            charstack.push(input[i]);
        }
        else
        {
            while (!charstack.empty())
            {
                reversed += charstack.top();
                charstack.pop();
            }
            reversed += ' ';
        }
        
    }
    // cout << reversed << endl;
    while (!charstack.empty())
    {
        reversed += charstack.top();
        charstack.pop();
    }
    // cout << reversed << endl;
    stack<char> wordstack;
    string final ="";
    for (int i = 0; i < reversed.length(); i++)
    {
        wordstack.push(reversed[i]);
    }
    while (!wordstack.empty())
    {
        final += wordstack.top();
        wordstack.pop();
    }
    cout << final << endl;
    
    

    return 0;
    
}