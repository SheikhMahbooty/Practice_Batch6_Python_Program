#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#input text "thom yorke"
text = input("Enter text: ")
char = input("Enter character: ") #input character "o"

for i in range(len(text) - 1, -1, -1):
    if text[i] == char:
        print(f"Last '{char}' at index {i}")
        break
else:
    print(f"'{char}' not found.")

