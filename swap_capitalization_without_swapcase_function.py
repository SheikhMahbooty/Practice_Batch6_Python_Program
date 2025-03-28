#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

#input text "i DONT lOvE rAdIoHEAD"
text = input("Enter text: ")
result = ""

#manually add characters a-z
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#for loop
for char in text:
    if char in lowercase:
        result += uppercase[lowercase.index(char)]
    elif char in uppercase:
        result += lowercase[uppercase.index(char)]
    else:
        result += char
        
#print "I dont LoVe RaDiOhead"
print("Swapcase result:", result)

