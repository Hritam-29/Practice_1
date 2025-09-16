class Node:
    data=0
    next=None

    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:

    #insertion

    head=None
    def insert_at_begin(self,data):
        new_node=Node(data)

        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node


    def insert_at_end(self,data):
        new_node=Node(data)

        if(self.head is None):
            self.head=new_node
            return
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=new_node

    def insert_at_mid(self,pos,data):
        new_node=Node(data)

        if (pos==0):
            new_node.next=self.head
            self.head=new_node
            return
        
        current_node=self.head
        count=0

        while(current_node is not None and count<pos-1):
            current_node=current_node.next
            count+=1
        if (current_node is None):
            print ('Position is out of Linked list')
            return
        new_node.next=current_node.next
        current_node.next=new_node

    #deletion

    def delete_at_beginning(self):
        if (self.head is None):
            print("No element to delete")
            return
        self.head=self.head.next
    
    def delete_at_end(self):
        if(self.head is None):
            print("No element to delete")
            return
        
        if (self.head.next is None):
            self.head=None
            return
        
        curr=self.head
        prev=None

        while(curr.next is not None):
            prev=curr
            curr=curr.next
        
        prev.next=None
    
    def delete_at_mid(self,pos):
        if(self.head is None):
            print("Linked List is empty")
            return
        if(pos==0):
            self.head=self.head.next
            return
        
        curr=self.head
        prev=None
        count=0

        while(curr is not None and count<pos):
            prev=curr
            curr=curr.next
            count+=1
        
        if(curr is None):
            print("Position is greater than Linked List")
            return
        
        prev.next=curr.next
        
    #search

    def search(self,data):
        if(self.head is None):
            return -1
        
        if(self.head.next is None and data==self.head.data):
            return 0
        
        curr=self.head
        pos=0

        while(curr is not None):
            if(curr.data==data):
                return pos
            curr=curr.next
            pos+=1
        return -1

    # traversal

    def display(self):
        temp=self.head

        while (temp is not None):
            print(temp.data)
            temp=temp.next

sl=SLL()
sl.insert_at_end(1)
sl.insert_at_end(2)
sl.insert_at_end(3)
sl.insert_at_end(10)
#sl.insert_at_mid(2,4)
#sl.delete_at_beginning()
#sl.delete_at_end()
#sl.delete_at_mid(1)
sl.display()
print(sl.search(10))
#print(sl.head.data)
 