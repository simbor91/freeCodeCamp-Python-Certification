# Linear Data Structures
# 020 Workshop: Build a Linked List

class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.length = 0
        self.head = None
    
    def is_empty(self):
        return self.length == 0

    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head
        # loop to find the node that contains the specified element to remove
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next # move current_node pointer to the next node during each iteration, allowing to 
            # traverse the linked list until the element is found or the list is at the end
        if current_node is None:
            return # list traversed without finding the element, function shall stop
        elif previous_node is not None:
            current_node.next = previous_node.next # if element to be removed is found and it's not in the head node, 
            # next pointer of the previous node will be updated to skip over the current node (the element to be removied), 
            # removing it from the linked list
        else:
            self.head = current_node.next # if element to be removed is in the head node
        
        self.length -= 1

my_list = LinkedList()
print(my_list.is_empty())

my_list.add(1)
my_list.add(2)
print(my_list.is_empty())
print(my_list.length)

my_list.remove(1)
print(my_list.length)