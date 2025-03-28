#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#input text I LOVE RADIOHEAD
text = input("Enter text: ")

#Initial value
all_upper = True 

#Check if theres any lowercase characters
for char in text:
    if 'a' <= char <= 'z':  
        all_upper = False
        break

#Print True if all characters are uppercase
print("Are all characters uppercase:", all_upper)