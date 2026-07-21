
'''
n=int(input("Enter a number"))
for i in range(1,n+1):
    print(i,end="")

    
n=int(input("Enter a number"))
for i in range(1,n+1):
    print(2*i,end="")

n=int(input("Enter a number:"))
i=1
while i<=n:
    print(i,end="")
    i+=1

n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(3*i,end="")

n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(5*i,end="")

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0 or i%3==0:
        print(i,end="")

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0 or i%5==0 or i%7==0:
        print(i,end="")

n=int(input("Enter a number:"))
c=0
i=1
while c<n:
    if i%3==0 or i%5==0 or i%7==0:
        print(i,end="")
        c+=1
        i+=1
        print(c)

n=int(input("Enter a number:"))
sum_digits=0
while num>0:
    digit=n%10
    sum_digits+=digit
    n//=0
print(sum_digits)

n=int(input("Enter a number:"))
c=0
while n>0:
    c+=1
    n//=10
    print(c)

n=int(input("Enter number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end="")

n=int(input("Enter a number:"))
c=0
for i  in range(1,n+1):
    if n%1==0:
        c+=1
        print(c)

n=int(input("Enter a number:"))
for n in range(2,n+1):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
        if is_prime:
            print("yes")
        else:
            print("No")

n=int(input("Enter a number:"))
for n in range(2,n+1):
    is_prime =True
    for i in range(2,n):
        if n%1==0:
            is_prime=False
            break
        if is_prime:
            print(n,end="")
            

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
gcf=1
for i in range(1,n+1):
    if a%i==0 and b%i==0:
        gcf=i
print(gcf)

a,b=0,1
print("fibonacci series till 50:")
while a<=50:
    print(a,end="")
    a,b=b,a+b

n=int(input("Enter number:"))
f=1
for i in range(1,n+1):
    f*=i
    print(f)

sum_even=0
sum_odd =0
print("Enter integers.enter 0 to stop.")
while True:
    n=int(input("Enter number:"))
    if n==0:
        break
    if num %2==0:
        sum_even+=n
    else:
        sum_odd+=n
        
n=int(input("Enter number:"))
o=n
r=0
while n>0:
    d=n%10
    r=r*10+d
    n//=10
if o==r:
    print("yes")
else:
    print("No")
'''
n=int(input("Enter number:"))
n= len(str(num))
t=num
sum=0
while t >0:
    d=t%10
    s+=d**n
    t//=10
if sum== num:
    print(n)
        




























        













    
    
            











































for i in range(1,n+1):
    if n%i==0:
        c+=1
        print(c)
























    
