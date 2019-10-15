class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.top())
    def top(self):
        return self.items[-1]
    def pop(self):
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

