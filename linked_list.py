
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

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
            self.length=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1
        return True

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.append(value)
        else:
            new_node.next=self.head
            self.head=new_node;
        self.length+=1
        return True

    def pop(self):
        pre=self.head
        temp=self.head
        if self.length==0:
            return None
        while temp.next:
            pre=temp
            temp=temp.next

        self.tail=pre
        self.tail.next=None
        self.length-=1
            
        if self.length==0:
                self.head=None
                self.tail=None

    def pop_first(self):
        if self.length==0:
            return None;
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length-=1
        if self.length==0:
            self.tail=None

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range (index):
            temp=temp.next
        return temp

    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        elif index==0:
            return self.prepend(value)
        elif index==self.length:
            return self.append(value)
        else:
            temp_1=self.get(index-1)
            temp_2=temp_1.next
            temp_1.next=Node(value)
            temp_1.next.next=temp_2
            self.length+=1
            return True

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        elif index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            temp=self.get(index)
            pre=self.get(index-1)
            pre.next=temp.next
            temp.next=None
            self.length-=1
            return temp

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

    def middle_node(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def has_loop(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

    def find_kth_from_end(self,k):
        slow=self.head
        fast=self.head
        for _ in range(k):
            if fast is None:
                return None
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        return slow

    def remove_duplicates(self):
        current=self.head
        while current:
            runner=current
            while runner.next:
                if runner.next.value==current.value:
                    runner.next=runner.next.next
                    self.length-=1
                else:
                    runner=runner.next
            current=current.next

    def binary_to_decimal(self,arr):
        #recursive alg
        #if len(arr)==0:
         #   return 0
        #else:
         #   return arr[0]*2**(len(arr)-1)+self.binary_to_decimal(arr[1:])
             num=0
             current=arr.head
             while current:
                    num=num*2+current.value
                    current=current.next
             return num



my_linked_list=LinkedList(4)
my_linked_list.append(6)
my_linked_list.append(8)
my_linked_list.append(10)
my_linked_list.append(12)
my_linked_list.append(14)
my_linked_list.append(16)
my_linked_list.append(6)
my_linked_list.append(6)
my_linked_list.append(22)
my_linked_list.append(8)
my_linked_list.append(26)
my_linked_list.append(8)
my_linked_list.append(30)

my_linked_list.remove_duplicates()
my_linked_list.print_list()
