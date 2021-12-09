class circleQueue:
    def  __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.body = [None for _ in range(capacity)]
        self.head = 0 # these are just pointers to the start and end
        self.tail = 0

    def enqueue(self, data):
        if self.size == self.capacity:
            print("queue is full")
        else:
            
            self.body[self.tail] = data
            self.tail += 1
            if self.tail == self.capacity:
                self.tail = 0
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("queue is empty")
        else:
            data = self.body[self.head]
            self.body[self.head] = None
            self.head += 1
            if self.head == self.capacity:
                self.head = 0
            self.size -= 1
            return data

    def __str__(self):
        string_list = str(self.body)
        body_copy = self.body
        body_copy[self.head] = "^"
        string_body_copy = list(str(body_copy))
        for i in range(len(string_body_copy)):
            if string_body_copy[i] != "^":
                string_body_copy[i] = " "
    
        return string_list + "\n" + ''.join(string_body_copy)[1:]
        top = ""
        pntr = 0
