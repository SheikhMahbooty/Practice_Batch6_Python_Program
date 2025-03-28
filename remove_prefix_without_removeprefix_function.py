#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#Input text
text = input("Input text: ")
prefix = input("Enter prefix to remove: ")

#Loop for manual removing
if text.startswith(prefix):
    result = text[len(prefix):]
else:
    result = text

print("Result:", result)