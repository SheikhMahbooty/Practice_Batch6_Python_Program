#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#input text I LOVE RADIOHEAD
text = input("Enter text: ")

#Initial value
upper_case_state = True 

#Check if theres any lowercase characters
for character in text:
    if 'a' <= character <= 'z':  
        upper_case_state = False
        break

#Print True if all characters are uppercase
print("Are all characters uppercase:", upper_case_state)