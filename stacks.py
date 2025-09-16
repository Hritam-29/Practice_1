class Stack:
    def __init__(self, size):
        self.size = size
        self.stackArr = []
        self.top = -1

    #insertion

    def push(self, data):
        if self.isFull():
            print("Stack full = Overflow")
            return
        self.stackArr.append(data)
        self.top += 1

    def isFull(self):
        return self.top == self.size - 1
    
    def isEmpty(self):
        return self.top==-1
    
    #Deletion

    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty = Underflow")
            return
        self.top-=1
        return self.stackArr.pop()

    #Top Element     
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.stackArr[self.top]

    def __str__(self):
        return str(self.stackArr)

stack = Stack(5)
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
#stack.push(5)
stack.pop()
print(stack)
print(stack.peek())

