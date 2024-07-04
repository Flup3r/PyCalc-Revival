def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"
        
def my_sum(numbers):
    return sum(numbers)

def average(numbers):
    return sum(numbers) / len(numbers)

def main():
    print("Hello ~Calculator!")
    print("Choose option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sum of a list of numbers")
    print("6. Average of a list of numbers")

    choice = input("Insert Option (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Insert first number: "))
        num2 = float(input("Insert second number: "))

        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
    elif choice in ['5', '6']:
        numbers = list(map(float, input("Insert numbers separated by space: ").split()))

        if choice == '5':
            print("Result:", my_sum(numbers))
        elif choice == '6':
            print("Result:", average(numbers))
    else:
        print("Incorrect option")

if __name__ == "__main__":
    main()