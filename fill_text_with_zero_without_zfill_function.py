#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

#input text "69420"
input_text = input("Enter number/s: ")
input_width = int(input("Enter total width: ")) #add desired zeros "10"

#add the remaining zeros missing from the inputted width
if input_width > len(input_text):
    zero_count = "0" * (input_width - len(input_text))
    result = zero_count + input_text
else:
    result = input_text

#print output "0000069420"
print(result)