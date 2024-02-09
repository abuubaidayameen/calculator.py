# NAME:ABU_UBAIDA.
# EMAIL:abuubaidayameen12@gmail.com





# MAKING CALCULATOR USING PYTHON PROGRAMMING.

print("select operator to perform:")
print("1. add")
print("2.subtract")
print("3.multiply")
print("4.divide")

num1 = int(input('Enter the value 1 :'))
num2 = int(input("Enter the value 2:"))
opr=input("Enter the opr(add,subtract,multiply,divide)")
if opr == "add":
    print(num1+num2)
    
if opr == "subtract":
    print(num1 - num2)
if opr == "multiply":
    print(num1 * num2)
if opr == "divide":
    print(num1/num2)
    
if  opr!= "+" and opr!="-" and opr!="*" and opr!="/":
    print("Invalid opr.....")