class Stack:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]
        
    def __str__(self):
        if self.list:
            self.list.reverse()
            values=[str(value) for value in self.list]
            return '\n'.join(values)
        else:
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
    
customStack=Stack(4)
customStack.push(4)
customStack.push(3)
customStack.push(2)
print(customStack)