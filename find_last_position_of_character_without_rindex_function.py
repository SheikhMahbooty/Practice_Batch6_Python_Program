#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#input text "thom yorke"
input_text = input("Enter text: ")
chosen_char = input("Enter character: ") #input character "o"

#find where the character appears last "6"
for index in range(len(input_text) - 1, -1, -1):
    if input_text[index] == chosen_char:
        print(f"Last '{chosen_char}' at index {index}") #print where it appears "6"
        break
else:
    print(f"'{chosen_char}' not found.")

