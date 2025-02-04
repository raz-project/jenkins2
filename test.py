#function to cheack polindrom number 
poli = True
number1 = 25
number2 = 22
while poli:
 
   # Ensures the input is a valid number
    if number1 == number1[::-1] or number2 == number2[::-1]:  # Compare original with its reverse
        print(f"{number1} is a palindrome.")
        print(f"{number1} is a palindrome.")
        poli = False
        break
    else:
        print(f"{number1} is not a palindrome.")
        print(f"{number1} is not a palindrome.")
