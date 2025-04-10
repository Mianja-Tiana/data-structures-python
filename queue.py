class Queue :
  def __init__(self):
    self.data =[]

  def enqueue(self,data):
    self.data.append(data)

  def dequeue(self):
    if self.is_empty():
      return None
    return self.data.pop(0)

  def is_empty(self):
    return len(self.data)==0

  def size(self):
    return len(self.data)
  def display (self):
    if self.is_empty():
      print("Queue is empty")
    else:
      print ("This is our File :",end="")
      for data in self.data:
        print(f"--> {data}",end = "")
      print()
      print(f"Length of the queue: {self.size()}")