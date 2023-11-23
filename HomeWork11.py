while True:
    a = int(input("Please enter first number: "))
    b = int(input("Please enter second number: "))
    c = input("Please enter action: +, -, * or / ! ")
    if c == "/":
        if b == 0:
            print("You can't divide by 0! ")
        else:
            x = a / b
            print(x)
    elif c == '+':
        x = a + b
        print(x)
    elif c == "-":
        x = a - b
        print(x)
    elif c == "*":
        x = a * b
        print(x)
    user_input = input("Please enter yes if you wish to continue: ").lower()
    if user_input != ('yes' or 'YES' or 'Yes' ):
        break
