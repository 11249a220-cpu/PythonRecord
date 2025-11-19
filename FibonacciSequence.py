# Function to print Fibonacci sequence
def fibonacci(n):
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
print(a, end=' ')
a, b = b, a + b

16 | P a g e

# Get user input
N = input("Enter the number of terms (N > 0): ")
# Validate input
if N.isdigit():
N = int(N)
if N > 0:
fibonacci(N)
else:
print("Invalid input. Please enter a number greater than 0.")
else:
print("Invalid input. Please enter a positive integer.")

SAMPLE OUTPUT:
Enter the number of terms (N > 0): 6
Fibonacci sequence:
0 1 1 2 3 5
Enter the number of terms (N > 0): 0
Invalid input. Please enter a number greater than 0
