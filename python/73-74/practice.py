"""
list [1,2,3,4,5]
set {1,2,3,4,5}
dict {1:2,2:3}


stack (стек)
qeueu (очередь)

"""

#связанный список
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value = None):
        if value is None:
            self.head = None
        else:
            self.head = Node(value)
        self.head = Node()


    def append(self,new_value):
        new_node = Node(new_value)
        current_last_item = self.head
        while current_last_item.next is not None:
            current_last_item = current_last_item.next
        current_last_item.next = new_node

    def show_list(self):
        new_node = Node()
        current_last_item = self.head
        while current_last_item.next is not None:
            print(current_last_item.value)
            current_last_item = current_last_item.next
        current_last_item.next = new_node


my_linked_list = LinkedList()
my_linked_list.append(10)
my_linked_list.append(50)
my_linked_list.append(100)
my_linked_list.append(100)
my_linked_list.append(100)
my_linked_list.show_list()
