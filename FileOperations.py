def main():
# Step 1: Input file name
filename = input("Enter the filename: ")

# Step 2: Open file and display first N lines
file = open(filename, 'r')
N = int(input("Enter number of lines to display: "))
print(f"\nFirst {N} lines of the file:")

for i in range(N):
line = file.readline
if line == '':
print("End of file reached.")
break
print(line.strip())
file.close()

# Step 3: Count word frequency
word = input("\nEnter the word to find its frequency: ").lower()
file = open(filename, 'r')
content = file.read().lower()
frequency = content.count(word)
file.close()

print(f"\nThe word '{word}' occurred {frequency} times in the file.")

# Run the function
main()

SAMPLE OUTPUT:

Enter the filename: demo.txt
Enter number of lines to display: 2
Enter the word to find its frequency: data

First 2 lines of the file:
Data is essential in today’s world.
Big data is changing the industry.

The word 'data' occurred 2 times in the file.
