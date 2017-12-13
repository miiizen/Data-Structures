# -*- coding: utf-8 -*-

class Stack:
    """ An implementation of a stack """
    MAX_SIZE = 8
    # Initialise list
    stack_ = [""] * MAX_SIZE
    top = 0
 
    def __init__(self, items=None):
        """ Init, take optional argument items """
        # Check the user has specified a list of items
        if(items != None):
            # Check the list of items is not too long
            if(len(items) > self.MAX_SIZE):
                raise IndexError("The list has more than the max number of items in it!")
            else:
                # Put the items in the stack
                for i in range(0, len(items)):
                    self.stack_[i] = items[i]
                # The next available slot will be the same as the length
                self.top = len(items)
        else:
            self.top = 0

    def push(self, item):
        """ Push a value onto the stack """
        if(not self.isFull()):
            self.stack_[self.top] = item
            self.top += 1
        else:
            raise IndexError("The stack is full")
    
    def pop(self):
        """ Pop an item off the stack """
        if(not self.isEmpty()):
            item = self.stack_[self.top - 1]
            self.top -= 1
            return item
        else:
            raise IndexError("Stack is empty, nothing to pop")

    def peek(self):
        """ Peek top item without popping it """
        if(not self.isEmpty()):
            return self.stack_[self.top - 1]
        else:
            raise IndexError("Stack is empty, nothing to peek")

    def clear(self):
        """ Clear the stack """
        top = 0

    def __len__(self):
        """ Hook method for returning size of stack using len(stack) """
        return self.top
    
    def isEmpty(self):
        """ Bool, returns true or false based on whether the stack is empty or not """
        if(self.top == 0):
            return True
        else:
            return False

    def isFull(self):
        """ Bool, returns true or false based on whether the stack is full or not """
        if(self.top == self.MAX_SIZE):
            return True
        else:
            return False

""" Main - Tests """
if(__name__ == "__main__"):
    # Init and add to stack
    s = Stack(["item 1", "item 2", "item 3", "item 4"])
    s.push("item 5")
    s.push("item 6")
    s.push("item 7")
    s.push("item 8")
    # Check if full (yes)
    print("Is full: " + str(s.isFull()))
    # peek then pop
    print("Peek: " + s.peek())
    print("Pop: " + s.pop())
    print("Len: " + str(len(s)))
