import random # for testing purpose
def insertMin(heap,data):
    heap.append(data)
    dataIt = len(heap) - 1
    parent = len(heap) // 2
    while heap[dataIt] < heap[parent] and dataIt > 1:
        heap[dataIt],heap[parent] = heap[parent],heap[dataIt]
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
    heap[1] = heap.pop()
    dataIt = 1
    while dataIt * 2  < len(heap) and not (heap[dataIt] < heap[dataIt * 2] and heap[dataIt] < heap[dataIt * 2 + 1]):
        if dataIt * 2 + 1 >= len(heap) or heap[dataIt * 2] < heap[dataIt * 2 + 1]:
            heap[dataIt], heap[dataIt * 2] = heap[dataIt * 2], heap[dataIt]
            dataIt = dataIt * 2
        elif heap[dataIt * 2] < heap[dataIt * 2 + 1]:
            heap[dataIt],heap[dataIt * 2] = heap[dataIt * 2],heap[dataIt]
            dataIt = dataIt * 2
        else:
            heap[dataIt], heap[dataIt * 2 + 1] = heap[dataIt * 2 + 1], heap[dataIt]
            dataIt = dataIt * 2 + 1


h = [0]

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
    deleteMin(h)
    print("-----------")
    print90(h,1,0)
