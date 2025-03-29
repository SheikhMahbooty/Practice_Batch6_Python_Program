#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

#input text "123"
text = input("Enter number/s: ")
width = int(input("Enter total width: "))

#add the remaining zeros missing from the inputted width
if width > len(text):
    zeros = "0" * (width - len(text))
    result = zeros + text
else:
    result = text

print(result)