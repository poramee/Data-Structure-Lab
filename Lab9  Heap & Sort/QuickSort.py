import random
from LinkedList import LinkedList
from isSorted import isSorted

comp = 0

def quickSort(list):
    global comp
    if len(list) == 0:
        return LinkedList()
    pivot = random.randint(0, len(list) - 1)
    left = LinkedList()
    right = LinkedList()
    for i in range(0, len(list)):
        comp += 1
        if i == pivot:
            continue
        if list[i].data <= list[pivot].data:
            left.append(list[i].data)
        else:
            right.append(list[i].data)
    left = quickSort(left)
    right = quickSort(right)

    newList = LinkedList()
    newList.head = left.head
    newList.append(list[pivot].data)
    newList.appendNode(right.head)
    return newList

def quickSort2(list,pivot):
    global comp
    if len(list) == 0:
        return LinkedList()
    left = LinkedList()
    right = LinkedList()
    for i in range(0, len(list)):
        if i == pivot:
            continue
        comp += 1
        if list[i].data <= list[pivot].data:
            left.append(list[i].data)
        else:
            right.append(list[i].data)
    left = quickSort2(left, 0)
    right = quickSort2(right, 0)
    # left = quickSort2(left, len(left) // 2)
    # right = quickSort2(right, len(right) // 2)
    # left = quickSort2(left,len(left) - 1)
    # right = quickSort2(right, len(right) - 1)

    newList = LinkedList()
    newList.head = left.head
    newList.append(list[pivot].data)
    newList.appendNode(right.head)
    return newList


# l = LinkedList()

# for i in range(0, 173):
#     l.append(random.randint(0, 10000))
# print("Before Sort: ",l)
# l = quickSort(l)
# print("Total Compare: ",comp)
# print(l)
# print(isSorted(l))

l2 = LinkedList()

for i in range(0,10):
    l2.append(i)
comp = 0
l2 = quickSort2(l2,0)
# l2 = quickSort2(l2, len(l2) // 2)
# l2 = quickSort2(l2,len(l2) - 1)
print("Total Compare: ", comp)
print(l2)
print(isSorted(l2))

