#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function

input_text = input("Enter text: ")

#Split the text and use the first split and remove the leading spaces there
#Set the value to 0 so it can use the first split
index = input_text.find(text.split()[0])
modified_text = input_text[index:]

print("Without leading spaces:", modified_text)