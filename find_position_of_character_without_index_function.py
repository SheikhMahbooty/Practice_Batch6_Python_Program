#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

#input text "thom yorke"
input_text = input("Enter a text: ")
chosen_char = input("Enter character to find: ") #input character "o"

#find position
position = -1
for index in range(len(input_text)):
    if input_text[index] == chosen_char:
        position = index
        break

#print where the character is "2"
if position != -1:
    print(f"First occurrence at index {position}")
else:
    print("Character not found.")