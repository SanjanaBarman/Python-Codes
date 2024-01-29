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
 '''Enter the value of n:55
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53'''   
