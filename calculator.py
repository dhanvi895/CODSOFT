# Simple Calculator Program

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user for operation choice
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

# Perform calculation based on user choice
if choice == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please choose a valid operation (1-4).")