import random


def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)


print("fac(5) = ", fac(5))


def sum1ToN(n):
    if n < 0:
        return 0
    return n + sum1ToN(n-1)


print("sum1ToN(5) = ", sum1ToN(5))


def printNto1(n):
    if n < 1:
        print("")
        return
    print(n, end=" ")
    printNto1(n - 1)


print("printNto1(5) = ", end="")
printNto1(5)


def print1ToN(n):
    if n <= 1:
        print(n, end=" ")
    else:
        print1ToN(n - 1)
        print(n, end=" ")


print("print1toN(5) = ", end="")
print1ToN(5)
print("")


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print("fib(5) = ", fib(5))


def binarySearch(lo, hi, x, l):
    index = int((lo + hi) / 2)
    if lo > hi:
        return None
    if x < l[index]:
        return binarySearch(lo, index - 1, x, l)
    elif x > l[index]:
        return binarySearch(index + 1, hi, x, l)
    else:
        return index


temp = []
for i in range(0, 20):
    temp.append(random.randint(0, 1000))
temp.sort()
print(temp)
print("binarySearch(", temp[18], ") = ",
      binarySearch(0, 19, temp[18], temp), sep="")
print("binarySearch(", 2000, ") = ",
      binarySearch(0, 19, 2000, temp), sep="")


def move(n, fr, to, ax):
    if n == 1:
        print("move ", n, " : ", fr, " -> ", to)
    else:
        move(n - 1, fr, ax, to)
        print("move ", n, " : ", fr, " -> ", to)
        move(n - 1, ax, to, fr)


print("move: ")
move(3, 'A', 'C', 'B')


def sum1(n, l):
    if n == 0:
        return l[0]
    else:
        return l[n] + sum1(n - 1, l)


print("sum1(19,temp) = ", sum1(19, temp))


def sum2(l, i=0):
    if i == len(l):
        return 0
    else:
        return l[i] + sum2(l, i+1)


print("sum2(temp) = ", sum2(temp))


def sum3(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum3(l[1:])


print("sum3(temp) = ", sum3(temp))


def printListForw(l):
    if len(l) > 0:
        print(l[0], end=" ")
        printListForw(l[1:])


print("printListForw(temp) = ")
printListForw(temp)
print("")


def printListBkw(l):
    if len(l) > 1:
        printListBkw(l[1:])
    print(l[0], end=" ")


print("printListBkw(temp) = ")
printListBkw(temp)
print("")


def app(n, l):
    if n == 0:
        return None

    if n > 1:
        app(n - 1, l)
    l.append(n)


    # return l
print("app(10,[]) = ", app(2, []))


def appB(n, l):
    if n >= 1:
        l.append(n)
        return appB(n - 1, l)
    return l


print("appB(10,[]) = ", appB(10, []))


class node:
    def __init__(self, d, nxt=None):
        self.data = d
        if nxt is None:
            self.next = None
        else:
            self.next = nxt


h = node(1)
currNode = h
for i in range(2, 10):
    currNode.next = node(i)
    currNode = currNode.next


def printList(h):
    if h is not None:
        print(h.data, end=" ")
        printList(h.next)


print("printList(h)")
printList(h)
print()


def createLLL(l):
    # if len(l) == 0:
    #     return None
    # h = node(l[0])
    # h.next = createLLL(l[1:])
    # return h
    if len(l) == 0:
        return None
    else:
        nx = createLLL(l[1:])
        h = node(l[0])
        h.next = nx
        return h


print("createLLL(['A','B','C','D'])")
printList(createLLL(['A', 'B', 'C', 'D']))
print()


def createLL(n, head=None):
    if n == 0:
        return head
    else:
        newHead = node(n)
        newHead.next = head
        return createLL(n - 1, newHead)


print("createLL(10)")
printList(createLL(10))
print()