from Stack import Stack

stk = Stack()
text = "( a+b-c }*[d+e]/{f*(g+h) }"
print(text)

isMatch = True
for i in text:
    if i in ('{','[','('):
        stk.push(i)
    elif i == '}':
        if stk.isEmpty() or stk.top() != '{':
            isMatch = False
            break
        else:
            stk.pop()
    elif i == ']':
        if stk.isEmpty() or stk.top() != '[':
            isMatch = False
            break
        else:
            stk.pop()
    elif i == ')':
        if stk.isEmpty() or stk.top() != '(':
            isMatch = False
            break
        else:
            stk.pop()
    print(" ",end='')
if not isMatch or not stk.isEmpty():
    print("^", "MISMATCH")
else:
    print("\rMATCH")
