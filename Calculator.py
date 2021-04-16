def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def main():
    print("Calculator Options")
    print("1. Adding two numbers")
    print("2. Subtracting two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    
    while True:
        choice = input("Enter your choice: ")
        if choice in (1, 2, 3, 4):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == 1:
                print("Answer = " + str(add(x, y)))

            elif choice == 2:
                print("Answer = " + str(sub(x, y)))

            elif choice == 3:
                print("Answer = " + str(mult(x, y)))

            elif choice == 4:
                print("Answer = " + str(div(x, y)))
            break
        else:
            print("Invalid Input")

main()