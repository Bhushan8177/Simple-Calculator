# Simple-Calculator using Python


print("This is a SIMPLE CALCULATOR")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a>b:
        a-=b 
        return a
    else :
        b-=a
        return b
def mult(a,b):
    a*=b
    return a
def div(a,b):
    p=a/b
    q=a%b
    print("The quotient is ",p)
    print("The remainder is ",q)
def sqr(num):
    x= num**0.5
    return x
while(True):
    print("Choose what operation you want to perform")
    print("1.Addition")
    print("2.Subtraction ")
    print("3.Multiplication")
    print("4.Division")
    print("5.Square Root")
    choice= int(input("Enter your choice= "))
    if choice==1:
        num1= int(input("Enter First no= "))
        num2= int(input("Enter Second no= "))
        s= sum(num1,num2)
        print("The Sum is ",s)
    elif choice==2:
        num1= int(input("Enter First no= "))
        num2= int(input("Enter Second no= "))
        m = sub(num1,num2)
        print("The Subtraction is ",m)
    elif choice==3:
        num1= int(input("Enter First no= "))
        num2= int(input("Enter Second no= "))
        z= mult(num1,num2)
        print("The Multipication is ",z)
    elif choice==4:
        num1= int(input("Enter First no= "))
        num2= int(input("Enter Second no= "))
        div(num1,num2)
        print("The Division is",div)
    elif choice==5:
        num= int(input("Enter the number= "))
        m=sqr(num)
        print("Square Root of given number is ",m)
    else:
        print("No ThankYou!")
        break

