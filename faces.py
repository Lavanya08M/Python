def main():
    user_input = input()
    result = convert(user_input)
    print(result)

def convert(usr_input):
    if ":)" in usr_input:
        usr_input = usr_input.replace(":)", "🙂")
    elif ":(" in usr_input:
        usr_input = usr_input.replace(":(", "🙁")
    else:
        pass
    return usr_input

if __name__ == "__main__":
    main()

