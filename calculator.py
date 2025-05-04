import pyfiglet

ascii_banner = pyfiglet.figlet_format("Calculator v1")
print(ascii_banner)

operator = input("Enter an operator (+ - / * hy (hypotenuse) ): ")

if operator == "+":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print (result)
    
elif operator == "-":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    prinr (result)
    
elif operator == "/":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print (result)
    
elif operator == "*":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print (result)
    
elif operator == "hy":
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    form = side1 ** 2 + side2 ** 2 
    result = form ** 0.5
    print(result)
    
else:
    print (f"{operator} is not a valid operator")