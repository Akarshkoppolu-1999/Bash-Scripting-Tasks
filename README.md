**Bash Scripting Tasks (Python Implementations)

This repository contains four basic scripting exercises implemented in Python to simulate Bash-style automation tasks.
Each script demonstrates fundamental programming logic such as input handling, loops, and file operations.

** Task 1: Simple Calculator**

Description:
A script that takes two numbers and an operator (+, -, *) from the user and performs the respective arithmetic operation.

Code:

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    print("Invalid operator. Use +, -, or * only.")
    exit()

print("Result:", result)


Example Output:

Enter first number: 5
Enter operator (+, -, *): *
Enter second number: 3
Result: 15.0

Task 2: Count Files in Current Directory

Description:
Counts and prints how many files are present in the current working directory.

Code:

import os
items = os.listdir('.')
files = [f for f in items if os.path.isfile(f)]
print("Number of files in current directory:", len(files))


Example Output:

Number of files in current directory: 7

Task 3: Greeting Loop

Description:
Continuously asks the user to enter names and greets each person.
Stops when the user types "done".

Code:

while True:
    name = input("Enter a name (type 'done' to stop): ")

    if name.lower() == "done":
        print("Goodbye!")
        break

    print(f"Hello, {name}!")


Example Output:

Enter a name (type 'done' to stop): Akarsh
Hello, Akarsh!
Enter a name (type 'done' to stop): Sam
Hello, Sam!
Enter a name (type 'done' to stop): done
Goodbye!

Task 4: Temperature Converter

Description:
Converts a temperature from Celsius to Fahrenheit using the formula
F = C * 9/5 + 32.

Code:

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")


Example Output:

Enter temperature in Celsius: 37
37.0°C = 98.60°F

 How to Run the Scripts

You can run these scripts using VS Code terminal or Git Bash.

Steps:

Open the folder in VS Code or Git Bash.

Run any task file using:

python task1_calculator.py
python task2_count_files.py
python task3_greetings.py
python task4_temp_convert.py


Follow on-screen instructions.

 Conclusion

These tasks demonstrate simple command-line interaction, arithmetic operations, looping, and basic file handling — the core concepts useful in both Bash scripting and Python automation.
