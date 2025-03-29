#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

#input text "i love radiohead"
input_text = input("Enter text: ")
suffix = input("Enter suffix to remove: ")

#remove the desired suffix "head"
if input_text.endswith(suffix):
    input_text = input_text[:len(input_text) - len(suffix)]

#print "i love radio"
print(input_text)
