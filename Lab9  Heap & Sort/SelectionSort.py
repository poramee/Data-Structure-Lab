import random  # for testing
from LinkedList import LinkedList

def isSorted(list):
    for i in range(0, len(list) - 1):
        if list[i] < list[i - 1]:
            return False
    return True

def selectionSort(list):
    length = len(list)
    comp = 0
    for i in range(0, length - 1):
        maxx = list[0].data
        maxIndex = 0
        for j in range(0, length - i):
            comp += 1
            if list[j].data > maxx:
                maxx = list[j].data
                maxIndex = j
        list[length - i - 1].data, list[maxIndex].data = list[maxIndex].data,list[length - i - 1].data
    print("Total Compare: ",comp)
    return list


l = LinkedList()

for i in range(0, 100):
    l.append(random.randint(0, 100000))
l = selectionSort(l)

print(l)
print(isSorted(l))

