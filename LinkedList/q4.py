#delete the middle node from Singly Linked List
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

    def middle(self):
            temp = temp1 = self.head
            prev = None

            while temp1 and temp1.next:
                prev=temp
                temp=temp.next
                temp1=temp.next.next
            print("Middle node", temp.data)

            prev.next=temp.next
            temp=None

            print("Deleted node successfully")
            
list = LL()

list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))
list.append(node(50))
list.append(node(60))

#print("List: ")
#list.print()

#print("Inserting a node at specific Position")
#list.insert_at_pos(node(35), 3)
#list.print()

print("Node at middle Position: ")
list.middle()

list.print()