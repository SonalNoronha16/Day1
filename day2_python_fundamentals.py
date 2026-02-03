age=21
print(type(21))
name="Sona"
print(type(name))
is_student=True
print(type(is_student))

a=input("Enter a number:")
print("The number is:",a)

##Simple calculator
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    print("Result:", num1 ** num2)
else:
    print("Invalid Output")

##Concatenation
name = input("Enter your name: ")
print("Welcome, " + name + "!")

##fstring
name = input("Enter your name: ")
print(f"Welcome, {name}!")

#typecasting
num1 = input("Enter number: ")
num2 = input("Enter number: ")
print(int(num1) + int(num2))   

"""
##The Age in 30 Calculator

name = input("Enter your name: ")
age = input("Enter your current age: ")

age = int(age)         
new_age = age + 4       

print(f"Hey {name}, you will be {new_age} years old in 2030!")
"""
"""
##The Bill Splitter

total_bill = float(input("Enter the total bill amount: "))

num_people = int(input("Enter the number of people: "))

share_per_person = total_bill / num_people

print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")

print("Data type of total_bill:", type(total_bill))
print("Data type of num_people:", type(num_people))
print("Data type of share_per_person:", type(share_per_person))
"""
"""
##The Raw Data Formatter

item_name = "Laptop"     
quantity = 2             
price = 499.99           
in_stock = True         

print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)

total_cost = quantity * price

print("Total Cost:", total_cost)
"""