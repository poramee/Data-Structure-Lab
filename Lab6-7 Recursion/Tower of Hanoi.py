def towerOfHanoi(n,fr,to,ax):
    if n == 1:
        print("move",n,"from",fr,"to",to) # From A to C
    else:
        towerOfHanoi(n - 1,fr,ax,to) # From A to B
        print("move",n,"from",fr,"to",to) # From A to C
        towerOfHanoi(n - 1,ax,to,fr) # From B to C

towerOfHanoi(3,'A','C','B')