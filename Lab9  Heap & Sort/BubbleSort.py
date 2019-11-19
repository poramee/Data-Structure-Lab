import random  # for testing purpose
from LinkedList import LinkedList

def isSorted(list):
    for i in range(0, len(list) - 1):
        if list[i] < list[i - 1]:
            return False
    return True

def bubbleSort(list):
    length = len(list)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if list[j] > list[j+1]:
                list[j].data, list[j+1].data = list[j+1].data, list[j].data
    return list

l = LinkedList()

for i in range(0,100):
    l.append(random.randint(0,100000))
l = bubbleSort(l)

print(l)
print(isSorted(l))
