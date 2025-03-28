#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
#Input text "i love radiohead"
text = input("Enter text: ")
width = int(input("Enter desired width: "))

#Enter width: 10
spaces_to_add = width - len(text)
if spaces_to_add > 0:
    space_added_text = text + (" " * spaces_to_add)
else:
    space_added_text = text

#Print 'i love radiohead     '
print(f"Result: '{space_added_text}'")