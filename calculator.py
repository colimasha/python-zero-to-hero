
operator = input("Input your operator(+ - / *)?: ")
num1 = float(input("Enter you 1st number?: "))
num2 = float(input("Enter you 2nd number?: "))


if operator == "+":
   result = num1 + num2
   print({round(result,2)})
elif operator == "-":
    result = num1 - num2
    print({round(result,2)})
elif operator == "*":
    result = num1 * num2
    print({round(result,2)})
elif operator == "/":
    result = num1 / num2
    print({round(result,2)})
else:
    print("Invalid operator")