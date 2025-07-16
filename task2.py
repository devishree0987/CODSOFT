def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero."""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def get_number_input(prompt):
    """
    Prompts the user for a number and handles invalid input.
    Keeps prompting until a valid number is entered.
    """
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_choice():
    """
    Prompts the user for an operation choice and handles invalid input.
    Keeps prompting until a valid operation is entered.
    """
    while True:
        print("\nSelect operation:")
        print("1. Add      (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide   (/)")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ").strip()
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def main():
    """Main function to run the calculator application."""
    print("Welcome to Simple Calculator!")

    while True:
        # Get operation choice from the user
        choice = get_operation_choice()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        result = None # Initialize result to None

        if choice == '1':
            result = add(num1, num2)
            operation_symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation_symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation_symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation_symbol = '/'

        # Display the result
        if isinstance(result, str) and "Error" in result:
            print(result) # Print error message directly
        else:
            print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")

        print("-" * 30) # Separator for next calculation

if __name__ == "__main__":
    main()