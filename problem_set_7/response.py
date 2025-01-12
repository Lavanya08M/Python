from validator_collection import validators
import sys

def main():
    try:
        if validators.email(input("What's your email address? ")):
            print("Valid")
    except:
        sys.exit("Invalid")

if __name__ == "__main__":
    main()