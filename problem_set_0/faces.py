def main():
    # Ask the user for input
    user_input = input()

    # Call convert function and store the result
    result = convert(user_input)

    # Print the result
    print(result)

def convert(usr_input):
    # If the user input contain :) emoticon replace it with smiling face emoji
    if ":)" in usr_input:
        usr_input = usr_input.replace(":)", "🙂")
    # If the user input contain :( emoticon replace it with frowning face emoji
    elif ":(" in usr_input:
        usr_input = usr_input.replace(":(", "🙁")
    # Do not change input if it does not contain emoticon
    else:
        pass
    return usr_input

if __name__ == "__main__":
    main()

