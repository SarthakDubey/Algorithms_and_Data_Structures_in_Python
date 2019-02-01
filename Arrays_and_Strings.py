class ListNode(object):
    """
    An abstract node class with basic functions for a ListNode.
    """
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        return self.next_node = new_next
    
    def set_prev(self, new_prev):
        return self.prev_node = new_prev

class LinkedList(ListNode):
    """
    LinkedList Class
    """
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data):
        new_node = ListNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_previous(self, data):
        new_node = ListNode(data)
        new_node.set_prev(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
            if current is None:
                raise ValueError("Data not in list.")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
