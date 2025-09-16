class Queue:
  def __init__(self, maxsize=None):
    self.queue = []
    self.maxsize = maxsize

  def enqueue(self, element):
    if self.isFull():
      return "Queue is full"
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def isFull(self):
    if self.size is None:
      return False
    return len(self.queue) >= self.maxsize

  def size(self):
    return len(self.queue)

#trial
queue = Queue(maxsize=4)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.isFull()) 
queue.enqueue(4)
print(queue.queue)
print(queue.peek())
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.dequeue())
print(queue.queue)
print(queue.peek())
print(queue.isEmpty())
print(queue.size())
