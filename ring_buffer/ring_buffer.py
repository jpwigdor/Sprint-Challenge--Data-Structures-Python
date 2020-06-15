class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # set the storage
        self.storage = []
        # create variable of the oldest created item. This will update as we iterate over a list at max storage.
        self.oldest = 0

    def append(self, item):
        # Check to see if we're even less than capacity. if we are, simply append the item.
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        # if we're at max capacity, we need to overwrite the oldest item.
        else:
            # Explicitly assign the new item to the oldest item to overwrite it.
            self.storage[self.oldest] = item
            # Check to see if the 'oldest marker' is less than the max storage limit. if so, then increment it up by one.
            if self.oldest < len(self.storage) - 1:
                self.oldest += 1
            # If the 'oldest marker' is at the last idex, reassign it to zero to start overwriting the beginning of the array again.
            else:
                self.oldest = 0

    def get(self):
        # return current list of items
        return self.storage


print(RingBuffer)
