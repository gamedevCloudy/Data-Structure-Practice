#include<iostream>

using namespace std;

struct  Node
{
    int val;
    Node* prev;
};

class Stack
{
    private: Node* top;
            Node*base;
            int height;

    public: Stack()
            {
                top=NULL;
                base=NULL;
                height=0;
            }   

            Stack(int value)
            {
                top->val=value;
                base=top;
                height=1;
            }

            void Push(int value)
            {
                Node* temp = new Node();
                temp->val=value;

                if(isEmpty())
                {
                    top=temp;
                    base=top;

                }
                else{
                    base=top;
                    top=temp;
                    top->prev=base;
                }

                height++;
                
            }

            void Pop()
            {
                if(isEmpty())
                {
                    cerr<<"\nSTACK IS EMPTY"<<endl;
                    return;
                }
                else{
                    if(height==1)
                    {
                        Node*t=base;

                        top=base=new Node();
                        delete t;
                    }
                    else{

                        Node*temp=top;
                        if(base->prev!=NULL)
                            base=base->prev;
                        if(top->prev !=NULL)
                        {
                            top=top->prev;
                            delete temp;
                        }
                        
                    }
                }

                height--;
                cout<<"After REMOVAL: TOP: "<<top->val<<"\t"<<"BASE: "<<base->val<<"\tHEIGHT: "<<height<<endl;
            }

            int PeekTop()
            {
                if(isEmpty()) {
                    cerr<<"EMPTY"<<endl;
                    return -1;
                }
                return top->val;
            }

            bool isEmpty()
            {
                if(height==0) return true;
                return false;
            }


};

int main()
{
    Stack st;
    st.Push(5);
    cout<<st.PeekTop()<<endl;
    st.Push(6);
    cout<<st.PeekTop()<<endl;
    st.Push(7);
    cout<<st.PeekTop()<<endl;
    st.Pop();
    cout<<st.PeekTop()<<endl;
    st.Pop();
    cout<<st.PeekTop()<<endl;
    st.Pop();
    st.Pop();
    cout<<st.PeekTop()<<endl;
    st.Push(7);
    cout<<st.PeekTop()<<endl;
    

    return 0;
}