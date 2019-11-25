import random  # for testing purpose
from LinkedList import LinkedList
from isSorted import isSorted

def bubbleSort(list):
    length = len(list)
    comp = 0
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            comp += 1
            if list[j] > list[j+1]:
                list[j].data, list[j + 1].data = list[j + 1].data, list[j].data
    print("Total Compare: ",comp)
    return list

l = LinkedList()

for i in range(0,100):
    l.append(random.randint(0,100))
l = bubbleSort(l)

print(l)
print(isSorted(l))
