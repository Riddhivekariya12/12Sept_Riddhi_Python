new_a = (input("enter a string :"))
new_b = (input("enter a secound string : "))

print("before swap : ",new_a," ",new_b)

new_a = new_b[:2] + new_a[2:]
new_b= new_a[:2] + new_b[2:]

print("After Swap :",new_a," ",new_b)

