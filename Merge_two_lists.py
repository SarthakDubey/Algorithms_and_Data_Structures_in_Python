class Node(object):
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Linkedlist(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node


def merge(L1, L2):
    L3 = Linkedlist()
    while L1.head and L2.head:
        if L1.head.get_data() > L2.head.get_data():
            L3.insert(L1.head.get_data())
            L1.head = L1.head.get_next()
        else:
            L3.insert(L2.head.get_data())
            L2.head = L2.head.get_next()
    L3.insert(L1.head.get_data() or L2.head.get_data())
    return L3


def main():
    L1 = Linkedlist()
    L1.insert(2)
    L1.insert(5)
    L1.insert(7)
    L2 = Linkedlist()
    L2.insert(3)
    L2.insert(11)
    L3 = merge(L1, L2)
    while L3.head:
        print(L3.head.get_data())
        L3.head = L3.head.get_next()


if __name__ == '__main__':
    main()
