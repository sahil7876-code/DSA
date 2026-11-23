#Creating Binary Search Tree

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
        self.ncnt = 0
        self.lcnt = 0

    def insert(self, new_node):
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left == None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def inorder(self, temp): #self id varible created  for traversing
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end= ' ')
            if temp.left is None and temp.right is None:
                self.count += 1
            else:
                self.ncnt += 1
            self.inorder(temp.right)

    def postorder(self,temp):
        if temp==None:
            return
        else:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=' ')
            

    def preorder(self,temp):
            if temp==None:
                return
            else:
                print(temp.data, end=' ')
                self.preorder(temp.left)
                self.preorder(temp.right)

    def m(self, temp):
        rot = temp
        while rot.left:
            rot = rot.left
        print('Minimum val:',rot.data)
        
        rot = temp
        while rot.right:
            rot = rot.right
        print('Maximum val:',rot.data)

    def count_lnode(self, temp):
        rot = temp 
        self.lcnt = 0
        while rot.left:
            rot = rot.left
            self.lcnt += 1
        #print(self.lcnt)

    

b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(15))
b1.insert(Node(15))
b1.insert(Node(500))
b1.insert(Node(50))
b1.insert(Node(70))
b1.insert(Node(2))
b1.inorder(b1.root)
print(b1.count)
print(b1.ncnt)
print()
b1.postorder(b1.root)
print()
b1.preorder(b1.root)
print()
b1.m(b1.root)
print("lnode",b1.root)