#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

#input text "i love radiohead     "
input_text = input("Type your text: ")
result = ' '.join(input_text.split())
print(f"'{result}'")