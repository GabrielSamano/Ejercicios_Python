class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Agregando Nodo
    def insert(self, data):

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

# Imprimiendo arbol
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Traversal en reversa
# Raiz -> Izquierda ->Derecha
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

root = Node(30)
root.insert(3)
root.insert(25)
root.insert(10)
root.insert(37)
root.insert(40)
root.insert(5)

print(root.PreorderTraversal(root))