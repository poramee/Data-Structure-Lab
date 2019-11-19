class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __gt__(self, o):
        return self.data > o.data

    def __lt__(self, o):
        return self.data < o.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        currNode = self.head
        returnString = ""
        while currNode != None:
            returnString += str(currNode.data) + " "
            currNode = currNode.next
        return returnString

    def __getitem__(self, index):
        return self.nodeAt(index)

    def __setitem__(self, key, value):
        temp = self.nodeAt(key)
        temp.data = value

    def __len__(self):
        return self.size

    def nodeAt(self, index):
        currNode = self.head
        indexIt = 0
        while currNode != None and indexIt < index:
            currNode = currNode.next
            indexIt += 1
        return currNode

    def append(self, data):
        currNode = self.head
        self.size += 1
        if self.head == None:
            self.head = Node(data)
            return self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode.next = Node(data)
        return currNode.next

    def pop(self):
        currNode = self.head
        if self.head == None:
            return None
        elif self.size == 1:
            temp = self.head
            self.head = None
            return temp
        while currNode.next.next != None:
            currNode = currNode.next
        temp = currNode.next
        currNode.next = None
        self.size -= 1
        return temp
