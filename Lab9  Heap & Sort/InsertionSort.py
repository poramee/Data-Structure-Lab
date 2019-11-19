import random
from LinkedList import LinkedList
from isSorted import isSorted

def insertionSort(list):
    for i in range(1, len(list)):
        k = list[i].data
        j = i - 1
        while j >= 0 and k < list[j].data:
            list[j + 1].data = list[j].data
            j -= 1
        list[j + 1].data = k
    return list


l = LinkedList()

for i in range(0, 100):
    l.append(random.randint(0, 100000))
l = insertionSort(l)

print(l)
print(isSorted(l))
