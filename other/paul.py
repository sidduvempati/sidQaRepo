budget = int(input("Enter your budget: "))
shakes = {"1": 3, "2": 4, "3": 5}  # Dictionary of shake options and their prices

while True:
    print("Shake options:")
    for option, price in shakes.items():
        print(f"{option}. ${price}")

    choice = input("What can I fix you? (Enter Q to quit): ")

    if choice.upper() == "Q":
        print("Goodbye!")
        break

    if choice not in shakes:
        print("Invalid option.")
        continue

    price = shakes[choice]
    if price > budget:
        print("You can't afford that. Get out of here!")
        break

    print(f"Enjoy your shake for ${price}.")
    budget -= price
    print(f"Budget remaining: ${budget}")