class LinkedList:
    class Node:
        def __init__(self, data):
            self.next = None
            self.prev = None
            self.data = data

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        if self.size == 0:
            self.tail = self.Node(data)
            self.head = self.tail
        else:
            newNode = self.Node(data)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def peek(self):
        return self.tail.data

    def pop(self):
        desiredData = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return desiredData

    def __str__(self):
        string = '['
        currentNode = self.head
        while currentNode != None:
            string += str(currentNode.data) + ', '
            currentNode = currentNode.next
        if string[-1] != '[':
            string = string[:-2]
        string += ']'
        return string


lis = LinkedList()
for i in range(5):
    lis.push(i)

print(lis.pop())
