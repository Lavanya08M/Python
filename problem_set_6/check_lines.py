import sys

def main():
    try:
        # User input
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        print(x+y)
    except ValueError:
        sys.exit("Enter integers only")

if __name__ == "__main__":
    main()