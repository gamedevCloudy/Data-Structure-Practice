#include<iostream>

using namespace std; 
struct Node
{
    int val; 
    Node*prev; 
    Node*next; 
};
class DoublyLinkedList
{
    private:Node* head;
            Node* current; 
            int size; 
            
    public: DoublyLinkedList()
            {
                head=NULL; 
                current=head; 
                size=0;
            }

            DoublyLinkedList(int value)
            {
                Node*temp = new Node();
                temp->val=value;

                head=temp; 
                current=head; 
                size=1;
            }

            void AddNode(int value)
            {
                Node* temp = new Node(); 
                temp->val= value; 

                if(head==NULL)
                {
                    head=temp; 
                    current=head;
                }
                else{
                    temp->prev=current;
                    current->next=temp;

                    current=temp;
                }
                size++;
            }

            void Remove()
            {
                Node* last = current;
                if(current!=head)
                {
                current=last->prev;
                current->next=NULL;
                }
                else{
                    head=NULL;
                }

                size--;
                delete last;
            }
            
            void InsertAtPosition(int posn, int value)
            {
                if(posn>size)
                {
                    cerr<<"\n! Exceeded List Size !"
                        <<"\nAdding at last.....";
                    AddNode(value); 
                    return;
                }
                Node*target=head;
                Node*insert= new Node();
                insert->val=value;
                int count=1;
                while(count!=posn)
                {
                    target=target->next;
                    count++;
                }
                //reached target posn

                target->prev->next=insert;
                insert->prev=target->prev;
                insert->next=target;
                
                size++;
            }

            void RemoveAtPosition(int posn)
            {
                if(posn>size || posn<1)
                {
                    cerr<<"\n Exceeded Size, removing last!"; 
                    Remove();
                    return;
                }

                Node* target = head;
                int count=1;

                while(count!=posn)
                {
                    target=target->next;
                    count++;
                }
                if(target!=head)
                {
                    target->prev->next=target->next;
                    target->next->prev=target->prev;
                }
                else{
                    head=target->next;
                    head->prev=NULL;
                }
                size--;
                delete target;
            }
            
            void ClearList()
            {
                Node*target=current;
                while(target->prev!=NULL)
                {
                    target=target->prev;
                    current=current->prev;
                    delete target->next;
                }
                delete target;
                
                head=NULL;
                current=head;
            }

            void DisplayFwd()
            {
                //front
                Node*front=head; 

                cout<<endl;
                while(front!=NULL)
                {
                    cout<<front->val<<"\t"; 
                    front=front->next; 
                }
                cout<<endl;
               
            }
            
            void DisplayRev()
            {
                Node*rear=current; 

                cout<<endl;
                while(rear!=NULL)
                {
                    cout<<rear->val<<"\t"; 
                    rear=rear->prev; 
                }
                cout<<endl;
                //back
            }

            int GetSize()
            {
                return size;
            }
};

int main()
{
    DoublyLinkedList dl(55);


    dl.AddNode(54);
    dl.AddNode(53);
    dl.AddNode(52);
    dl.AddNode(51);
    dl.AddNode(50);
    
    dl.InsertAtPosition(4,65);
    dl.DisplayFwd();
    dl.RemoveAtPosition(5);
    dl.Remove();
    dl.ClearList();
    dl.DisplayFwd();
    return 0;
}