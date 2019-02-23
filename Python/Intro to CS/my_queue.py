class MyQueue:
    def __init__(self):
        self.elements = []
        self.front = -1
        self.rear = -1

    def add(self, value):
        # Checks if the queue is empty or not
        if self.front == -1 or self.rear == -1:
            self.front = 0
            self.rear = 0
            self.elements.insert(self.rear, value)
        else:
            self.rear += 1
            self.elements.insert(self.rear, value)

    def remove(self):
        if self.front == -1 or self.rear == -1:
            return False
        elif self.rear == 0:
            self.front = -1
            return self.elements.pop()
        else:
            self.rear -= 1
            return self.elements.pop(self.front)

    def print_values(self):
        for item in self.elements:
            print (item, end=' ')
        print ()


my_queue = MyQueue()
my_queue.add(5)
my_queue.add('pizza')
my_queue.add(False)
my_queue.add('sunshine')
my_queue.print_values()
my_queue.remove()
my_queue.print_values()
my_queue.add(42)
my_queue.remove()
my_queue.print_values()
