def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("select operation")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
while True:
    choice=input("Enter the choice(1,2,3,4):")
    if choice in('1','2','3','4'):
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        if choice=='1':
           print(num1 ,"+", num2,"=",add(num1,num2))
        elif choice=='2':
           print(num1, "-",num2,"=", sub(num1,num2))
        elif choice =='3':
           print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
           print(num1,"1",num2,"=",divide(num1,num2))
        next_calculation=input("want to do next calculation?(yes/no)")
        if next_calculation=="no":
           break
    else:
        print("invalid input")
  
       
