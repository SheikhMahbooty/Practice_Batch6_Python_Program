#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
#Input text " rADIOHEAD"
input_text = input("Enter text: ")
result = ""

#Check if text has upper and lower values and capitalize the first letter of the string
if input_text:
    result += input_text[0].upper()
    result += ''.join(char.lower() for char in text[1:])

#print text "Radiohead"
print("Capitalized:", result)
