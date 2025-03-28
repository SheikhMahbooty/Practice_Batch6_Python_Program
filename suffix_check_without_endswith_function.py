#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
#input text "i love radiohead"
text = input("Enter text: ")
suffix = input("Enter ending text to check: ")

#Input suffix to verify
result = text[len(text) - len(suffix):] == suffix

#Verify if suffix ends with "radiohead"
print("Ends with suffix:", result)