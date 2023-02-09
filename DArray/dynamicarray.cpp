#include<iostream>
using namespace std; 

class DynamicArray
{
    private:int* arr;
            int len; 
            int capacity; 

    public: DynamicArray()
            {
                this->arr = new int[4]; 
                len=0;
                capacity=4; 
                for(int i=0; i<4;i++)
                {
                    arr[i]=0; 
                }
            }
            DynamicArray(int capacity)
            {
                if(capacity<=0)
                {
                    cerr<<"Illegal capacity: "<<capacity; 
                }

                this->capacity=capacity;
                arr= new int[capacity]; 
                len=0;
            }
            int GetSize() {return len;}
            void GetMemSize()
            {
                cout<<(sizeof(arr))<<endl;
            }
            int Get(int index){return arr[index];}
            int Set(int index, int val){return arr[index]=val;}

            bool isFull()
            {
                if(len==capacity) return true;
                return false;
            }
            bool isEmpty()
            {
                if(len==0) return true;
                return false;
            }

            void Display()
            {
                for(int i=0;i<len;i++)
                {
                    cout<<arr[i]<<"\t"; 
                }
                cout<<endl;
            }      

            void Clear()
            {
                while(len--)
                {
                    arr[len]=0; 
                }
            }
            void Add(int ele)
            {
                if(len==capacity)
                {
                    GrowArray(); 
                }
                arr[len]=ele; 
                len++;
            }


            void Remove()
            {
                arr[len]=0;
                len--;
                if(len ==capacity/2)
                {
                    ShrinkArray();
                }
            }
            void RemoveAtIndex(int index)
            {
                if(index>=len)
                {
                    cerr<<"Failed to remove: Index Exceeded.";
                    return;
                }
                for (int i = index; i < len; i++) {
                    arr[i] = arr[i + 1];
                }
                arr[len] = 0;
                len--;
                if (len == (capacity / 2)) {
                    ShrinkArray();
                }
            }
            void AddAtIndex(int index, int ele)
            {
                if(index>=len){
                    cerr<<"\nExceeded Length: "; 
                    Add(ele);
                }
                if(len ==capacity)
                {
                    GrowArray();
                }

                for(int i=len-1;i>=index;i--)
                {
                    arr[i+1]=arr[i];
                }

                arr[index]=ele;
            }

    private:void GrowArray()
            {
                int*temp = new int[capacity*2];   
                capacity*=2;

                for(int i=0;i<len;i++)
                {
                    temp[i]=arr[i];
                }

                delete []arr; 
                arr=temp; 
                cout<<"ECapacity:"<<capacity<<":"<<arr<<endl;
            }

            void ShrinkArray()
            {
                int*temp= new int[capacity/2];
                capacity/=2;
                for(int i=0;i<len;i++)
                {
                    temp[i]=arr[i];
                }
                delete []arr; 
                arr=temp; 
                cout<<"SCapacity:"<<capacity<<":"<<arr<<endl;
            }
};

int main()
{
    DynamicArray der(1);
        
    der.Add(5);
    der.Add(4);
    
    der.Display();
   
    der.Add(3);
    der.Add(2);
    
    der.Display();
    der.Add(69);
    der.Add(64);
    der.Display();
    der.AddAtIndex(5,4); 
    der.AddAtIndex(6,0); 
    der.Display();
    der.RemoveAtIndex(0); 
    der.Display();
    der.RemoveAtIndex(4); 
    der.Display();
    der.RemoveAtIndex(7); 
    der.Display();
    der.RemoveAtIndex(3); 
    der.Display();
    
    return 0; 
}