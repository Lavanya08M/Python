def main():
    # Ask the user to enter greeting
    greeting = input("Greeting: ").strip().lower()
    amount = 0

    # If greeting starts with "hello" amount given is zero 
    if greeting.startswith("hello"):
        amount = 0
    elif greeting.startswith("h"): # If greeting starts with "h" amount given is 20 dollars
        amount = 20
    else: # If greeting does not start with "hello" or "h" amount given is 100 dollars
        amount = 100

    # Print the amount
    print(f"${amount}")

if __name__ == "__main__":
    main()

