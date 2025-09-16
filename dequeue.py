class Deque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return ((self.front == 0 and self.rear == self.size - 1) or
                (self.front == self.rear + 1))

    def isEmpty(self):
        return self.front == -1

    #insertion
    def insert_at_front(self, data):
        if self.isFull():
            print("Deque is full. Cannot insert at front.")
            return

        
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1

        self.deque[self.front] = data
        print(f"Inserted {data} at front. Deque: {self.deque}")

    def insert_at_end(self, data):
        if self.isFull():
            print(f"Deque is full. Cannot insert at end.")
            return     
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1

        self.deque[self.rear] = data
        print(f"Inserted {data} at end. Deque: {self.deque}")
    

    #delete

    def delete_at_front(self):
        if self.isEmpty():
            print("Deque is Empty. Underflow")
            return
        
        deleted=self.deque[self.front]
        self.deque[self.front]=None

        if self.front==self.rear: #last element remaining
            self.front=self.rear=-1
        elif self.front==self.size-1:
            self.front=0
        else:
            self.front+=1
        
        print(f"Deleted {deleted} from front. Deque: {self.deque}")
    
    def delete_at_end(self):
        if self.isEmpty():
            print("Deque is Empty. Underflow")
            return
        
        deleted=self.deque[self.rear]
        self.deque[self.rear]=None

        if self.front==self.rear:
            self.front=self.rear=-1
        elif self.rear==0:
            self.rear=self.size-1
        else:
            self.rear-=1
        print(f"Deleted {deleted} from front. Deque: {self.deque}")

dq = Deque(5)

dq.insert_at_end(10)
dq.insert_at_end(20)
dq.insert_at_front(5)
dq.insert_at_front(2)

print(dq.isFull())
print("Is Empty?", dq.isEmpty())

dq.insert_at_end(30) 
#dq.insert_at_front(1)
dq.delete_at_front()
#dq.delete_at_front()
dq.delete_at_end()
#dq.delete_at_end()



