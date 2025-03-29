#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#input text "i love radiohead"
input_text = input("Enter text: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

all_lower = True

#check text if characters are lowercase
for char in input_text:
    if char in uppercase:
        all_lower = False
        break

#print "I LOVE RADIOHEAD"
print(all_lower)


