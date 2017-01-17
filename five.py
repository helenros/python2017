class Stack():
  
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return self.items == []
    
  def push(self,item):
    return self.items.append(item)
  
  def pop(self):
    return self.items.pop()
  
  def getElements(self):
    return self.items

stack=Stack()
print("Push (1)")
stack.push(1)
print("Push (2)")
stack.push(2)
print("Elements in the Stack  : ")
print(stack.getElements())
print("Push (3)")
stack.push(3)
print("Elements in the Stack  : ")
print(stack.getElements())
print("POP : "+str(stack.pop()))
print("Elements in the Stack  : ")
print(stack.getElements())

