#!python


from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """
    PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.
    Item pairs are stored in a binary min heap for its efficient operations.
    """

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize new binary min heap to store items in this priority queue
        self.heap = BinaryMinHeap()

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.length(), self.front())

    # def __str__(self):
    #     pass
        
    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """
        Insert the given item into this priority queue in order according to
        the given priority.
        """
        # Insert given item into heap in order according to given priority
        new_item = (priority, item)
        self.heap.insert(new_item)

    def front(self):
        """
        Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty.
        """
        if self.length() == 0:
            return None
        return self.heap.get_min()

    def dequeue(self):
        """
        Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty.
        """
        if self.length() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # delete the min element
        front_elem = self.heap.delete_min()

        return front_elem

    def push_pop(self, item, priority):
        """
        Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority.
        This method is more efficient than calling dequeue and then enqueue.
        """
        if self.length() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # store the old front item
        old_front = self.front()

        # replace the item at the 0th element with new item and its priority
        self.heap.items[0] = (item, priority)
        # print(f"new front item: {self.front()}")
        return old_front


if __name__ == "__main__":
    items = [('math', 0), ('cs', 0), ('phys', 1), ('art', 2), ('history', 3),
            ('psychology', 3)]

    
    p_queue = PriorityQueue()
    for item in items:
        elem, priority = item

        p_queue.enqueue(elem, priority)
    
    print(f"queue before push_pop: {p_queue}")
    # print(p_queue.dequeue())
    p_queue.push_pop('pe', 1)
    print(f"queue after push_pop: {p_queue}")
