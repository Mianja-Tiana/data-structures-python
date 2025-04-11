class NodeTree:
  def __init__(self,data):
    self.data = data
    self.left= None
    self.right =None
class Tree :
  def __init__(self):
    self.root = None
  
  def insert(self,data):
    if self.root is None :
      self.root = NodeTree(data)
    else:
      self._insert_rec(data, self.root)
  
  def _insert_rec (self, data,node):
    if data < node.data:
      if node.left is None:
        node.left = NodeTree(data)
      else:
        self._insert_rec(data, node.left)
    else :

      if node.right is None:
        node.right = NodeTree(data)
      else:
        self._insert_rec(data, node.right)

  def search(self, data):
    if self.root is None:
      return False
    else:
      return self._search_rec(data , self.root)

  def _search_rec(self, data, node):
    if data == node.data:
      return True 
    elif data< node.data:
      if node.left is None :
        return False
      else:
        return self._search(data,node.left)

  
  def in_order(self):
    stack = []
    current_node = self.root

    while stack or current_node:
      while current_node:
          stack.append(current_node)
          current_node = current_node.left
      
      current_node = stack.pop()
      print(current_node.data, end=" ")
      
      current_node = current_node.right
