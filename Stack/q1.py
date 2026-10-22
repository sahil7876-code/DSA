# Creating a stack using a Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
            return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("empty")
        else:
            temp =self.top
            print("Popped", temp.data)
            self.top = self.top.next
            temp = None


# write a function to revverse a stack
    def reverse(self):
        temp = self.top
        while temp:
            s1.push(Node(temp.data))
            pre = temp
            temp = temp.next

        
    def display(self):
        if self.isempty():
            print("empty")
        else:
            print("stack contains..")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

s = stack()
s.push(Node(5))
s.push(Node(15))
s.push(Node(25))
s.push(Node(35))
s.display()

print()
#s.pop()
#s.pop()
#s.pop()
#s.pop()
# s.display()


s1 = stack()
s.reverse()
s1.display()