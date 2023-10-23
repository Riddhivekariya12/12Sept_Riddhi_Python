main_string=(input("enter your first string:"))
substring=(input("enter ypur second string:"))

newstring=main_string[:2] + substring[:2] + " " + substring[:2] + main_string[:2] 
   
print(newstring)

