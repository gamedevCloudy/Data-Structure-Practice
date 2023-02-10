class Node: 
    def __init__(self, dataVal = None): 
        self.dataVal = dataVal
        self.next = None
    
class SlinkedList:
    def __init__(self, val) -> None:
        self.head = Node(val)
        self.current = self.head
    
    def AddNode(self,val):
        x = Node(val)
        if self.head == None: 
            print("hello")
            self.head = x
        else: 
            self.current.next = x
            self.current = x
            pass 
    
    def PrintL(self,node): 
        if(node.next == None): 
            return node.dataVal
        else: 
            print(node.dataVal)
            return (self.PrintL(node.next))
    
    def EleAtIndex(self, index, node, counter = 0, value = True): 
        if(node.next == None): 
            return ("\nNon existant")
        else: 
            if(counter == index): 
                if(value == True): 
                    return node.dataVal
                else: 
                    return node
            else: 
                counter += 1
                return self.EleAtIndex(index, node.next, counter, value) #returns the node or dataval based on value
        return None
    
    def AddAtIndex(self, index, value): 
        x = self.EleAtIndex(index-1, self.head, 0, False)
        y = self.EleAtIndex(index, self.head, 0, False)
        
        temp = Node(value)

        temp.next = y
        x.next = temp 


        return ("Done")

    def RemoveAtIndex(self, index):
        x = self.EleAtIndex(index, self.head)
        if(x != None):
            
            return "\nDeletion Successful."
        return "\nNot Found."
            

             



        


###main

#creating list
list1 = SlinkedList("Mon") 
#adding nodes
list1.AddNode("Tue")
list1.AddNode("Wed")
list1.AddNode("Thu")
list1.AddNode("Fri")
list1.AddNode("Sat")
list1.AddNode("Sun")


#printing entire list
print("\nPrinting Entire List: ")
print(list1.PrintL(list1.head)) 

# print("\n\nAccessing element at index: ")
# #gives the node at index, list Head, counter default 0, value - bool True for value, false for index
# print("\nNode: ",list1.EleAtIndex(3, list1.head,0, False)) 
# #gives the value
# print("\nValue:",list1.EleAtIndex(3, list1.head,0, True))

# print("\n\nAdding a new Element: ")
# print(list1.AddAtIndex(2,"BooBoo"))
# print(list1.AddAtIndex(4,"ChooChoo"))
# print(list1.AddAtIndex(6,"TootToot"))

# print("\n\nReprinting list after adding elements: ")
# list1.PrintL(list1.head)


# print("\n Last but one: ",list1.EleAtIndex(8,list1.head))

# print("\n",  list1.EleAtIndex(8,list1.head,0,False).next.dataVal)

# print("\n\nAdding a new Element: ")
# print(list1.AddAtIndex(2,"BooBoo"))
# print(list1.AddAtIndex(4,"ChooChoo"))
# print(list1.AddAtIndex(6,"TootToot"))

# print("\n\nReprinting list after adding elements: ")
# list1.PrintL(list1.head)

print("\n", list1.RemoveAtIndex(2))
# print(list1.RemoveAtIndex(4))


# print("\n\nReprinting list after adding elements: ")
list1.PrintL(list1.head)


