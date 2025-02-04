#function to cheack polindrom number 
import os

# Read numbers from environment variables
number1 = os.getenv("NUMBER1", "121")  # Default to "121" if not set
number2 = os.getenv("NUMBER2", "123")  # Default to "123" if not set

# Ensure inputs are treated as strings
number1 = str(number1)
number2 = str(number2)

# Check if either number is a palindrome
if number1 == number1[::-1] or number2 == number2[::-1]:
    print(f"One of the numbers ({number1} or {number2}) is a palindrome.")
else:
    print(f"Neither {number1} nor {number2} is a palindrome.")
