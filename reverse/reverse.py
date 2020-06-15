class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current_node = node
        # Here, we're just worried about 1)each node as a whole and 2) the node pointer

        # create base-case for recursion
        while current_node is not None:
            # create new variable 'next' to be called at the end of the while loop creating a loop.
            # (the iterator) assign this to look at the next available node.
            next = current_node.next_node

            # (assign the pointer to the previous node) take the current node and change the `next_node` pointer to be a new variable called `prev`
            current_node.next_node = prev

            # (reverse the node's position)
            prev = current_node

            # (the iterator) look back with the iterator to start the process again
            current_node = next

        # when the loop finally gets to the end, we are now removing the head from it's original node
        # to point to the NEW start of the list
        self.head = prev
