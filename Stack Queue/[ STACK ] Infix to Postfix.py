from Stack import Stack

text = [25, '/','(', 3, '*', '(', 2, '+', 3, ')',')']
output = []
stk = Stack()

for i in text:
    if i in ['+','-']:
        while not stk.isEmpty() and stk.top() in ['*','/','+','-']:
            output.append(stk.pop())
        stk.push(i)
    elif i in ['*','/']:
        while not stk.isEmpty() and stk.top() in ['*','/']:
            output.append(stk.pop())
        stk.push(i)
    elif i in ['(']:
        stk.push(i)
    elif i in [')']:
        while stk.top() not in ['(']:
            output.append(stk.pop())
        stk.pop() # pop out '('
    else:
        output.append(i)

while not stk.isEmpty():
    output.append(stk.pop())

print(output)