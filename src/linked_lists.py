class SinglyLinkedNode:
    __slots__ = ('data', 'next')

    def __init__(self, data):
        self.data = data
        self.next = None



class BasicSinglyLinkedList:
    ''' Minimal implementation of the Singly Linked List abstract data type
        (ADT) showing the main concepts of this ADT '''

    def __init__(self):
        self.head = None


    def add(self, value):
        ''' Add new node to the beginning of the list in O(1) time '''

        new_node = SinglyLinkedNode(value)
        new_node.next = self.head
        self.head = new_node


    def remove(self, value):
        ''' Find a node by its data value and remove it in O(n) time '''

        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                if previous_node is None:
                    self.head = current_node.next

                else:
                    previous_node.next = current_node.next

                return

            previous_node = current_node
            current_node = current_node.next

        raise ValueError


    def get_size(self):
        ''' Get the count of nodes of the list in O(n) time '''
        
        node_count = 0
        current_node = self.head

        while current_node:
            node_count += 1
            current_node = current_node.next
        
        return node_count



class AdvancedSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # Keeping track of tail enables insertion of nodes at the end of list in O(1) time
        self.length = 0
        self.is_sorted = False


    def __len__(self):
        return self.length


    def __iter__(self):
        ''' Traverse throught the list one node at a time '''
        
        current_node = self.head

        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


    def insert_at_beginning(self, value):
        ''' Insert <value> at the beginning of the list in O(1) time '''

        self.insert_at_index(0, value)


    def insert_at_end(self, value):
        ''' Insert <value> at the end of the list in O(1) time '''

        self.insert_at_index(self.length, value)


    def insert_at_index(self, index, value):
        ''' Insert <value> at given <index> of the list in O(n) time '''

        if not (isinstance(index, int)):
            raise TypeError('list indices must be integers')

        if not (0 <= index <= self.length):
            raise IndexError('list index out of range')

        new_node = SinglyLinkedNode(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if self.length == 0:   # In case of empty list
                self.tail = new_node

        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node

        else:
            current_node = self.head
            position = 1

            while position < index:   # Traverse to the correct position in the list
                current_node = current_node.next
                position += 1

            new_node.next = current_node.next
            current_node.next = new_node

        self.length += 1
        self.is_sorted = False


    def insert_sorted(self, value):
        ''' Insert <value> into the sorted list in the correct sorted position.
            If the list is currently not sorted, sort it '''
        
        if self.is_sorted:
            new_node = SinglyLinkedNode(value)
            previous_node = None
            current_node = self.head

            while current_node is not None:
                if current_node.data <= new_node.data:
                    previous_node = current_node
                    current_node = current_node.next

                else:
                    break

            if previous_node is None:   # New node is being inserted at the very beginning of the list
                self.head = new_node

            else:
                previous_node.next = new_node

            new_node.next = current_node

            if new_node.next is None:   # New node is being inserted at the very end of the list
                self.tail = new_node

        else:
            self.insert_at_beginning(data)
            self.sort()

        self.length += 1


    def remove(self, value):
        ''' Find a node by data value and remove it '''

        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                if previous_node is None:
                    self.head = current_node.next   # Removing the very first element of the list ...

                    if current_node.next is None:   # ... which happens to be the only element in the list
                        self.tail = None

                else:
                    previous_node.next = current_node.next

                    if current_node.next is None:   # Removing the very last element of the list
                        self.tail = previous_node

                self.length -= 1
                return

            previous_node = current_node
            current_node = current_node.next

        raise ValueError('value not in list')


    def reverse(self):
        ''' Reverse the list in O(n) time '''
        
        previous_node = None
        current_node = self.head
        next_node = self.head
        self.tail = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
        self.is_sorted = False


    def sort(self, reverse=False):
        ''' Sort the list using recursive merge sort algorithm '''
        
        if not self.is_sorted:
            self.head = self._split(self.head, self.length)
            self.is_sorted = True

        if reverse:
            self.reverse()
            
        else:   # Set the tail reference of the list as the final step in sorting procedure
            self.tail = None
            current_node = self.head
            
            while current_node is not None:
                if current_node.next is None:
                    self.tail = current_node
                
                current_node = current_node.next


    def _merge(self, sorted_left, sorted_right):
        ''' Utility method for merging two sorted list into one for merge sort '''
        
        result_head = None
        result_tail = None

        left_node = sorted_left
        right_node = sorted_right

        while left_node and right_node:
            if left_node.data <= right_node.data:
                smaller_node = left_node
                left_node = left_node.next

            else:
                smaller_node = right_node
                right_node = right_node.next

            if result_head is None:   # Very first node is being assigned
                result_head = smaller_node
                result_tail = smaller_node

            else:
                result_tail.next = smaller_node
                result_tail = smaller_node

        while left_node:
            if result_head is None:
                result_head = left_node
                result_tail = left_node

            else:
                result_tail.next = left_node
                result_tail = left_node

            left_node = left_node.next

        while right_node:
            if result_head is None:
                result_head = right_node
                result_tail = right_node

            else:
                result_tail.next = right_node
                result_tail = right_node

            right_node = right_node.next
        
        return result_head

    
    def _split(self, head, length):
        ''' Utility method for splitting the list in half for merge sort '''
        
        if length <= 1:
            return head

        else:
            unsorted_left = head
            unsorted_right = head
            
            middle = length // 2
            left_length = length // 2
            right_length = (length // 2) +  (length % 2)

            position = 1
            previous_node = None

            while position <= middle:
                previous_node = unsorted_right
                unsorted_right = unsorted_right.next
                position += 1

            previous_node.next = None

            sorted_left = self._split(unsorted_left, left_length)
            sorted_right = self._split(unsorted_right, right_length)

            return self._merge(sorted_left, sorted_right)

