def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

def sum1ToN(n):
    if n == 1:
        return 1
    return n + sum1ToN(n - 1)

def printNTo1(n):
    print(n)
    if n > 1: printNTo1(n - 1)

def print1ToN(n):
    if n > 1: print1ToN(n - 1)
    print(n)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def binarySearch(lo,hi,x,l):
    index = int((lo + hi) / 2)

    if lo > hi:
        return None
    elif l[index] > x:
        return binarySearch(lo,index - 1,x,l)
    elif l[index] < x:
        return binarySearch(index + 1,hi,x,l)
    else:
        return index

def move(n,fr,to,ax):
    if n == 1:
        print("move",n,"from",fr,"to",to)
    else:
        move(n - 1,fr,ax,to)
        print("move", n, "from", fr, "to", ax)
        move(n - 1,ax,to,fr)

def sum1(n,l):
    if n == 0:
        return l[0]
    else:
        return l[n] + sum1(n - 1,l)

def sum2(l,i = 0):
    if i == len(l):
        return 0
    else:
        return l[i] + sum2(l,i + 1)

def sum3(l):
    if len(l) == 1:
        return l[0]
    return l[0] + sum3(l[1:])

def printListForw(l):
    print(l[0])
    if(len(l) > 1): printListForw(l[1:])

def printListBkw(l):
    if(len(l) > 1):
        printListBkw(l[1:])
    print(l[0])

def app(n,l):
    if n == 0:
        return l
    else:
        ll = app(n - 1,l)
        ll.append(n)
        return ll

def appN(n,l):
    if n == 0:
        return l
    l.append(n)
    return appN(n - 1,l)

# LINKED LIST

class node:
    def __init__(self, d, nxt=None):
        self.data = d
        if nxt is None:
            self.next = None
        else:
            self.next = nxt
class List:
    def __init__(self,head = None):
        self.head = head

def printList(h):
    if h == None:
        return 0
    print(h.data)
    printList(h.next)

def createLLL(head,list):
    if len(list) == 0:
        return head
    elif head == None:
        head = node(list[0])
        createLLL(head,list[1:])
        return head
    else:
        head.next = node(list[0])
        createLLL(head.next,list[1:])
        return head

def createLL(head,n):
    if head == None:
        head = node(n)
        createLL(head,n - 1)
    elif n > 0:
        head.next = node(n)
        createLL(head.next,n - 1)
    return head




l = [0,1,2,3,4,5]
print(binarySearch(0,5,2.5,l))

# print(sum2(l))
# print(sum3(l))
# printListBkw(l)
# print(appN(5,l))

# linkedList = List()

# linkedList.head = createLL(linkedList.head,5)
# printList(linkedList.head)

# linkedList.head = createLLL(linkedList.head,l)
# currNode = linkedList.head
# printList(linkedList.head)
