#Assignment Question Perfrom various Operations on Singly Linked List
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

    #Transversing and printing node values
    def print(self):
        temp=self.head

        while temp:
            print(temp.data)
            temp = temp.next

    #inserting node at a position
    def insert_at_pos(self, new_node, pos):
        if pos < 1:
            print ("Invalid Position")
            return
            
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count +=1

        if temp == None:
            print("Invalid Position")
        else:
            new_node.next = temp.next
            temp.next = new_node

    #Find middle node and print its value
    def middle(self):
        if self.head == None:
            print("Empty List")
            return
            
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        mid = count // 2

        temp = self.head
        count = 0

        while count < mid:
            temp = temp.next
            count += 1

        print("Middle node", temp.data)

    #Delete Node
    def delete(self, pos):
        if pos < 1 or self.head == None:
            print("Invalid postion or empty list")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        count =1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp == None or temp.next == None:
            print("Invalid Position")
        else:
            temp.next = temp.next.next

    #Reverse List
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    #Sum of 2 consecutive Numbers
    def sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next

list = LL()

list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))
list.append(node(50))
list.append(node(60))

print("List: ")
list.print()

print("Inserting a node at specific Position")
list.insert_at_pos(node(35), 3)
list.print()

print("Node at middle Position: ")
list.middle()

print("Deleted a Node")
list.delete(2)
list.print()

print("Sum of 2 Consecutive nodes")
list.sum()

print("Reversed List")
list.reverse()
list.print()