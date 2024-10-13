#include<iostream>
#include<vector>
using namespace std;

class AutoGrowingArray{

private:
    int *arr;
    int size;
    int capacity;
    void grow(){
        int *temp = new int[capacity*2];
        for(int i=0;i<size;i++){
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
        capacity *= 2;
    }
public:
    AutoGrowingArray(){
        arr = new int[1];
        size = 0;
        capacity = 1;
    }
    void push_back(int val){
        if(size == capacity){
            grow();
        }
        arr[size] = val;
        size++;
    }
    int get(int index){
        if(index < size){
            return arr[index];
        }
        return -1;
    }
    int get_size(){
        return size;
    }
    int get_capacity(){
        return capacity;
    }
    void print(){
        for(int i=0;i<size;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    ~AutoGrowingArray(){
        delete[] arr;
    }

    
};
int main()
{
  

}