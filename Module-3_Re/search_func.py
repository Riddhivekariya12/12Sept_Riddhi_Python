import re


mystr="This is Python!"

x=re.search('is',mystr)
#print(x)

if x: #TRUE
    print("Match done!")
    print(x)
else:
    print("Error!")