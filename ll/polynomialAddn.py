class Node: 
    def __init__(self, coef, powr):
        self.coef = coef
        self.powr = powr
        self.next = None

class SLinkedList:
    def __init__(self,coef = 0, powr = 0):
        self.head = Node(coef, powr)
        self.current = self.head
    
    def AddElement(self, coef, powr):
        x = Node(coef,powr)
        
        if(self.head != None):
            self.current.next = x
            self.current = x
        
        else: print("List created improperly...")
    

    def PrintList(self,node): #call by passing head .... 
        if(node.next == None): 
            varx = str(str(node.coef)+"x^"+str(node.powr)+"\t")
            return (varx)
        else: 
            varx = str(str(node.coef)+"x^"+str(node.powr)+"\t")
            print(varx)
            return (self.PrintList(node.next))

def NextEle(node):
    return node.next

def AddLinkedLists(l1, l2):
    l1 = l1
    l2 = l2

    l3 = SLinkedList()

    while(l1.powr != 0 and l2.powr):
        if(l2.powr == l1.powr): 
            l3.AddElement(l2.coef+l1.coef, l1.powr)
            print("Added something....")
            l1 = l1.next
            l2 = l2.next
        elif(l2.powr > l1.powr):
            l3.AddElement(l2.coef, l2.powr)
            print("Added some other thing...")
            # l1 = l1.next
            l2 = l2.next
        else: l1 = l1.next
    
    print("\nAddition is: ")
    return l3



def main():
    l1 = SLinkedList(5,3)
    l1.AddElement(4,2)
    l1.AddElement(2,0)
    
    l2 = SLinkedList(5,1)
    l2.AddElement(5,0)

    
    print("\n\n")
    print(l1.PrintList(l1.head))
    print("\n\n")
    print(l2.PrintList(l2.head))

    print(AddLinkedLists(l1.head,l2.head))
main()

    


