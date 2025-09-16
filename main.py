# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")

# TODO: Ask the user for their name using input()
name = input("What is your name?")

# TODO: Ask how many smoothies they want to buy
smoothies = input("How many smoothies would you like to buy?")

# TODO: Convert the number of smoothies to an integer
smoothies = int(smoothies)

# TODO: Calculate the total cost (each smoothie costs £3.50)
    smoothie_cost = 3.50
total_cost = smoothies * smoothie_cost

# TODO: Display a message using a formatted string
print(f"Thank you,{name}")
print(f"Your total cost is: £{total_cost:.2f}")

# OPTIONAL CHALLENGE:
# Ask if the customer wants a reusable cup for £1.00 extra
# Add the cost if they say yes
