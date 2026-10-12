#Concatenate Two Singly linked List

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

    def concatenate(self):
        temp=self.head
        while(temp.next):
            temp = temp.next
        temp.next=list1.head


list = LL()
list1 = LL()

list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))
list.append(node(50))
list.append(node(60))


list1.append(node(15))
list1.append(node(25))
list1.append(node(35))
list1.append(node(45))
list1.append(node(55))

print("List: ")
list.print()
print(" \n")
list1.print()
print(" \n")

list.concatenate()
list.print()