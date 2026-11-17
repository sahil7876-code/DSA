class Node:
    def __init__(self,name:str,pid:str,pr):
        self.name=name
        self.pid=pid
        self.pr=pr
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,value,pid,pr):
        if pr == "Critical":
            pr = 1
        elif pr == "Serious":
            pr = 2
        elif pr == "Normal":
            pr = 3
        else:
            print("Invalid priority")
            return
        
        new_node=Node(value,pid,pr)
        if self.front is None:
            self.front=self.rear=new_node
            return
        if new_node.pr<self.front.pr:
            new_node.next=self.front
            self.front=new_node
        else:
            temp = self.front

            while temp.next and temp.next.pr <= new_node.pr:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

            if new_node.next is None:
                self.rear = new_node

    def display(self):
        temp=self.front
        while temp :
            print("Patient Name is",temp.name,"His Id :",temp.pid,"Condition is :",temp.pr)
            temp=temp.next

    def display_next(self):
        print('Patient to be treated next:', self.front.next.name)

    def dequeue(self):
        if self.front is None:
            return "No patient in queue"
        self.front=self.front.next
        print('Patient removed',self.front.next.name, "\nTreatment done")
p=Queue()
p.enqueue("sujal",101,"Normal")
p.enqueue("vedika",102,"Serious")
p.enqueue("Shivam",103,"Critical")
p.enqueue("sahil",104,"Normal")
print('Queue of Patients:')
p.display()
print()
p.display_next()
print()
p.dequeue()
print()
p.display()