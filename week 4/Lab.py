class BSTNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        pNew = BSTNode(data)
        if self.root is None:
            self.root = pNew
        else:
            current_node = self.root
            while current_node:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = pNew
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = pNew
                        break
                    else:
                        current_node = current_node.right
                        
    def delete(self, data):
        def deleteNode(node, data):
            if node is None:
                return None
            elif data < node.data:
                node.left = deleteNode(node.left, data)
            elif data > node.data:
                node.right = deleteNode(node.right, data)
            else:
                if node.right is None:
                    return node.left
                elif node.left is None:
                    return node.right
                else:
                    minNode = self.findMin(node.left)
                    node.data = minNode
                    node.left = deleteNode(node.left, minNode)
            return node
        self.root = deleteNode(self.root, data)
        
    def preorder(self, root):
        if root is not None:
            print("-> ", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print("-> ", root.data, end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("-> ", root.data, end=" ")
            
    def traverse(self):
        print("")
        self.preorder(self.root)
        print("")
        self.inorder(self.root)
        print("")
        self.postorder(self.root)
        print("")
        
    def is_empty(self):
        return self.root is None
    
    def findMin(self, current_node=None):
        if current_node is None:
            current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data
        
    def findMax(self, current_node=None):
        if current_node is None:
            current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data
