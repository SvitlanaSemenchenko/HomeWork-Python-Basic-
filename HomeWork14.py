def multiply_digits_until_nine(num):
    result = 1
    while num > 0:
        digit = num % 10
        result *= digit
        num //= 10
    while result > 9:
        temp_result = result
        result = 1
        while temp_result > 0:
            temp_digit = temp_result % 10
            result *= temp_digit
            temp_result //= 10
    print(result)

user_input = int(input("Please enter an integer: "))
multiply_digits_until_nine(user_input)
