#The Product Catalog 
import pandas as pd

products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

laptop_price = products.loc['Laptop']

first_two = products.iloc[:2]

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Indexing):")
print(first_two)

#The Grade Filter
import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing_values = grades.isnull()

filled_grades = grades.fillna(0)

filtered_scores = filled_grades[filled_grades > 60]

print("Original Series:")
print(grades)

print("\nMissing Values (True indicates missing):")
print(missing_values)

print("\nSeries After Filling Missing Values with 0:")
print(filled_grades)

print("\nScores Greater Than 60:")
print(filtered_scores)

#The Username Formatter
import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned = usernames.str.strip()

cleaned = cleaned.str.lower()

contains_a = cleaned.str.contains('a')

print("Cleaned Usernames:")
print(cleaned)

print("\nNames Containing 'a':")
print(contains_a)


#Intro
import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)

#Indexing and Selecting
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

#Boolean Masking
scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)

#Handling Missing Data
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(5))

#Vectorized String Operations
names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('a'))

