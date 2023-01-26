""" IG : few.pz """

class DataNode:
    
    def __init__(self, name=""):
        """ Initialize the node with a name and a next pointer """
        self.name = name
        self.next = None

class SinglyLinked:
    
    def __init__(self):
        """ Initialize the list with a count and a head pointer """
        self.count = 0
        self.head = None
    
    def traverse(self):
        """ Traverse the list and print the name of each node """
        current = self.head
        while current != None:
            print(current.name)
            current = current.next
            
    def insertFront(self, name):
        """ Insert a new node at the front of the list """
        pNew = DataNode(name)
        pNew.next = self.head
        self.head = pNew
        self.count += 1

    def insertLast(self, name):
        """ Insert a new node at the end of the list """
        pNew = DataNode(name)
        if self.head == None:
            self.head = pNew
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = pNew
        self.count += 1
        
    def size(self):
        """ Return the number of nodes in the list """
        return self.count

    def isEmpty(self):
        """ Return True if the list is empty """
        return self.count == 0
    
    def push(self, name):
        """ Push a new node onto the stack """
        self.insertLast(name)
        
def main():
    """ Main functions """
    mylist = SinglyLinked()
    mylist.push("John")
    mylist.push("Tony")
    mylist.traverse()

main()