from Queue import Queue

text = "I love Python"
series = [2,5,6,1,8,3]

def enCoder(text,series):
    q = Queue()
    for i in series:
        q.push(i)
    returnString = ""
    for i in text:
        if 'a' <= i <= 'z':
            returnString += chr((ord(i) - ord('a') + q.front()) % 26 + ord('a'))
            q.push(q.pop())
        elif 'A' <= i <= 'Z':
            returnString += chr((ord(i) - ord('A') + q.front()) % 26 + ord('A'))
            q.push(q.pop())
        else:
            returnString += i
    return returnString

def deCoder(text,series):
    q = Queue()
    for i in series:
        q.push(i)
    returnString = ""
    for i in text:
        if 'a' <= i <= 'z':
            returnString += chr((ord(i) - ord('a') - q.front()) % 26 + ord('a'))
            q.push(q.pop())
        elif 'A' <= i <= 'Z':
            returnString += chr((ord(i) - ord('A') - q.front()) % 26 + ord('A'))
            q.push(q.pop())
        else:
            returnString += i
    return returnString


out = enCoder(text,series)
print(out)
print(deCoder(out,series))


q = Queue()

for i in series:
    q.push(i)

output = ""
for i in text:
    if 'a' <= i <= 'z':
        number = q.pop()
        output += str(chr(((ord(i) - ord('a') + number ) % 26) + ord('a')))
        q.push(number)
    elif 'A' <= i <= 'Z':
        number = q.pop()
        output += str(chr(((ord(i) - ord('A') + number ) % 26) + ord('A')))
        q.push(number)
    else:
        output += i

print(output)

q = Queue()

for i in series:
    q.push(i)

decode = ""

for i in output:
    if 'a' <= i <= 'z':
        number = q.pop()
        decode += str(chr((ord(i) - ord('a') - number) % 26 + ord('a')))
        q.push(number)
    elif 'A' <= i <= 'Z':
        number = q.pop()
        decode += str(chr((ord(i) - ord('A') - number) % 26 + ord('A')))
        q.push(number)
    else:
        decode += i

print(decode)
