#print sum of 2 consecutive nodes in SLL

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next=new_node

    def sum(self):
        temp=self.head
        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next

list=linkedlist()
list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))
list.append(node(50))
list.sum()