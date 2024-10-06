#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<string> str;
    int option;
    while (true)
    {
        // clear the screen
        
        cout << "1. Add\n";
        cout << "2. Remove\n";
        cout << "3. Exit\n";
        cin >> option;
        if (option == 1)
        {
            string value = "";
            cout << "Enter a string to add: ";
            cin >> value;
            str.push_back(value);
            cout << "Capacity: " << str.capacity() << endl;
            cout << "Size: " << str.size() << endl;
        }
        else if (option == 2)
        {
            if (!str.empty())
            {
                str.pop_back();
                cout << "Capacity: " << str.capacity() << endl;
                cout << "Size: " << str.size() << endl;
            }
            else
            {
                cout << "No elements to remove!" << endl;
            }
        }
        else if (option == 3)
        {
            cout << "Exiting ....";
            break;
        }
        else
        {
            cout << "Invalid option!";
            break;
        }
    }
}