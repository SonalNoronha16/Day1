# The Personal Logger
name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

# Save to file in append mode
with open("journal.txt", "w") as file:

    file.write(f"Name: {name}, Daily Goal: {goal}\n")

print("Saved successfully!")
