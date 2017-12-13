# -*- coding: utf-8 -*-

class Queue(object):
    """ An implementation of a circular queue """
    MAX_SIZE = 8
    # Initialise queue
    queue_ = [""] * MAX_SIZE
    top = 0
    bottom = 0
    count = 0
    def __init__(self, items = None):
        """ Init, take optional argument items to place in queue (index 0 is the start of the queue) """
        # Check if a list of items has been provided 
        if(items != None):
            # Check the list is not too long
            if(len(items) > self.MAX_SIZE):
                raise IndexError("The list has more than the max number of items in it!")
            else:
                # Put items in the queue
                for i in range(0, len(items)):
                    self.queue_[i] = items[i]
                self.bottom = len(items)
        else:
            self.bottom = 0

    def enqueue(self, item):
        if(not self.isFull()):
            self.queue_[self.bottom] = item
            # Wrap around array
            self.bottom = (self.bottom + 1) % self.MAX_SIZE
            self.count += 1
        else:
            raise IndexError("The queue is full")

    def dequeue(self):
        if(not self.isEmpty()):
            item = self.queue_[self.top]
            self.top += 1
            self.count -= 1
            return item
        else:
            raise IndexError("Queue is empty, nothing to dequeue")

    def peek(self):
        return self.queue_[self.top]

    def __len__(self):
        return self.count

    def isFull(self):
        if(self.count == self.MAX_SIZE):
            return True
        else:
            return False
    def isEmpty(self):
        if(self.count == 0):
            return True
        else:
            return False

if __name__ == "__main__":
    q = Queue()
    for i in range(0, 8):
        q.enqueue("OOH")
        q.dequeue()
