
# ROYAL CAFE MANAGEMENT SYSTEM

# Menu with item names and prices
menu = {
    "Coffee": 80,
    "Tea": 40,
    "Burger": 120,
    "Pizza": 200,
    "Sandwich": 100
}

# Stores customer orders
order = []

# Cafe details stored in a tuple
cafe_info = ("Royal Cafe", "Sehore", "10:00 AM - 10:00 PM")


# Function to show cafe details
def show_cafe_info():
    print("\n" + "=" * 30)
    print("       WELCOME TO ROYAL CAFE")
    print("=" * 30)
    print("Location :", cafe_info[1])
    print("Timings  :", cafe_info[2])
    print("=" * 30)


# Function to display the menu
def show_menu():
    print("\n" + "-" * 30)
    print("          MENU")
    print("-" * 30)

    for item, price in menu.items():
        print(f"{item:<10} : Rs. {price}")

    print("-" * 30)


# Function to take the customer's order
def take_order():
    print("\nPlace your order:")

    while True:
        show_menu()

        item = input(
            "\nEnter item name or type 'done' to finish: "
        ).capitalize()

        if item == "Done":
            print("Order completed.")
            break

        if item in menu:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    order.append((item, quantity))
                    print(f"{quantity} x {item} added to your order.")
                else:
                    print("Quantity should be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Sorry, this item is not available.")


# Function to generate the final bill
def generate_bill():
    print("\n" + "=" * 30)
    print("           BILL")
    print("=" * 30)

    total = 0

    for item, quantity in order:
        price = menu[item]
        amount = price * quantity

        print(f"{item} x {quantity} = Rs. {amount}")
        total += amount

    print("-" * 30)
    print(f"Total Bill = Rs. {total}")
    print("=" * 30)
    print("Thank you for visiting Royal Cafe!")

    return total


# Main function
def main():

    print("Welcome to Royal Cafe!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Cafe Information")
        print("2. Show Menu")
        print("3. Place Order")
        print("4. Generate Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_cafe_info()

        elif choice == "2":
            show_menu()

        elif choice == "3":
            take_order()

        elif choice == "4":
            if len(order) == 0:
                print("\nNo order has been placed yet.")
            else:
                generate_bill()

        elif choice == "5":
            print("\nThank you for visiting Royal Cafe!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()

