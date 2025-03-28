#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

#input text "i love radiohead"
text = input("Enter text: ")
input_width = int(input("Enter width: ")) #input the width "15"

spaces_added = max(0, input_width - len(text))
result = " " * (spaces_added // 2) + text + " " * (spaces_added - spaces_added // 2)

#print result "    i love radiohead    "
print(f"'{result}'")