
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1

    def pop(self):
        if self.height==0:
            return
        elif self.height==1:
            self.top=None
        else:
            temp=self.top
            self.top=self.top.next
            temp=None
        self.height-=1


my_stack=Stack(9)
my_stack.push(21)
my_stack.push(121)
my_stack.push(221)
my_stack.push(321)
my_stack.push(421)
my_stack.pop()
my_stack.print_stack()