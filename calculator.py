def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error Division by zero"
    
def main():
    print("Hello ~Calculator!")
    print("Chose option:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Insert Option (1/2/3/4): ")

    num1 = float(input("Insert first number: "))
    num2 = float(input("Insert second number: "))

    if choice == '1':
        print("Result:", addition(num1, num2))
    elif choice == '2':
        print("Result:", substraction(num1, num2))
    elif choice == '3':
        print("Result:", multiplication(num1, num2))
    elif choice == '4':
        print("Result:", division(num1, num2))
    else:
        print("Incorect option")

if __name__ == "__main__":
    main()