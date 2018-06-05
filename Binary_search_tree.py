class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, value):
        if self.data is None:
            self.data = value
        elif value < self.data:
            self.left = Node()
            self.left.insert(value)
        elif value > self.data:
            self.right = Node()
            self.right.insert(value)
        else:
            raise ValueError
    
    def print_inorder(self):
        if self.data:
            if self.left: self.left.print_inorder()
            print(self.data, end=" ")
            if self.right: self.right.print_inorder()

def main():
    BST = Node(40)
    BST.insert(20)
    BST.insert(50)
    BST.print_inorder()

if __name__ == '__main__':
    main()