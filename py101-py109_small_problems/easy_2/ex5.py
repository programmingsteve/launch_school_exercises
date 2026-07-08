# Write a program that prompts the user for two positive numbers
# (floating-point), then prints the results of the following operations on
# those two numbers: addition, subtraction, product, quotient, floor quotient,
# remainder, and power. Do not worry about validating the input.

# Examples
# ==> Enter the first number:
# 3.141592
# ==> Enter the second number:
# 2.718282
# ==> 3.141592 + 2.718282 = 5.859874
# ==> 3.141592 - 2.718282 = 0.4233100000000003
# ==> 3.141592 * 2.718282 = 8.539732984944001
# ==> 3.141592 / 2.718282 = 1.1557270364149121
# ==> 3.141592 // 2.718282 = 1.0
# ==> 3.141592 % 2.718282 = 0.4233100000000003
# ==> 3.141592 ** 2.718282 = 22.45914942746313

def floating_point_arithmetic(x, y):
    print(
        f"{x} + {y} = {x + y}\n"
        f"{x} - {y} = {x - y}\n"
        f"{x} * {y} = {x * y}\n"
        f"{x} / {y} = {x / y}\n"
        f"{x} // {y} = {x // y}\n"
        f"{x} % {y} = {x % y}\n"
        f"{x} ** {y} = {x ** y}\n"
    )

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

floating_point_arithmetic(num1, num2)

# LS Solution
# def calculate(first, second, operator):
#     match operator:
#         case '+':  return first + second
#         case '-':  return first - second
#         case '*':  return first * second
#         case '/':  return first / second
#         case '//': return first // second
#         case '%':  return first % second
#         case '**': return first ** second
#
# first_float = float(input("==> Enter the first number:\n"))
# second_float = float(input("==> Enter the second number:\n"))
# for operator in ['+', '-', '*', '/', '//', '%', '**']:
#     operation = f"{first_float} {operator} {second_float}"
#     result = calculate(first_float, second_float, operator)
#     print(f"==> {operation} = {result}")
