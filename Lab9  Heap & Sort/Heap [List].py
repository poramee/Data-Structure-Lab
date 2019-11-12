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
    if len(heap) == 2:
        return heap.pop()
    heap[1] = heap.pop()
    dataIt = 1
    while True:
        leftchild = dataIt * 2 if dataIt * 2 < len(heap) else None
        rightchild = dataIt * 2 + 1 if dataIt * 2 + 1 < len(heap) else None
        if leftchild is None and rightchild is None:
            break
        elif leftchild is not None and rightchild is None and heap[leftchild] < heap[dataIt]:
            heap[dataIt], heap[leftchild] = heap[leftchild], heap[dataIt]
            dataIt = leftchild
        elif leftchild is None and rightchild is not None and heap[rightchild] < heap[dataIt]:
            heap[dataIt], heap[rightchild] = heap[rightchild], heap[dataIt]
            dataIt = rightchild
        elif leftchild is not None and rightchild is not None:
            if heap[leftchild] < heap[rightchild]:
                heap[dataIt],heap[leftchild] = heap[leftchild],heap[dataIt]
                dataIt = leftchild
            else:
                heap[dataIt], heap[rightchild] = heap[rightchild], heap[dataIt]
                dataIt = rightchild

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
    print(h)
    # print90(h,1,0)
