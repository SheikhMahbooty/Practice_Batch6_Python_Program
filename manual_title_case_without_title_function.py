#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

#input text "I LOVE RADIOHEAD"
text = input("Enter text: ")

split_words = text.split()
result = []

#like in program 1, use split to split the words and capitalize the first letter and lower the others
for word in split_words:
    if word:
        new_word = word[0].upper() + word[1:].lower()
        result.append(new_word)

title_case_text = " ".join(result)

#print "I Love Radiohead"
print("Title case:", title_case_text)

