import random
# 1


class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right
def inOrder(r):
    if r:
        inOrder(r.left)
        print(r.data,end = ' ')
        inOrder(r.right)
def addi(r,d):
    currNode = r
    if r == None:
        return Node(d)
    while currNode != None:
        if d >= currNode.data:
            if currNode.right != None:
                currNode = currNode.right
            else:
                currNode.right = Node(d)
                break
        else:
            if currNode.left != None:
                currNode = currNode.left
            else:
                currNode.left = Node(d)
                break
    return r
def add(r,data):
    if not r:
        return Node(data)
    else:
        if data < r.data:
            r.left = add(r.left,data)
        else:
            r.right = add(r.right,data)
        return r
def printSideWay(r,level):
    if r:
        printSideWay(r.right,level + 1)
        print(" " * 3 * level,r.data)
        printSideWay(r.left,level+1)
def height(r):
    if not r:
        return -1
    else:
        hl = height(r.left)
        hr = height(r.right)
        return  max(hl,hr) + 1
def path(r,d):
    if r.data != d:
        print(r.data,end = " ")
        if d < r.data:
            path(r.left,d)
        else:
            path(r.right,d)
    else:
        print(d)
def search(r,d):
    if not r:
        return None
    if r.data == d:
        return r
    else:
        if d < r.data:
            return search(r.left,d)
        else:
            return search(r.right,d)
def depth(r,d):
    if r.data == d:
        return 0
    elif d > r.data:
        return depth(r.getRight(),d) + 1
    else:
        return depth(r.getLeft(),d) + 1
tree = None
for i in [3,4,1,6,2,5]:
    tree = addi(tree,i)
printSideWay(tree,0)
print("------")
path(tree,5)
print("height:",height(tree))
print(depth(tree, 2))
