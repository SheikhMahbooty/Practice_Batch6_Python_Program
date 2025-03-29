#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#input text "radio head"
input_text = input("Enter text: ")
input_prefix = input("Enter prefix: ") #input prefix "radio"

#check if inputted prefix matches the text
prefix_match = input_text[:len(input_prefix)] == input_prefix

#print "true"
print(prefix_match)