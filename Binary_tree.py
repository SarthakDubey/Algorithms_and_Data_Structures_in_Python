import numpy as np


class BinaryTreeNode(object):
    '''A node class for binary tree or doubly linked list.
    Data containers are for parent and two childs'''

    def __init__(self, data=0, leftnode=None, rightnode=None):
        self.data = data
        self.leftnode = leftnode
        self.rightnode = rightnode


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        '''@param - Inserts according to binary search tree algorithm'''
        if self.root is None:
            self.root = BinaryTreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.leftnode is None:
                node.leftnode = BinaryTreeNode(data)
            else:
                self._insert(data, node.leftnode)
        else:
            if node.rightnode is None:
                node.rightnode = BinaryTreeNode(data)
            else:
                self._insert(data, node.rightnode)

    def size(self):
        count = 0
        return count if self.root is None else self._size(self.root, count)

    def _size(self, tree, count):
        if tree is None:
            return count
        elif tree.leftnode or tree.rightnode is not None:
            return max(self._size(tree.leftnode, count),
                       self._size(tree.rightnode, count)) + 1
        else:
            return count + 1

    def delete(self):
        self.root = None
        return

    def print_inorder(self):
        if self.root:
            self._print_inorder(self.root)
        else:
            assert ValueError('Empty tree/node')

    def _print_inorder(self, tree):
        if tree:
            self._print_inorder(tree.leftnode)
            print('{}'.format(tree.data), end=" ")
            self._print_inorder(tree.rightnode)

    def print_preorder(self):
        if self.root:
            self._print_preorder(self.root)
        else:
            assert ValueError('Empty tree/node')

    def _print_preorder(self, tree):
        print('{}'.format(tree.data), end=" ")
        if tree.leftnode:
            self._print_preorder(tree.leftnode)
        if tree.rightnode:
            self._print_preorder(tree.rightnode)

    def print_postorder(self):
        if self.root:
            self._print_postorder(self.root)
        else:
            assert ValueError('Empty tree/node')

    def _print_postorder(self, tree):
        if tree.leftnode:
            self._print_postorder(tree.leftnode)
        if tree.rightnode:
            self._print_postorder(tree.rightnode)
        print('{}'.format(tree.data), end=" ")


def main():
    tree = BinaryTree()
    for _ in range(30):
        tree.insert(np.random.randint(1, 50))
    print('The height of tree is: {}'.format(tree.size()))
    tree.print_inorder()
    print()
    tree.print_preorder()
    print()
    tree.print_postorder()


if __name__ == '__main__':
    main()
