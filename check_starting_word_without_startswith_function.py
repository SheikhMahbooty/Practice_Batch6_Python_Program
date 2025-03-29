#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#input text "radio head"
text = input("Enter text: ")
prefix = input("Enter prefix: ")

matches = text[:len(prefix)] == prefix

print(matches)