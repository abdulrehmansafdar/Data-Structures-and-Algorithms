#include <iostream>
#include <vector>
using namespace std;
vector<int> BubbleSort(vector<int> integers)
{
    for (int i = 0; i < integers.size()-1; i++)
    {
        for (int j  = 0; j < integers.size() -i-1; j++)
        {
            if (integers[j] > integers[j+1])
            {
                int temp = integers[j];
                integers[j] = integers[j+1];
                integers[j+1] = temp;

            }
            
        }
        
    }
    return integers;
    

}
void removeDuplicates(vector<int> integers)
{
    for (int i = 0; i < integers.size(); i++)
    {
        for (int j = 0; j < integers.size(); j++)
        {
            if(integers[i] == integers[j])

            {
                integers.erase(integers.begin()+j);
                j--;

            }
        }
        
    }
    
}
int main()
{
    vector<int> integer;
    
    int opt;
    while (true)
    {
        cout<<"\n";
        cout<<"1.Add \n";
        cout<<"2.Reverse \n";
        cout<<"3.Sort in ascending \n";
        cout<<"4.Remove duplicaes \n";
        cout<<"5.Exit \n";
        cout<<"Enter option: ";
        cin>> opt;
        if (opt==1)
        {
            int value;
            cout<<"Enter a number: ";
            cin>> value;
            integer.push_back(value);

        }
        else if (opt==2)
        {
            integer.reserve(integer.size());
            for (int i = 0; i < integer.size(); i++)
            {
                cout<<integer[i]<<" ";
            }
            
        }
        else if (opt==3)
        {
            integer = BubbleSort(integer);
            cout << "Sorted in ascending order: ";
            for (int i = 0; i < integer.size(); i++)
            {
                cout << integer[i] << " ";
            }
            cout << endl;
            
        }
        else if (opt==4)
        {
            removeDuplicates(integer);
            cout << "Removed all duplicates";
            for (int i = 0; i < integer.size(); i++)
            {
                cout << integer[i] << " ";
            }
            cout << endl;

        }
        else if (opt==5)
        {
            break;
        }
        else
        {
            cout<<"Invalid option!";
            
        }
        
        
        
        
        

        
    }
    
    
    
}
