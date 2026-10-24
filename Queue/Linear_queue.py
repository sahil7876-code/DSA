# Creating a linear queue using Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next= None

class queue:
    def __init__(self):
        self.fro = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.fro = self.rear = new_node

    def dequeue(self):
        temp = self.fro
        print("deleted Node", temp.data)
        self.fro = self.fro.next
        
        if self.fro == None:
            print("EMpty")
            self.rear = None
        temp = None

    def print(self):
        temp = self.fro
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


q= queue()

q.enqueue(Node(10))
q.enqueue(Node(21))
q.enqueue(Node(37))
q.enqueue(Node(49))

q.print()
print()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print()