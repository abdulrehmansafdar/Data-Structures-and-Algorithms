#include<iostream>
#include<vector>
using namespace std;
int main()
{
    vector <int> integer;
    for (int i = 1; i <=100; i++)
    {
        integer.push_back(i);
        cout<<"Capacity: "<<integer.capacity() <<endl ;
        cout<<"Size: "<<integer.size() <<endl;
    }
    
}