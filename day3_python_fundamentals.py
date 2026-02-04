"""
#List examples
numbers=[10,20,30,40]
#Tuple example
coordinates=(5,10)
print(numbers)
print(coordinates)
#range
a=[100,200,300,400,500,600,700,800,900]
print(a[-3:-1])
print(a[1:4:3])
print(a[2:9:2])
print(a[-4:-1:2])
"""
"""
#change
marks=[85,72,90]
marks.append(88)
marks.pop()
marks.sort()
print(marks)
"""
"""
marks=[85,72,90]
marks.reverse()
print(marks)
"""
"""
#The Inventory Manager
inventory = ["Apples", "Bananas", "Carrots", "Dates"]

print("Current Inventory:", inventory)

inventory.append("Eggs")

inventory.remove("Bananas")

inventory.sort()

print("Final Updated Inventory:", inventory)
"""
"""
#The Data Slicer
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])

afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

last_three_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_three_hours)
"""
"""
#The Immutable Config
screen_res = (1920, 1080)

print("Current Resolution:", str(screen_res[0]) + "x" + str(screen_res[1]))

screen_res[0] = 1280 
"""
#The Fix
screen_res = (1920, 1080)

print("Current Resolution:", str(screen_res[0]) + "x" + str(screen_res[1]))

print("Tuples cannot be modified!")
