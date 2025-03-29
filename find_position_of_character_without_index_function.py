#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#input text "thom yorke"
text = input("Enter a text: ")
char = input("Enter character to find: ") #input character "o"

position = -1
for i in range(len(text)):
    if text[i] == char:
        position = i
        break

if position != -1:
    print(f"First occurrence at index {position}")
else:
    print("Character not found.")