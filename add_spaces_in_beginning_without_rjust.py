#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
#input text "i love radiohead"
text = input("Enter text: ")
width = 10 #initial value

spaces = " " * (width - len(text))
result = spaces + text

#print the result "   i love radiohead"
print(f"'{result}'")
