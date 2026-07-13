
'''
#1
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a<b:
  print("Smallest number is",a)
else:
 print("Smallest number is",b)

#2
a=int(input("Enter the first  number:"))
b=int(input("Enter the secound number:"))
if a>b:
   print("lergest number is",a)
else:
   print("lergest number is",b)

#3
a=int(input("Enter the first number:"))
b=int(input("Enter the secound number:"))
if a<0:
    print("Absolute value is",-a)
else:
    print("Absoulte value is",b)

#4
a=int(input("Enter a number:"))
if a%2==0:
    print("Even number")
else:
    print("odd number")

#5
mult=int(input("Enter the number:"))
if mult%5==0:
    print("It is a multiple of 5")
else:
    print("It is a not multiple of 5")

#6
mult=int(input("Enter the given number:"))
if mult%10==0:
     print("It  is a multiple of 10")
else:
    print("It is a not multiple of 10")

#7
digit=int(input("Enter the number:"))
if 10 <=abs(digit) <=99:
    print("It is two digit number")
else:
    print("It is not two digit number")

#8
digit=int(input("Enter the number:"))
if 100 <=abs(digit) <=999:
     print("It is three digit number")
else:
    print("It is not three digit number")

#9
num=int(input("Enter the number:"))
if num%10==0:
    print("it end with zero")
else:
    print("it  does not end with zero")

#10
num=int(input("Enter the number:"))
if num * num >50:
    print("square is above 50")
else:
    print("square is below 50")

#11
num1 =int(input("Enter the first number:"))
num2=int(input("Enter the  secound number:"))
if num1 - num2==0:
    print("Difference is 0")
else:
    print("Difference is not 0")

#12
marks =int(input("Enter the chemistry marks:"))
if marks >=50:
    print("student is passed")
else:
    print("student is failed")

#13
num =int(input("Enter a number:"))
if num%10 ==0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")

#14
num= int(input("Enter a two digit number:"))
a = num//10
b = num%10
if a>b:
    print("Biggest digit =",a)
else:
    print("Biggest digit =",b)
 
#15
choice=int(input("Enter you choice:"))
if choice==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")
  
#16
a=int(input("Enter value:"))
if a==1:
    print("you can go out and play")
else:
    print("you cannot go out and play")

#17
a= int(input("Enter length:"))
b= int(input("Enter length:"))
if a==b:
    print("It is a square")
else:
    print("It is a rectangle")
 
#18
a=int(input("Enter ASCII value:"))
if a>=65 and a<=90:
    print("Uppercase alphabet")
else:
    print("Not an uppercase alphabet")

#19
a=int(input("Enter ASCII value:"))
if a >=97 and a >=122:
    print("Lowercase alphabet")
else:
    print("Not a lowercase alphabet")

#20
a=int(input("Enter ASCII value:"))
if a >=48 and a >=57:
    print("Numeric character")
else:
    print("Not a numeric character")
'''
#21
num=int(input("Enter a number:"))
if num%5==0 and num%3==0:
    print("The number is a multiple of both 5 and 3")
else:
    print("The number is not a multiple of both 5 and 3")
 
#22
num=int(input("Enter a number:"))
if num >=100 and num <=999 and num%10==0:
    print("The number is a three-digit number and a multiple of 10")
else:
    print("The number is not a three-digit  number and a multiple of 10") 

#23
num=int(input("Enter a  number:"))
if num >=100 and num <=999 and num%2==0 and num%5==0 and num%10==0:
    print("The number is a  three-digit number and a multiple of 2,5 and 10")
else:
    print("The number is not a three-digit number and a multiple of 2,5 and 10")
''
#24
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a%2==0 and b%2==0:
    print("product=",a*b)
else:
    print("sum=",a+b)

#25
n=int(input("Enter a number:"))
if n%7==0 or n%10==7:
      print("Buzz number")
else:
    print("Not a buzz number")

#1

a=int(input("Enter first  number:"))
b=int(input("Enter secound number:"))
c=int(input("Enter third number:"))
if a >=b and a >=c:
      print("Largest =",a)
elif b >=a and b >=c:
      print("Largest =",b)
else:
      print("Largest =",c)

#2

a=int(input("Enter first  number:"))
b=int(input("Enter secound number:"))
c=int(input("Enter third number:"))
if a <=b and a <=c:
      print("Largest =",a)
elif b <=a and b <=c:
      print("Largest =",b)
else:
      print("Largest =",c)

#3

n=int(input("Enter a number:"))
if n>0:
      print("positive")
elif n<0:
      print("negative")
else:
      print("zero")

#4
d=int(input("Enter number of late days:"))
if d <=5:
      fine =d*0.40
elif d <=10:
      fine =d*0.65
else:
      fine =d*0.80
print("fine =",fine)

#5
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter operator(+,-,*,/):"))
if op =="+":
      print("answer =",a+b)
elif op =="-":
      print("answer =",a-b)
elif op =="*":
      print("answer =",a*b)
elif op =="/":
      print("answer =",a/b)
else:
      print("Invalid operator")

#6

n=int(input("enter a number:"))
if n%5==0 and n%3==0 and n%7==0:
      print("multiple of 5,3 and 7")
else:
      print("Not a multiple of 5,3 and 7")

#7
w=int(input("Enter weight in gm:"))
t=input("Enter booking type(O/E):")
if t == "0":
    if w <=100:
        charge =80
    elif w <=500:
        charge =150
    elif w <=1000:
        charge =210
    else:
        charge =250
elif t =="E":
      if w<=100:
        charge =100
      elif w <=500:
        charge =200
      elif w <=1000:
        charge =250
else:
      print("Invalid booking type")
      charge=0
      print("charge =",charge)

#8
price= int(input("Enter laptop price:"))
if price <=5000:
      dis =0
elif price <=100000:
      dis =price *10/100
elif price <=150000:
      dis =price *15/100
else:
      dis =price *20/100
print("Discount =", dis)
print("Total price =",price -dis)
























      
















































      





































      















































































    
    
