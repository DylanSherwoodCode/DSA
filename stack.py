class Stack:
    

    # Create the stack
    def __init__(self):
    
        self.stack = []

    # Use the append list method to push an item on top
    def push(self, item):

        self.stack.append(item)
        
        return

    # Use the pop list method to pop the item off the top
    def pop(self):
        
        if self.isEmpty():
            raise IndexError("Stack is empty")

        return self.stack.pop()

    # Return the last element in the list, which is the head of our stack
    def peek(self):
        
        if self.isEmpty():
            raise Indexerror("Stack is empty")

        return self.stack[-1]
        
    # Check if the stack is empty, return T/F
    def isEmpty(self):

        return not self.stack

    # Return the len of the list, which is size of stack
    def size(self):

        return len(self.stack)

