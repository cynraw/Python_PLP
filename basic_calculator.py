num1 = float(input("num1:"))
num2 = float(input("num2:"))
operand = input("Enter the operation you want to do ('+', '-','*', '/'):")

if operand == "+":
	result = num1 + num2
elif operand == "-":
	result = num1 - num2
elif operand == "/":
	result = num1 / num2
elif operand == "*":
	result = num1 * num2
elif operand == "**":
	result = num1 ** num2
elif operand == "%":
	result = num1 % num2
else:
 result = "Invalid operator!"

print(result)
