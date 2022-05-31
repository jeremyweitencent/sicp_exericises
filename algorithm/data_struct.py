

class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Queue:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

