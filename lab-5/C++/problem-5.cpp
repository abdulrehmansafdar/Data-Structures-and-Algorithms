// #include<iostream>
// #include<vector>
// using namespace std;
// void AddRowsandColumns(vector<vector<int>> matrix)
// {
//     int sum = 0;
//     for (int i = 0; i < matrix.size(); i++)
//     {
//         for (int j = 0; j < matrix[i].size(); j++)
//         {
//             sum += matrix[i][j];
//         }
//         matrix[i].push_back(sum);
//         sum = 0;
//     }
//     for (int i = 0; i < matrix[0].size(); i++)
//     {
//         for (int j = 0; j < matrix.size(); j++)
//         {
//             sum += matrix[j][i];
//         }
//         vector<int> row = matrix[matrix.size()-1];
//         row.push_back(sum);
//         matrix.push_back(row);
//         sum = 0;
//     }
//     for (int i = 0; i < matrix.size(); i++)
//     {
//         for (int j = 0; j < matrix[i].size(); j++)
//         {
//             cout << matrix[i][j] << " ";
//         }
//         cout << endl;
//     }
// }
// int main()
// {
//     // 2d vector of integers matrix
//     vector<vector<int>> matrix;
//     int rows, cols;
//     cout << "Enter number of rows: ";
//     cin >> rows;
//     cout << "Enter number of columns: ";
//     cin >> cols;
//     for (int i = 0; i < rows; i++)
//     {
//         vector<int> row;
//         for (int j = 0; j < cols; j++)
//         {
//             int value;
//             cout << "Enter value for [" << i << "][" << j << "]: ";
//             cin >> value;
//             row.push_back(value);
//         }
//         matrix.push_back(row);
//     }
//     AddRowsandColumns(matrix);
    
// }
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    vector<vector<int>> matrix;
    int rows;
    int columns;
    cout<<"Enter the number of rows: ";
    cin>>rows;
    cout<<"Enter the number of columns: ";
    cin>>columns;
    for (int i = 0; i < rows; i++)
    {
        vector<int> row;
        for (int j = 0; j < columns; j++)
        {
            int value;
            cout<<"Enter value for [" << i<<"] ["<<j<<"]: ";
            cin>> value;
            row.push_back(value);
        }
        matrix.push_back(row);
        
    }
    cout<<"Your Matrix is: \n";
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size(); j++)
        {
            cout<<matrix[i][j]<<" ";
        }
        cout<<"\n";
    }
    
    cout<<"\n1.Add Rows\n";
    cout<<"2.Add Columns\n";
    cout<<"3.Transpose\n";
    int option;
    cout<<"Enter the option: ";
    cin>>option;
    if (option==1)
    {
        int sum =0;
        for (int i = 0; i <matrix.size(); i++)
        {
            for (int j = 0; j < matrix[i].size(); j++)
            {
                sum = sum + matrix[i][j];
            }
            matrix[i].push_back(sum);
            sum =0;
            
        }
        
    }
    
    else if (option==2)
    {
        int sum = 0;
        for (int i = 0; i < matrix[0].size(); i++)
        {
            for (int j = 0; j < matrix.size(); j++)
            {
                sum += matrix[j][i];
            }
            vector<int> row = matrix[matrix.size()-1];
            row.push_back(sum);
            matrix.push_back(row);
            sum = 0;
        }
        cout<<"Matrix after adding columns: \n";
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[i].size(); j++)
            {
                cout<<matrix[i][j]<<" ";
            }
            cout<<"\n";
        }
        
    }
    else if (option==3)
    {
        vector<vector<int>> transpose;
        for (int i = 0; i < matrix[0].size(); i++)
        {
            vector<int> row;
            for (int j = 0; j < matrix.size(); j++)
            {
                row.push_back(matrix[j][i]);
            }
            transpose.push_back(row);
        }
        cout<<"Matrix after transpose: \n";
        for (int i = 0; i < transpose.size(); i++)
        {
            for (int j = 0; j < transpose[i].size(); j++)
            {
                cout<<transpose[i][j]<<" ";
            }
            cout<<"\n";
        }

        
    }
    




}