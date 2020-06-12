class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Check to see if a specific value is in the tree
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:  # call and return contains on existing left node
                return self.left.contains(target)
            else:
                return False  # if no left node
        else:
            if self.right:  # call and return contains on existing right node
                return self.right.contains(target)
            else:
                return False  # if no right node
