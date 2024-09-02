def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Main program loop
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    operation = input("Choose an operation (+, -, *, /): ")
    
    result = calculate(num1, num2, operation)
    
    print(f"The result is: {result}")
    
    another = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another != 'yes':
        print("PROGRAM CLOSED!")
        break
