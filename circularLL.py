class Node:
    data=0
    next=None
    prev=None

    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    head=None

    #insertion

    def insert_at_begin(self,data):
        new_node=Node(data)

        if(self.head is None):
           self.head=new_node
           self.head.next=self.head
           return

        last=self.head

        while(last.next is not self.head):
            last=last.next
        last.next=new_node
        new_node.next=self.head
        self.head=new_node

    def insert_at_last(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head =new_node
            self.head.next=self.head
            return
        
        last=self.head
        while(last.next is not self.head):
            last=last.next

        last.next=new_node
        new_node.next=self.head   

    def insert_at_mid(self,data,pos):
        new_node=Node(data)

        if(self.head is None):
            self.head=new_node
            self.head.next=self.head
            return
        
        if (pos==0):
            self.insert_at_begin(data)

        count=1
        curr=self.head

        while(count<pos and curr.next is not self.head):
            curr=curr.next
            count+=1

        if (curr.next is self.head):
            self.insert_at_last(data)
        
        new_node.next=curr.next
        curr.next=new_node

    #deleteion

    def delete_at_begin(self):
        if (self.head is None):
            print("Linked list is empty")
            return
        
        if(self.head.next is self.head):
            self.head=None
            return
        
        last=self.head
        while(last.next is not self.head):
            last=last.next

        self.head=self.head.next
        last.next=self.head

    def delete_at_end(self):
        if (self.head is None):
            print("Linked list is empty")
            return
        
        if(self.head.next is self.head):
            self.head=None
            return
        prev=None
        curr=self.head

        while(curr.next is not self.head):
            prev=curr
            curr=curr.next
        
        prev.next=self.head
    
    def delete_at_mid(self,pos):
        if (self.head is None):
            print("Linked list is empty")
            return
        
        if(pos==0):
            self.delete_at_begin()
        curr=self.head
        prev=None
        count=1

        while(count<=pos and curr.next is not self.head):
            prev=curr
            curr=curr.next
            count+=1
        
        if(curr.next is self.head):
            self.delete_at_end()
        
        prev.next=curr.next



    #traversal

    def display(self):
        if(self.head is None):
            print("Linked list is empty")
            return
        print(self.head.data)

        temp=self.head.next
        while(temp is not self.head):
            print(temp.data)
            temp=temp.next
    
    #search
    
    def search(self,data):
        temp=self.head
        index=0
        while(temp is not None):
            if(temp.data==data):
                return index
            temp=temp.next
            index+=1

cl=CLL()
#cl.insert_at_begin(0)
#cl.insert_at_begin(1)
#cl.insert_at_begin(2)
#cl.insert_at_begin(3)
cl.insert_at_last(0)
cl.insert_at_last(1)
cl.insert_at_last(4)
cl.insert_at_last(3)
cl.insert_at_mid(6,2)
#cl.delete_at_begin()
#cl.delete_at_end()
cl.delete_at_mid(2)
cl.display()
a=cl.search(4)
print(a)

