def main():
    # Main function to prompt user input and check if the plate is valid
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    """
    Checks if the vanity plate meets the basic rules:
    1. Must be alphanumeric.
    2. Must start with at least two letters.
    3. Length must be between 2 and 6 characters.
    4. Numbers, if preent, must follow placement rules.
    """

    # Check if the string is alphanumeric, starts with 2 letters , and has a valid length
    if not s.isalnum() or not s[:2].isalpha() or not (2<=len(s)<=6):
        return False

    # Check for additional number placement rules
    if not is_valid_end_number(s):
        return False

    return True

def is_valid_end_number(s):
    """
    Checks the rules for number placement in the vanity plate:
    1. Numbers, if present, must appear at the end.
    2. Letters cannot appear after the number.
    3. The first number cannot be '0'.
    """

    # List to store the indices of digits in the string
    digits_index = []

    # Loop through each character in the string to find digits
    for i in range(len(s)):
        if s[i].isdigit():
            digits_index.append(i)
    
    # if there are any digits in the plate
    if len(digits_index) > 0:
        # Loop throgh the string to check rules for number placement
        for i in range(len(s)-1):
            # check if a digit is followed by a letter, or if the first number is '0'
            if (s[i].isdigit() and s[i+1].isalpha()) or s[digits_index[0]] == '0':
                return False
    
    # If no rules are violated, return True
    return True

if __name__ == "__main__":
    main()


           