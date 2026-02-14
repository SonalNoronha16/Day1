
#The Trend Tracker
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

plt.plot(months, revenue)

plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 11]

plt.plot(x, y)
plt.show()


x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.scatter(x, y)
plt.show()


categories = ['A', 'B', 'C']
values = [11, 20, 15]

plt.bar(categories, values)
plt.show()


import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")
plt.subplot(1, 2, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()


#Correlation Checker
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

plt.scatter(study_hours, scores)

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Spent Studying")
plt.ylabel("Exam Score")

plt.show()


#The Comparison Dashboard
import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

months = [1, 2, 3, 4, 5]
revenue = [500, 700, 600, 900, 1200]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()

