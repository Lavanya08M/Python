import sys
def main():
    names = []
    string = str("")
    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name.capitalize())
            else:
                sys.exit("please enter atleast one character")
        except EOFError:
            break

    length = len(names)
    if length == 1:
        string += names[0]
    elif length == 2:
        string += names[0] + " and " + names[1]
    elif length > 2:
        for i in range(length):
            if i < length-1:
                string += names[i] + ", "
            elif i == length-1:
                string += "and " + names[i]
    print(f"Adieu, adieu, to {string}")

if __name__ == "__main__":
    main()




