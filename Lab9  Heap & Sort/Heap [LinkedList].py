import random # for testing purpose

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
class Heap:
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
        indexIt = 1
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

def insertMin(heap,data):
    heap.append(data)
    dataIt = len(heap) - 1
    parent = len(heap) // 2
    while heap[dataIt] < heap[parent] and dataIt > 1:
        heap[dataIt].data, heap[parent].data = heap[parent].data, heap[dataIt].data
        dataIt = parent
        parent = parent // 2
    return heap

def print90(heap,index,level):
    if index < len(heap):
        print90(heap,index * 2 + 1,level + 1)
        print("  " * level * 3,heap[index],sep = "")
        print90(heap,index * 2,level + 1)
def deleteMin(heap):
    mm = heap[1]
    if len(heap) == 1:
        return heap.pop()
    heap[1] = heap.pop().data
    dataIt = 1
    while True:
        leftchild = dataIt * 2 if dataIt * 2 < len(heap) else None
        rightchild = dataIt * 2 + 1 if dataIt * 2 + 1 < len(heap) else None
        if leftchild is None and rightchild is None:
            break
        elif leftchild is not None and rightchild is None and heap[leftchild] < heap[dataIt]:
            heap[dataIt].data, heap[leftchild].data = heap[leftchild].data, heap[dataIt].data
            dataIt = leftchild
        elif leftchild is None and rightchild is not None and heap[rightchild] < heap[dataIt]:
            heap[dataIt].data, heap[rightchild].data = heap[rightchild].data, heap[dataIt].data
            dataIt = rightchild
        elif leftchild is not None and rightchild is not None:
            if heap[leftchild] < heap[rightchild]:
                heap[dataIt].data, heap[leftchild].data = heap[leftchild].data, heap[dataIt].data
                dataIt = leftchild
            else:
                heap[dataIt].data, heap[rightchild].data = heap[rightchild].data, heap[dataIt].data
                dataIt = rightchild
    return mm

h = Heap()

dataToInsert = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]

# for i in range(0,10):
#     rand = random.randint(0, 100)
#     print(rand,end = " ")
#     insertMin(h,rand)
for i in dataToInsert:
    insertMin(h,i)
print()
print(h)
print90(h,1,0)
for i in range(0,len(dataToInsert)):
    print(deleteMin(h))
    # print90(h,1,0)
