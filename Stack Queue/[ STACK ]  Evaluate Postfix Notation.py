from Stack import Stack

stk = Stack()

text = [25, 3, 2, 3, '+', '*', '+']

for i in text:
    if i == '+':
        a = stk.pop()
        b = stk.pop()
        stk.push(b+a)
    elif i == '-':
        a = stk.pop()
        b = stk.pop() 
        stk.push(b-a)
    elif i == '*':
        a = stk.pop()
        b = stk.pop()
        stk.push(b*a)
    elif i == '/':
        a = stk.pop()
        b = stk.pop()
        stk.push(b/a)
    else:
        stk.push(i)

print(stk.pop())