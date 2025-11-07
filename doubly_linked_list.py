
from operator import length_hint


class Node:
    def __init__(self,value):
        self.value=value;
        self.next=None;
        self.prev=None;



class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node;
        self.tail=new_node;
        self.length=1;

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.tail.prev
            temp.next=None
            self.tail=temp
        self.length-=1

    def prepend(self,value):
        if self.length==0:
            self.append(value)
        else:
            new_node=Node(value)
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1

    def pop_first(self):
        temp=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
        self.length-=1
        return temp

    def get(self,index):
        if index<0 or index >=self.length:
            return None
        elif index < self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp

    def set(self,index,value):
        if index<0 or index>=self.length:
            return None
        else:
            self.get(index).value=value

    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        elif index==0:
            return self.prepend(value)
        elif index==self.length:
            return self.append(value)
        else:
            new_node=Node(value)
            before=self.get(index-1)
            after=before.next

            new_node.prev=before
            new_node.next=after
            before.next=new_node
            after.prev=new_node
            self.length+=1

    def remove(self,index):
        if index<=0 or index>=self.length:
            return None
        elif self.length==1:
            self.pop_first()
        elif index==self.length-1:
            self.pop()
        else:
            temp=self.get(index)
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp=None
            self.length-=1

    def reverse(self):
        if self.length==0:
            return None
        current=self.head
        temp=None
        while current:
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        temp=self.tail
        self.tail=self.head
        self.head=temp

    def is_palindrome(self):
        if self.length==0 or self.length==1:
            return True
        else:
            forward=self.head
            backward=self.tail
            for _ in range(self.length//2):
                if forward.value!=backward.value:
                    return False
            return True

    def partition_list(self,value):
        if self.length==0:
            return None
        lower=DoublyLinkedList(0)
        greater=DoublyLinkedList(0)
        current=self.head
        while current:
            if current.value<value:
                lower.append(current.value)
            else:
                greater.append(current.value)
            current=current.next
        dll=DoublyLinkedList(0)
        while lower.length:
            dll.append(lower.pop_first().value)
        while greater.length:
            dll.append(greater.pop_first().value)
        self.head=dll.head
        self.tail=dll.tail
        self.length=dll.length


my_doubly_linked_list=DoublyLinkedList(141)
my_doubly_linked_list.append(552)
my_doubly_linked_list.append(13)
my_doubly_linked_list.append(21)
my_doubly_linked_list.append(25)
my_doubly_linked_list.partition_list(21)
my_doubly_linked_list.print_list()