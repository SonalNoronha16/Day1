
"""def greet():
    print("Hello, Welcome to internship!")
greet()
"""
"""
def add_number(a,b):
    return a+b
result=add_number(5,7)
print("The sum is:",result)
"""
"""
x= 10
def show_value():
    x = 5
    print(x)
show_value()
print(x)
"""
"""
import math
import random

print(math.sqrt(16))
print(random.randint(1, 10))
"""
"""
# Global variable
x = 10  
def my_function():
    # Local variable
    y = 5
    print("Inside function:")
    print("Global variable x =", x)
    print("Local variable y =", y)
my_function()
print("Outside function:")
print("Global variable x =", x)
"""
"""
import random
# Generate a random integer
num = random.randint(10, 50)
# Convert it to float
float_num = num / 10
print("Integer value:", num)
print("Floating-point value:", float_num)
"""
"""
import random
# Generate two random integers
a = random.randint(10, 50)
b = random.randint(10, 50)
# Convert to floating point
x = a / 10
y = b / 10
print("First number:", x)
print("Second number:", y)
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
"""
"""
utils.py
def multiply(a, b):
    return a * b
main.py
import utils
print(utils.multiply(3, 4))
"""
"""
#The Area and Perimeter Tool
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")
"""
import math_operations

result_power = math_operations.power(2, 10)
numbers = [10, 20, 30, 40]
result_avg = math_operations.average(numbers)

print("2^10 =", result_power)
print("Average =", result_avg)