# Input
sentence = input("Enter a sentence: ")

# Initialize counters

20 | P a g e

word_count = len(sentence.split())
digit_count = 0
uppercase_count = 0
lowercase_count = 0

# Iterate over characters
for ch in sentence:
if ch.isdigit():
digit_count += 1
elif ch.isupper():
uppercase_count += 1
elif ch.islower():
lowercase_count += 1

# Output
print("Number of words:", word_count)
print("Number of digits:", digit_count)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)

SAMPLE OUTPUT:
Enter a sentence: Hello World 123!
Number of words: 3
Number of digits: 3
Number of uppercase letters: 2
Number of lowercase letters: 8
