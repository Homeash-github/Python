class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    '''def display(self):
        temp=self.head
        if self.head is None:
            print("List is Empty")
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next'''
    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
llist=LL
llist.append("A")
llist.append("B")