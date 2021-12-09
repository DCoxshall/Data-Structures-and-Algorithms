class Queue:
    def __init__(self):
         self.head = None
         self.size = 0

    def enqueue(self, data):
        if self.size == 0:
            self.head = Node(data)
        else:
            self.head.push(data)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
        size -= 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def push(self, data):
        if self.next == None:
            self.next = Node(data)
        else:
            self.next.push(data)
