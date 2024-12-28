def main():
    greeting = input("Greeting: ").strip().lower()
    amount = 0

    if greeting.startswith("hello"):
        amount = 0
    elif greeting.startswith("h"):
        amount = 20
    else:
        amount = 100
    
    print(f"${amount}")

if __name__ == "__main__":
    main()

