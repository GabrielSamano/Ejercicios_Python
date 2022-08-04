from logging import root


class Boot:
    def __init__(self, val=0, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right

def inorder(boot):
    if boot is None:
        return
    inorder(boot.left)
    print(boot.val)
    inorder(boot.right)

root = Boot(15)
root.left = Boot(4)
root.right = Boot(7)

inorder(root)
