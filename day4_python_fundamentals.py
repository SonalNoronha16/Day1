"""
a={"sonal":22}
print(a)

student={
    "Name":"sona",
    "Age":22,
    "Course":"Engineering"
}
print(student["Name"])
student["age"]=23
student["city"]="Delhi"
print(student)
"""
"""
marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history", 0))
marks.update({"hindi": 100})

for subject, score in marks.items():
    print(subject, score)
"""
"""
purchases = {
    "Alice": 250,
    "Bob": 400,
    "Charlie": 150
}
print(len(purchases))
print("Customer Names:", purchases.keys())
print("Purchase Amounts:", purchases.values())
print("Alice's Purchase:", purchases.get("Alice"))
purchases.update({"David": 500})
print("After Adding David:", purchases)
purchases.pop("Charlie")
print("After Removing Charlie:", purchases)

for name, amount in purchases.items():
    print(f"{name} spent ₹{amount}")
"""
"""
# Input dictionary from user
n = int(input("Enter number of customers: "))
user_purchases = {}

for i in range(n):
    name = input("Enter customer name: ")
    amount = int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name] = amount

print("Top Spending Customer:", top_customer)
print("Customer Purchase Data:", user_purchases)
"""
"""
# Input dictionary from user
n = int(input("Enter number of customers: "))
user_purchases = {}

for i in range(n):
    name = input("Enter customer name: ")
    amount = int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name] = amount

top_customer = max(user_purchases, key=user_purchases.get)

print("Top Spending Customer:", top_customer)
print("Customer Purchase Data:", user_purchases)
"""
"""
numbers = {1, 2, 3, 3, 4}
print(numbers)

numbers.add(5)
print(numbers)
"""
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A & B)

print(3 in A)