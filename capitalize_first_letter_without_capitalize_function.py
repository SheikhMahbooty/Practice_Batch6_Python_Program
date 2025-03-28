#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
#Input text " rADIOHEAD"
text = input("Enter text: ")
result = ""

#Check if text has upper and lower values and capitalize the first letter of the string
if text:
    result += text[0].upper()
    result += ''.join(c.lower() for c in text[1:])

#print text "Radiohead"
print("Capitalized:", result)
