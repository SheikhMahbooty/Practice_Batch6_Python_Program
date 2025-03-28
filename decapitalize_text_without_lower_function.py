#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

#Input text "I LOVE RADIOHEAD"
text = input("Enter text: ")

#Manual listing of characters"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

#Transform characters to lowercase
decapitalized_text = text.translate(str.maketrans(uppercase, lowercase))

#Print result "i love radiohead"
print("Lowercase:", decapitalized_text)