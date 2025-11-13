num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

arithmetic_operation = input("Choose the operation (+, -, *, /):")
match arithmetic_operation:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    case "/":
        if num2 ==0:
            print("Cannot divide by zero")
        else:
         result = num1 / num2
         print(f"The result of {num1} / {num2} is {result}")
    case _:
        print("Invalid operation selected.")
         
