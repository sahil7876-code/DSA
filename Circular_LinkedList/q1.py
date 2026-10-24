# Creating a Singly Circular Linked List, printing it, and inserting at a position

class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SCL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print(self):
        if self.head == None:
            return

        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp is self.head:
                break

    def insert(self, new_node, pos):
        if pos == 1:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
        else:
            temp = self.head
            p = 1
            while p < pos - 1:
                temp = temp.next
                p += 1

            new_node.next = temp.next
            temp.next = new_node

    def delete(self, val):
        temp = self.head
        prev = None
        if temp.data == val:
            while(temp.next != self.head):
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            while(temp.data != val):
                prev=temp
                temp = temp.next
                if temp == self.head:
                    print("Value not present in the list")
                    


linked_list = SCL()
linked_list.append(node(10))
linked_list.append(node(20))
linked_list.append(node(30))
linked_list.append(node(40))
linked_list.print()
print("\n")
linked_list.insert(node(50), 5)
linked_list.print()
