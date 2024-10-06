#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> integer;
    for (int i = 1; i < 1000; i++)
    {
        integer.push_back(i);
    }
    int value;
    cout<<"Enter a number to search: ";
    cin>> value;
    bool isfound = false;
    for (int j = 0; j < integer.size(); j++)
    {

        if(integer[j] == value)
        {
            cout<<"Number is at index: " << j<<endl;
            isfound = true;
            break;
        }
        
    }
    if(!isfound)
    {
        cout<<"404 not found" <<endl;
    }
    
    

    
}