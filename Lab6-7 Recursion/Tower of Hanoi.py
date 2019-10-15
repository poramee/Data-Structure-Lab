def towerOfHanoi(n,fr,to,ax):
    if n == 1:
        print("move",n,"from",fr,"to",to) # From A to C
    else:
        towerOfHanoi(n - 1,fr,ax,to) # From A to B
        print("move",n,"from",fr,"to",to) # From A to C
        towerOfHanoi(n - 1,ax,to,fr) # From B to C









dp = [None] * 100000
def fibo(n):
    if n <= 1:
        dp[n] = n
        return n
    elif dp[n] != None:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]

towerOfHanoi(2,'A','C','B')
# print(fibo(100))
