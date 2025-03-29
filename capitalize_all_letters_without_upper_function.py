#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

#input text "i love radiohead"
input_text = input("Enter text: ")
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#initial value
result = ""

#change text from lower to uppercase
for char in input_text:
    if char in lowercase:
        index = lowercase.index(char)
        result += uppercase[index]
    else:
        result += char

#print "I LOVE RADIOHEAD"
print(result)