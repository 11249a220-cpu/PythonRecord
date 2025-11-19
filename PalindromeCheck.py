# Get input from the user
num = input("Enter a number: ")

# Check for palindrome
if num == num[::-1]:
print(f"{num} is a palindrome.")
else:
print(f"{num} is not a palindrome.")

# Count digit occurrences

14 | P a g e

digit_count = {}

for digit in num:
if digit.isdigit(): # Ensure only digits are considered
digit_count[digit] = digit_count.get(digit, 0) + 1

print("\nDigit Occurrence Count:")
for digit in sorted(digit_count):
print(f"Digit {digit} occurs {digit_count[digit]} time(s)")

SAMPLE OUTPUT:

Enter a number: 12321
12321 is a palindrome.

Digit Occurrence Count:
Digit 1 occurs 2 time(s)
Digit 2 occurs 2 time(s)
Digit 3 occurs 1 time(s)
