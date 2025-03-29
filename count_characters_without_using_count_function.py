#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
#input text "i am thom yorke"
text = input("Text: ")
char = input("Char: ") #input character to count "o"

#print how many times the character appeared "o" = 2
print(sum(1 for c in text if c == char))

