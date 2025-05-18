def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        try:
            operation = input("Select operation (1-5 or +-*/): ").strip()
            
            if operation == '5' or operation.lower() == 'exit':
                print("Exiting calculator...")
                break
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '1' or operation == '+':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operation == '2' or operation == '-':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operation == '3' or operation == '*':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operation == '4' or operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Invalid operation! Please enter 1-5 or +-*/")
            
            print("\n" + "="*30 + "\n")
            
        except ValueError:
            print("Error: Please enter numbers only!")
        except Exception as e:
            print(f"Unknown error: {e}")

if __name__ == "__main__":
    calculator()
