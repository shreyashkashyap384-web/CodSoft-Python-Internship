# Program named as Simple Calculator 
# This program performs basic arithmetic operations

print("Simple Calculator")

# First number input from the user
num1= float(input("Enter first number: "))

# Second number input from the user
num2= float(input("Enter second number: "))

# Operation choices to perform
print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User's operation choice
choice= input("\nEnter choice (1/2/3/4): ")

# Performing addition
if choice == '1':
    print("Result:", num1+num2)

# Performing subtraction
elif choice == '2':
    print("Result:", num1-num2)

# Performing multiplication
elif choice == '3':
    print("Result:", num1*num2)

# Performing division
elif choice == '4':

    # Checking division by zero
    if num2 != 0:
        print("Result:", num1/num2)
    else:
        print("Division by zero is not allowed\n")

# Handling invalid input
else:
    print("Invalid input")