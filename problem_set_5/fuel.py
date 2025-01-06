def main():
    while True:
        try:
            # Prompt user for a fraction
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            string = gauge(percentage)
            print(string)
            break # Exit loop if input is valid and output is given
        except (ValueError, ZeroDivisionError):
            pass
        except EOFError:
            break
def convert(fraction):
    x, y = map(int, fraction.split('/')) # split and convert to integers
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage):
    string = ""
    # output based on the percentage
    if percentage <= 1:
        string = "E"
    elif 99 <= percentage <= 100:
        string = "F"
    else:
        string = f"{percentage}%"

    return string


if __name__ == "__main__":
    main()
