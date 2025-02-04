#function to cheack polindrom number 
poli = True

while poli:
 number = input("Enter a number: ")
 if number.isdigit():  # Ensures the input is a valid number
    if number == number[::-1]:  # Compare original with its reverse
        print(f"{number} is a palindrome.")
        poli = False
        break
    else:
        print(f"{number} is not a palindrome.")
 else:
     print("Please enter a valid number.")