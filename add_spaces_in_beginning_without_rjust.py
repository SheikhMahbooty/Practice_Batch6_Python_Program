#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

#input text "i love radiohead"
input_text = input("Enter text: ")
text_width = 10 #initial value

spaces = " " * (text_width - len(input_text))
result = spaces + input_text

#print the result "   i love radiohead"
print(f"'{result}'")
