class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.CircularArr=[None]*size
        self.front=self.rear=-1

    def isFull(self):
        if(self.front==0 and self.rear==self.size-1):
            return True
        if (self.front==self.rear+1):
            return True
        return False
    
    def isEmpty(self):
        return self.front == -1
    
    def Enqueue(self,data):
        if (self.isFull()):
            print("Queue is Full")
            return
        if(self.front==-1):
            self.front=0
        
        self.rear=(self.rear+1)%self.size
        self.CircularArr[self.rear]=data
    
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        data=self.CircularArr[self.front]
        self.CircularArr[self.front] = None
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return data

    def print_array(self):
        for i in self.CircularArr:
            print(i)

ca=CircularQueue(5) 
ca.Enqueue(1)
ca.Enqueue(2)
ca.Enqueue(3)
ca.Enqueue(4)
ca.Enqueue(5)
a=ca.isFull()
print(a)
ca.print_array()
ca.Dequeue()
ca.Dequeue()
ca.Dequeue()
ca.Dequeue()
 
b=ca.isEmpty()
print(b)
#ca.print_array()
