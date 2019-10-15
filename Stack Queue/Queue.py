class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def front(self):
        return self.items[0]
    def pop(self):
        return self.items.pop(0)
    def push(self,data):
        self.items.append(data)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    