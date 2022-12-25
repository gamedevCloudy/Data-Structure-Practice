class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def GetData(self): 
        return self.val
    
    def GetNext(self): 
        return self.next
    
    def SetValue(self,val): 
        self.val = val
    
    def SetNext(self, next): 
        self.next = next
    

class CreateLinkedList(object): 
    current = Node(0)
    def __init__(self, head):
        self.head = head
        self.count = 0
        

    def Insert(self, data): 
        newNode = Node(data) #creates a new node with Data as the value
        newNode.SetNext(self.head) #sets the next of the new node to head

        self.head = newNode # sets the head as the new node
        # self.current = self.head

        self.count +=1
    
    def InsertNext(self, data): 
        newNode = Node(data)

        if(self.head != None):
            self.current.SetNext(newNode)
            self.current = newNode 
        else: self.insert(data)
    
    def PrintList(self):
        temp = self.current
        self.current = self.head
        while(self.current.GetNext() != None): 
            print(self.current.GetData())
            self.current = self.current.GetNext()
        self.current.GetData()
        self.current = temp 


    

# def Main(): 
#     print("\nCreate a new linked list: ")
#     x = input("Enter first element: ")
#     y = CreateLinkedList(5)
#     y.Insert(x)

#     z = input("\n How many more elements do you want to add: ")
#     for i in z:
#         m = input("\n Next Element: ")
#         y.InsertNext(m)

#     print("\nPrinting entire list: ") 
#     y.PrintList()

# Main()



y = CreateLinkedList(Node(4))
y.Insert(1)
y.InsertNext(2)
y.InsertNext(3)
y.InsertNext(5)
y.InsertNext(7)

y.PrintList()


             
        


    