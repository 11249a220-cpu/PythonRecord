# Input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find length of shorter string
min_len = min(len(string1), len(string2))
max_len = max(len(string1), len(string2))

# Initialize match counter
match_count = 0

# Compare characters
for i in range(min_len):
if string1[i] == string2[i]:

22 | P a g e

match_count += 1

#Calculate similarity percentage
similarity = (match_count / max_len) * 100

# Output
print(f"String similarity: {similarity:.2f}%")

SAMPLE OUTPUT:

Enter the first string: apple
Enter the second string: apply
String similarity: 80.00%

Enter the first string: hello
Enter the second string: yellow
String similarity: 60.00%
