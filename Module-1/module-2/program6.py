letter=input("enter any latter:")

def myvowel(letter):
    myvowels = "aeiou AEIOU"
    return letter in myvowels

if myvowel(letter):
    print("yay...The latter is vowel.")
else:
    print("opps...The latter is not vowel.")    