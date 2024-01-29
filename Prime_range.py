def isPrime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
    
    
n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    if isPrime(i)==True:
        print(i)
    
