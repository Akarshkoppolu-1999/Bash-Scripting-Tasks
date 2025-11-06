num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    print("Invalid operator. Use +, -, or * only.")
    exit()  # stop program

print("Result:", result)