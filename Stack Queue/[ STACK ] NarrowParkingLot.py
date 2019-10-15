from Stack import Stack
class StackN(Stack):
    SIZE = 4
    def isFull(self):
        return self.size() >= self.SIZE

soiA = StackN()
soiB = StackN()

while True:
    cmd = input()
    if cmd[0] == 'D':
        no = cmd[1]
        if no in soiA.items:
            while soiA.top() != no:
                print("POP: ",soiA.top())
                soiB.push(soiA.pop())
            print("OUT: ",soiA.pop())
            while not soiB.isEmpty():
                soiA.push(soiB.top())
                print("PUSH: ",soiB.pop())
            print("SPACE ",soiA.SIZE - soiA.size())
        elif soiA.isEmpty():
            print("ERROR: SOI EMPTY")
        else:
            print("ERROR: No Car Number ",no)
    elif cmd[0] == 'A':
        no = cmd[1]
        if soiA.isFull():
            print("ERROR: SOI FULL")
        else:
            soiA.push(no)
            print("ARRIVE ",no,"\tSPACE ",soiA.SIZE - soiA.size())
    elif cmd[0] == 'P':
        print("SOIA: ",soiA.items)