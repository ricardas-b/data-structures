from linked_lists import BasicSinglyLinkedList as LinkedList



class Stack:
    ''' Implementation of Stack ADT '''
    
    def __init__(self):
        self.items = LinkedList()


    def push(self, val):
        ''' Add an element to the stack in O(1) time '''
        
        self.items.add(val)


    def pop(self):
        ''' Remove an element from the stack in O(1) time '''
        
        val = None

        if not self.is_empty():
            val = self.items.head.data
            self.items.remove(val)

        return val


    def peek(self):
        ''' Get the top element without removing it from the stack in O(1) time '''
        
        val = None

        if not self.is_empty():
            val = self.items.head.data

        return val


    def is_empty(self):
        ''' Check if stack has any elements in O(1) time '''
        
        return self.items.head is None

