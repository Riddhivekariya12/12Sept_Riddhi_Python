num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

#----------------without temporary variable-------------------#

print("num1=",num2)
print("num2=",num1)

num1 = num2
num2 = num1



#---------------temporary variable-----------# 

temp = num1
num1 = num2
num2 = temp 

print("num1=",num1)
print("num2=",num2)