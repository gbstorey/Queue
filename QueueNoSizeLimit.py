# FIRST IN, FIRST OUT

class Queue:
    # Creation: O(1) time and space complexity
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        # O(1) Time and space complexity
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        # O(n) time complexity, O(1) space complexity
        self.items.append(value)
        return 'The element is inserted at the end of the queue'

    def dequeue(self):
        # O(n) time complexity, O(1) space complexity
        if self.is_empty():
            return "There are no elements in the queue"
        else:
            return self.items.pop(0)

    def peek(self):
        # O(1) time and space complexity
        if self.is_empty():
            return "There are no elements in the queue"
        else:
            return self.items[0]

    def delete(self):
        # O(1) time and space complexity
        self.items = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
print(customQueue.delete())
