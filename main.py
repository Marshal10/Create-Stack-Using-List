class Stack:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]
        
    def __str__(self):
        if self.list:
            values=[str(el) for el in self.list.reverse()]
            return '\n'.join(values)
        else:
            return "The stack is empty"
    
customStack=Stack(4)
print(customStack)