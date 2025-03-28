#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#Input text
input_text = input("Input text: ")
chosen_prefix = input("Enter prefix to remove: ")

#Loop for manual removing
if input_text.startswith(chosen_prefix):
    modified_result = input_text[len(chosen_prefix):]
else:
    modified_result = input_text

print(modified_result)