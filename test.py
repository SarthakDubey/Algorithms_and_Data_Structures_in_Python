class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    check = set()
    while head is not None:
        if head.data in check:
            return False
        else:
            check.add(head.data)
            head = head.next
    return True

def addTwoNumbers(l1, l2):
        if l1 or l2:
            




L1 = Node(1)
L2 = Node(2)
L3 = Node(3)
L4 = Node(4)
L5 = Node(5)
L6 = Node(9)
L1.next = L2
L2.next = L3
L4.next = L5
L5.next = L6
#L5.next = L3
print(addTwoNumbers(L1, L4))