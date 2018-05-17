class Node(object):
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data=data
        self.next= next_node
        self.prev = prev_node

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next
    
    def set_prev(self, new_prev):
        self.prev_node = new_prev

class DoubleLinkedList(object):
    def __init__(self, head=0):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_left(self, data):
        new_node = Node(data)
        new_node.set_prev(self.head)
        
