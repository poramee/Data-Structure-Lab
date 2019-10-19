# 1
class Node:
    def __init__(self,data,left = None,right = None):
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

    def setData(self,data):
        self.data = data
    def setLeft(self,left):
        self.left = left
    def setRight(self,right):
        self.right = right

# 2 - 3
class BST:
    def __init__(self,root = None):
        self.root = root
    def __str__(self):
        return str(self.root)

    def addI(self,data): # 3.1
        currNode = self.root
        newNode = Node(data)
        if currNode == None:
            self.root = newNode
            return newNode
        while currNode != None:
            if data >= currNode.getData():
                if(currNode.getRight() == None):
                    currNode.setRight(newNode)
                    break
                else:
                    currNode = currNode.getRight()
            else:
                if(currNode.getLeft() == None):
                    currNode.setLeft(newNode)
                    break
                else:
                    currNode = currNode.getLeft()
        return newNode
    def add(self,data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            return self._add(self.root,data)
    def _add(self,currNode,data):
        if data >= currNode.getData():
            if currNode.getRight() == None:
                currNode.setRight(Node(data))
                return currNode.getRight()
            else:
                return self._add(currNode.getRight(),data)
        else:
            if currNode.getLeft == None:
                currNode.setLeft(Node(data))
                return currNode.setLeft()
            else:
                return self._add(currNode.getLeft(),data)

    def inOrder(self):
        self._inOrder(self.root)
    def _inOrder(self, currNode):
        if currNode != None:
            self._inOrder(currNode.getLeft())
            print(currNode.getData())
            self._inOrder(currNode.getRight())

    def printSideway(self):
        self._printSideway(self.root,0)
    def _printSideway(self,currNode,level):
        if currNode != None:
            self._printSideway(currNode.getRight(),level+1)
            for i in range(0,3*level):
                print(" ",end="")
            print(currNode.getData())
            self._printSideway(currNode.getLeft(),level+1)

    def preOrder(self):
        self._preOrder(self.root)
    def _preOrder(self, currNode):
        if currNode != None:
            print(currNode.getData())
            self._preOrder(currNode.getLeft())
            self._preOrder(currNode.getRight())

    def serach(self,searchData):
        return self._search(self.root,searchData)
    def _search(self,currNode,searchData):
        if currNode == None:
            return None
        else:
            if searchData >= currNode.getData():
                return self._search(currNode.getRight(),searchData)
            elif searchData == currNode.getData():
                return currNode
            else:
                return self._search(currNode.getLeft(),searchData)
    
    def path(self,searchData):
        return self._path(self.root,searchData)
    def _path(self,currNode,searchData):
        if currNode == None:
            return None
        else:
            print(currNode,end=" ")
            if searchData > currNode.getData():
                return self._path(currNode.getRight(), searchData)
            elif searchData == currNode.getData():
                return currNode
            else:
                return self._path(currNode.getLeft(), searchData)

    def delete(self,data):
        return self._delete(self.root,data)
    
    def _inOrderSuccessor(self,currNode):
        if currNode.getLeft() == None:
            return currNode
        else:
            return self._inOrderSuccessor(currNode.getLeft())

    def _delete(self, currNode, data):
        if currNode == None:
            return None

        if data < currNode.data:
            currNode.left = self._delete(currNode.left,data)
        elif data > currNode.data:
            currNode.right = self._delete(currNode.right,data)
        else:
            if currNode.left == None:
                return currNode.right
            elif currNode.right == None:
                return currNode.left
            else:
                temp = self._inOrderSuccessor(currNode.right)
                currNode.data = temp.data
                self._delete(temp,temp.data)

        return currNode

l = [int(e) for e in input("insert integers : ").split()]
print(l)
t = BST() 
for ele in l:
    t.addI(ele)
    
for ele in l:
    t.addI(ele)

t.inOrder()
t.printSideway()
t.delete(2)
t.inOrder()
