#include<iostream>

using namespace std; 

struct Node
{
    int val; 
    Node* next; 
};
class LinkedList
{
    private:Node* head;
            Node* current; 

    public:
            LinkedList()
            {
                head=NULL;
                current=NULL;
            }

            LinkedList(int headVal)
            {
                head->val=headVal; 
                current=head;
            }

            bool isEmpty()
            {
                if(head==NULL && head->next==NULL)
                {
                    return true; 
                }
                return false;
            }

            int FrontPeek()
            {
                if(isEmpty) return NULL; 
                return head->val;
            }
            
            int BackPeek()
            {
                if(isEmpty) return NULL; 
                return current->val;
            }
            
            void AddNode(int val)
            {
                Node* temp = new Node(); //do not forget to initialize this with new!!!
                temp->val=val;

                if(head==NULL)
                {
                    head=temp;
                    current=head;
                }
                else
                {
                    current->next=temp; 
                    current=temp; 
                }
            }

            void RemoveNodeByValue(int val)
            {
                Node* before=head;
                Node*target=head;
                Node* after;

                
                while(target->val!= val)
                {
                    target=target->next;
                }
                while (before->next!=target and target!=head)
                {
                    before=before->next;
                }
                after=target->next;

                if(before==target)
                {
                    head=after;
                }
                else if(target==current)
                {
                    current=before;
                    current->next=NULL; 
                }
                else{
                    before->next=after; 
                }
                delete  target;
                
            }
            void PrintList()
            {
                Node*temp=(head);

                do
                {
                   cout<<temp->val<<"\t";
                   temp=temp->next; 
                } while (temp->next!=NULL);
                cout<<temp->val<<endl; 
            }

            int Size()
            {
                int count; 
                Node*temp=(head);
                do
                {
                   count++;
                   temp=temp->next; 
                } while (temp->next!=NULL);
                return count;
            }

            void ClearList()
            {
                Node* crt = head;
                Node* next = NULL;
            
                while (crt != NULL)
                {
                    next = crt->next;
                    delete crt;
                    crt = next;
                }
            
                
                head = NULL;
                current=NULL;
            }

}; 

int main()
{
    LinkedList l0; 
    l0.AddNode(6);
    l0.AddNode(26);
    l0.AddNode(2);
    l0.PrintList();
    cout<<"\n"<<l0.Size()<<endl;

    
    l0.RemoveNodeByValue(6);
    l0.PrintList();
    cout<<"\n"<<l0.Size()<<endl;
    
    l0.ClearList();
    return 0; 
}