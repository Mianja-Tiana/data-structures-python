class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add_Node(self, data, post=0):
        # new node
        new_node = Node(data)

        # first node
        if post == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # insert node at a specific position
        current = self.head
        index = 0
        while current and index < post - 1:
            current = current.next
            index += 1

        if current is None and index < post - 1:
            return

        # Insert the new node
        if current:
            new_node.next = current.next
            current.next = new_node
        else:
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def delete_Node(self , data, post =0):

    #delete the first node
        if self.head is None :
            print ("First node only")
            return
        if post == 0:
          self.head = self.head.next
          return

    #delete the node in another position
        current = self.head
        index=0
        while current is not None and index < post-1:
            current = current.next
            index +=1

        if current is not None and current.next is not None:
          current.next = current.next.next
        return

    #delete the node in last position
        current = post
        index =0
        while post is None :
            current.next = None
            return


    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def search(self,node):
      current = self.head
      post = 0
      while current :
        if current.data == node:
          return post
        current = current.next
        post+=1
      return -1

    def get_node(self, position):
      if self.head is None:
        return None
      current = self.head
      index = 0
      while current and index< position:
        current = current.next
        index +=1
      return current

    def update(self, val , new_val):
      current = self.head
      while current:
        if current.data == val:
          current.data = new_val
          return
        current = current.next
      return False  
