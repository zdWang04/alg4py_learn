class Stack:
  def __init__(self):
	self.stack = []
  def isEmpty(self):
	return self.stack == []
  def push(self, something):
	return self.stack.push(something)
  def pop(self):
	return self.stack.pop()

