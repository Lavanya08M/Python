def main():
    items_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total_amount = 0
    while True:
        try:
            # prompt user for an item
            item = input("Item: ").lower()

            # loop through each key in items_prices dictionary
            for key in items_prices.keys():
                # Check condition if key matches with user item
                if key.lower() == item:
                    # Add price value of that item to total amount
                    total_amount += items_prices[key]
            print(f"Total: ${total_amount}")
        except EOFError:
            break

if __name__ == "__main__":
    main()
