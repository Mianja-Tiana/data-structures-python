class Array :
  def __init__(self , capacity):
    self.data = [None]*capacity
    self.size =0
    self.capacity = capacity

  def __len__(self):
    return self.size

  def __getdata__(self, index):
    if 0 <= index < self.size:
      return self.data[index]
    else:
      raise IndexError("Index out of range")

  def __setdata__(self, index , value):
    if 0 <= index< self.size:
      self.data[index] = value
    else :
      raise IndexError("Index out of range")

  def append (self, value):
    if self.size == self.capacity:
      self._resize(self.capacity * 2)
    self.data[self.size] = value
    self.size +=1
 
  def insert(self, index, value):
    if self.size == self.capacity:
      self.resize(self.capacity * 2)
    
    if 0 <= index <= self.size:  
      for i in range(self.size, index, -1):
          self.data[i] = self.data[i - 1]
      self.data[index] = value
      self.size += 1
    else:
      raise IndexError("Index out of range")

  def delete(self, index):
    if 0<= index < self.size:
      for i in range(index, self.size-1):
        self.data[i] = self.data[i+1]
      self.data[self.size -1] = None
      self.size -= 1
    else:
      raise IndexError("Index out of range")

  def search(self, value):
    for i in range (self.size):
      if self.data[i] == value:
        return i

    return -1

  def display(self):
    print(self.data[:self.size])

  def resize(self , new_capacity):
    new_data =[None] * new_capacity
    for i in range(self.size):
      new_data[i] = self.data[i]
    self.data = new_data
    self.capacity = new_capacity