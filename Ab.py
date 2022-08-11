class Node:

    def __init__(self, data):

        self.left = None
        self.right = None 
        self.data = data

    # Ingresando Nodo

    def insert (self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

# Imprimir el arbol
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.left),
        if self.right:
            self.right.PrintTree()

# Inorder Traversal
# Izquierda -> Raiz -> Derecha

    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

root = Node(30)

root.insert(3)
root.insert(25)
root.insert(10)
root.insert(37)
root.insert(40)

print(root.InorderTraversal(root))




        