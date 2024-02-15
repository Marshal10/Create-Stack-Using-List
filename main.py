class Stack:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]
        
    def __str__(self):
        if self.list:
            values=[str(value) for value in self.list[::-1]]
            return '\n'.join(values)
        return "The stack is empty"

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        self.list.append(value)
        return "An element has been added successfully"
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        return self.list.pop()
        
    
customStack=Stack(4)
print(customStack)
customStack.push(4)
customStack.push(3)
customStack.push(2)
print(customStack)
print(customStack.pop())
print(customStack)