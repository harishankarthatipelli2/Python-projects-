def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
       print(a//b)
    except ZeroDivisionError:
       return 0
    return a/b
    
print("------------THE CALCULATOR--------------")
flag=True
while flag:
    print()
    print("1.ADDITION")
    print("2.SUBTRACTION") 
    print("3.MULTIPLICATION")
    print("4.DIVISON")
    print("0.EXIT")
    print()
    choice=input("ENTER YOUR CHOICE:")
    if choice=="1":
        a= int(input("ENTER THE VALUE OF A:"))
        b= int(input("ENTER THE VALUE OF B:"))
        print("ADDITION =",add(a,b))
    elif choice=="2":
        a= int(input("ENTER THE VALUE OF A:"))
        b= int(input("ENTER THE VALUE OF B:"))
        print("SUBTRACTION =",sub(a,b))    
    elif choice=="3":
        a= int(input("ENTER THE VALUE OF A:"))
        b= int(input("ENTER THE VALUE OF B:"))
        print("MULTIPLICATION =",mul(a,b))
    elif choice=="4":
        a= int(input("ENTER THE VALUE OF A:"))
        b= int(input("ENTER THE VALUE OF B:"))
        print("DIVISON =",div(a,b))
    else:
        flag=False
        print("EXIT")
