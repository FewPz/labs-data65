""" IG : few.pz """

class DataNode:
    
    def __init__(self, name="") -> None:
        """ Initialize the node with a name and a next pointer """
        self.name = name
        self.next = None

class SinglyLinked:
    
    def __init__(self) -> None:
        """ Initialize the list with a count and a head pointer """
        self.count = 0
        self.head = None

    def traverse(self):
        """ Traverse the list and print the name of each node """
        current = self.head
        if (self.count == 0):
            return print("This is an empty list.")
        while current != None:
            print(current.name)
            current = current.next
    
    def insertBefore(self, node, data):
        """ Insert a new node before the given node """
        current = self.head
        while current:
            if current.name == node:
                break
            current = current.next
        else:
            print("Cannot insert, {} does not exist.".format(node))
            return
        pNew = DataNode(data)
        if self.head == current:
            pNew.next = self.head
            self.head = pNew
        else:
            prev = self.head
            while prev.next != current:
                prev = prev.next
            pNew.next = current
            prev.next = pNew
        self.count += 1

    def delete(self, node):
        """ Delete a node with a given name """
        current = self.head
        if current.name == node:
            self.head = self.head.next
            self.count -= 1
            return
        while current.next != None:
            if current.next.name == node:
                current.next = current.next.next
                self.count -= 1
                return
            current = current.next
        print("Cannot insert, {} does not exist.".format(node))

    def insertFront(self, name):
        new_node = DataNode(name)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insertLast(self, name):
        new_node = DataNode(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
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
    print("---------------------")
    mylist = SinglyLinked()
    mylist.insertLast("John")
    mylist.insertLast("Tony")
    mylist.insertFront("Bill")
    mylist.traverse()
    print("---------------------")
    mylist.insertBefore("Tony", "Kim")
    mylist.insertBefore("Tony Stark", "Kim")
    mylist.traverse()
    print("---------------------")
    mylist.delete("John")
    mylist.delete("John")
    mylist.delete("John")
    mylist.traverse()
    print("---------------------")
    mylist.delete("Bill")
    mylist.delete("Kim")
    mylist.delete("Tony")
    mylist.traverse()
    """mylist.delete("Tony")
    mylist.delete("Tony")"""
    print("---------------------")
    mylist.traverse()
    print("---------------------")
    mylist.insertBefore("Tony", "Joseph")
    mylist.traverse()


main()
