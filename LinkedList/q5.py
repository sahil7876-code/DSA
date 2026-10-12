#Delete first and last node from singly linked list
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    #Creating a linked List
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
                temp = temp.next

    def del_first_last(self):
        temp1=self.head
        temp1 =None

        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next = None
        temp = None

list = LL()

list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))
list.append(node(50))
list.append(node(60))

print("List: ")
list.print()

print(" \n")
list.del_first_last()
list.print()