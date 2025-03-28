#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function

input_text = input("Enter text: ")

#Split the text and use the first split and remove the leading spaces there
index = input_text.find(text.split()[0])
result = input_text[index:]

print("Without leading spaces:", result)