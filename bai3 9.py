#This function adds two numbers
def add(x,y):
    return x+y
#This function subtracts two numbers
def subtracts(x,y):
    return x-y
#This function multiplies two numbers
def multiplies(x,y):
    return x*y
#This function divides two numbers
def divides(x,y):
    return x/y
print("1.Add")
print("2.Subtracts")
print("3.Multiplies")
print("4.Divides")


#Take input from the user
choice=input("Enter choice(1/2/3/4):")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtracts(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiplies(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divides(num1,num2))
else:
    print("Invalid input")
