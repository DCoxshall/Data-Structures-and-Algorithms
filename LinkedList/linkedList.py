#Example of a doubly linked list concept in python

class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = 0
        print(args)


    def __str__(self):
        string = "["
        currentNode = self.head
        while currentNode != None:
            string += str(currentNode.data)
            currentNode = currentNode.next
            if currentNode == None:
                string += ']'
            else:
                string += ', '
        return string

    def __getitem__(self, key):
        currentNode = self.head
        for i in range(key):
            currentNode = currentNode.next
            if currentNode == None:
                raise(Exception("List index out of range"))
        return currentNode.data

    def __add__(self, other):
        newList = LinkedList()
        currentNode = self.head
        while currentNode != None:
            newList.push(currentNode.data)
            currentNode = currentNode.next
        currentNode = other.head
        while currentNode != None:
            newList.push(currentNode.data)
            currentNode = currentNode.next
        return newList

    def push(self, data):
        if self.size == 0:
            newNode = self.Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self.Node(data)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise(Exception("Cannot pop from empty list."))
        else:
            returnData = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return returnData