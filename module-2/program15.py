mystring=input("enter a string :")
lenght = len(mystring)

if lenght > 2 :
    if mystring [-3] == 'ing':
        mystring += 'ly'
    else:
        mystring += 'ing'

print("new string:",mystring)    

