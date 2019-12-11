class Stack:
  def __init__(self):
    self.items = []
  
  def push(self, item):
    self.items.append(item)
   
  def pop(self):
    return self.items.pop()
    
  def is_empty(self):
    return self.items == []
  
  def top(self):
    return self.items[-1]
  
  def get_stack(self):
    return self.items

  
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.get_stack())
print(st.pop())
print(st.get_stack())
