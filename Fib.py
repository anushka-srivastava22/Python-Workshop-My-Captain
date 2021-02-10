n = int(input())

n1=0
n2=1
count = 0

if n <= 0:
    print ("Enter postive numbers")
elif n==1:
    print(n1)
else:
    print("Fibonacci Series")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1=n2
        n2=nth
        count += 1