num1 = float(input("Enter the first number: "))
operator = input("Select operator +, -, *, /: ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("The answer is ", result)
elif operator == "-":
    result = num1 - num2
    print("The answer is ", result)
elif operator == "*":
    result = num1 * num2
    print("The answer is ", result)
elif operator == "/":
    result = num1 / num2
    print("The answer is ", result)
else:
    print("Invalid Operator")
