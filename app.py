# 1. This is a comment. The computer ignores it, but it helps humans read the code.

# 2. Print a welcome message to the screen
print("Hello! Welcome to your first Python script.")

# 3. Variables and User Input
# We ask the user for their name and store it in a variable called 'user_name'
user_name = input("What is your name? ")
print(f"Great to meet you, {user_name}!")

# We ask for a number. input() always treats data as text, so we convert it to an integer using int()
user_number = int(input("Enter a number to count up to (e.g., 5): "))

# 4. Conditional Logic (If / Else)
# Check if the number is less than or equal to 0
if user_number <= 0:
    print("Please enter a number greater than 0 next time!")
else:
    print(f"Excellent! Let's count up to {user_number}:")
    
    # 5. Loops
    # The 'for' loop will run a specific number of times, starting from 1
    for i in range(1, user_number + 1):
        print(f"Number: {i}")

print("Script finished successfully!")
