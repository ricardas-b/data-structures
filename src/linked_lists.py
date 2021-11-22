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


    def add(self, data):
        ''' Add new node to the beginning of the list in O(1) time '''

        new_node = SinglyLinkedNode(data)
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


