class Node: 
    def __init__(self, day = None):
        self.day = day
        self.next = None

class SList: 
    def __init__(self) -> None:
        self.head = None


def PrintList(nodes): 
    if(nodes.next != None): 
        return (nodes.day, id(nodes))
    else: return PrintList(nodes.next)


def main(): 
    print("\n Week days....")
    x = input("\n Day 1: ")
    head = SList()
    head.day = x
    

main()


        

