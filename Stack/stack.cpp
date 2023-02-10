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

                if(top==NULL)
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
                if(height==0)
                {
                    cerr<<"NOT PRESENT!"<<endl;
                    return;
                }
                if(height==1)
                {
                    cout<<"1H"<<endl;
                    base=top=NULL;
                    return;
                }
                else if(height==2)
                {
                    return;
                    top=top->prev;

                }
                else{
                    Node*temp=top;
                    base=base->prev;
                    top=top->prev;
                    delete temp;
                }
                cout<<"TOP: "<<top->val<<"\t"<<"BASE: "<<base->val<<"\tHEIGHT: "<<height<<endl;

                height--;
            }

            int PeekTop()
            {
                return top->val;
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
    cout<<st.PeekTop()<<endl;
    

    return 0;
}