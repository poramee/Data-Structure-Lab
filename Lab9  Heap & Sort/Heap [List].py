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
def deleteMin(h):
    if len(h) <= 2:
        return h[1]
    temp = h[1]
    h[1] = h.pop(-1)
    i = 1
    while True:
        lC = 2*i
        lR = 2*i + 1
        min_i = i
        if lC < len(h) and h[lC] < h[min_i]:
            min_i = lC
        if lR < len(h) and h[lR] < h[min_i]:
            min_i = lR

        if min_i != i:
            h[i],h[min_i] = h[min_i],h[i]
            i = min_i
        else:
            break
    return temp

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
