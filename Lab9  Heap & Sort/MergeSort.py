import random  # for testing
from LinkedList import LinkedList
from isSorted import isSorted

comp = 0

def mergeSort(list, fr, to):
    global comp
    if fr == to:
        nList = LinkedList()
        if list[fr] is not None:
            nList.append(list[fr].data)
        return nList
    left = mergeSort(list, fr, (fr + to) // 2)
    right = mergeSort(list, ((fr + to) // 2) + 1, to)
    leftIt = 0
    rightIt = 0
    newList = LinkedList()
    # print(left,right,sep = " || ")
    while leftIt < len(left) and rightIt < len(right):
        comp += 1
        if left[leftIt].data < right[rightIt].data:
            newList.append(left[leftIt].data)
            leftIt += 1
        else:
            newList.append(right[rightIt].data)
            rightIt += 1
    while leftIt < len(left):
        newList.append(left[leftIt].data)
        leftIt += 1
    while rightIt < len(right):
        newList.append(right[rightIt].data)
        rightIt += 1
    return newList


l = LinkedList()

for i in range(0, 10):
    l.append(random.randint(0, 100000))
print("Before Sort",l)
l = mergeSort(l,0,9)
print("Total Compare: ",comp)
print(l)
print(isSorted(l))
