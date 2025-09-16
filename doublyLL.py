class Node:
    data=0
    next=None
    prev=None

    def __init__(self,data):
        self.data=data
        self.next=None

class DLL:
    head=None
    tail=None

    #insertion

    def insert_at_begin(self,data):
        new_node=Node(data)

        if (self.head is None):
            self.head=new_node
            self.tail=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            self.tail=new_node
            return
        
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node

    def insert_at_mid(self,data,pos):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        count=0
        curr=self.head

        while(curr is not None and count<pos-1):
            curr=curr.next
            count+=1
        if (curr.next is None):
            curr.next=new_node
            new_node.prev=curr
            tail=new_node
            return
        curr.next.prev=new_node
        new_node.next=curr.next
        curr.next=new_node
        new_node.prev=curr

    #deletion

    def delete_at_begin(self):
        if(self.head is None):
            print("Linked list is empty")
            return
        if(self.head.next is None):
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
    
    def delete_at_end(self):
        if(self.head is None):
            print("Linked list is empty")
            return
        if(self.head.next is None):
            self.head=None
            return
        self.tail=self.tail.prev
        self.tail.next=None

    def delete_at_mid(self,pos):
        if(self.head is None):
            print("Linked List is empty")
            return
        if(pos==0):
            self.head=self.head.next
            return
        
        curr=self.head
        back=None
        count=0

        while(curr is not None and count<pos):
            back=curr
            curr=curr.next
            count+=1
        
        back.next=curr.next
        curr.next.prev=back
    # traversal

    def forward_display(self):
        if (self.head is None):
            print("Linked list is emty")
            return
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next


    def backward_display(self):
        if (self.head is None):
            print("Linked list is empty")
            return
        temp=self.tail
        while(temp is not None):
            print(temp.data)
            temp=temp.prev
    
    #search

    def search(self,data):
        temp=self.head
        index=0
        while(temp is not None):
            if(temp.data==data):
                return index
            temp=temp.next
            index+=1


dl=DLL()
#.insert_at_begin(0)
#dl.insert_at_begin(1)
dl.insert_at_end(0)
dl.insert_at_end(1)
dl.insert_at_end(2)
dl.insert_at_end(3)
dl.insert_at_mid(6,2) 
#dl.backward_display()
#print(dl.head.data)
#dl.delete_at_begin()
#dl.delete_at_end()
#dl.delete_at_mid(2)  
dl.forward_display() 
c=dl.search(4)
print(c)
