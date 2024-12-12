"""
Двухсвязный список состоит из узлов узел состоит из данных
адрес следующего узла
адрес предидущего узла

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addNode(self,data):
        newNode = Node(data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None
        self.size =+1

    def display(self):
        currentNode = self.head
        if self.head == None:
            print("Список пустой")
            return
        while currentNode != None:
            print(f"{currentNode.data}")
            currentNode = currentNode.next



dlist = DLL()
dlist.addNode(1)
dlist.addNode(2)
dlist.addNode(3)
dlist.display()
import os
os.mkdir("Z:\РПО\__Python41\Екимов Иван\python\\81-82")