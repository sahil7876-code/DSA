#Insert a value at a position in LikedList

class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None


    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

list=linkedlist()
list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))

list.print()