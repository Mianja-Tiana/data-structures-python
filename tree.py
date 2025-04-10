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
      return None
    else:
      return self._search_rec(data , self.root)

  def _search_rec(self, data, node):
    if data == node.data:
      return node 
    elif data< node.data:
      if node.left is None :
        return None
      else:
        return self._search(data,node.left)

  def display(self):
    if self.root is None:
      print("Tree is empty")
    else:
      self._display(self.root)

  def _display(self, node):
    if node is not None:
      self._display(node.left)
      print(node.data,end =" ")
      self._display(node.right)
      
## Exemple
tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)

print(tree.search(10))  
print(tree.search(20))  

tree.display()  