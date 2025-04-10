class Stack:
  def __init__(self):
    self.data =[]

  def push(self , data):
    self.data.append(data)

  def pop(self):
    if self.data :
      return self.data.pop()
    return None

  def top(self):
    if self.data:
      print(" The top is :")
      return self.data[-1]

    return None

  def display(self):
    print ("This is our Piles")
    for data in reversed(self.data):
      print(data)
      
  def size(self):
    return len(self.data)
