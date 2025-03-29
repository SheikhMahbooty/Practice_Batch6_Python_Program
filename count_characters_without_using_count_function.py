#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

#input text "i am thom yorke"
input_text = input("Text: ")
selected_char = input("Char: ") #input character to count "o"

#print how many times the character appeared "o" = 2
print(sum(1 for characters in input_text if characters == selected_char))

