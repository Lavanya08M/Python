def main():
    while True:
        try:
            # Prompt user for a fraction
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/')) # split and convert to integers
            percentage = round((x / y) * 100)

            # output based on the percentage
            if 0 <= percentage <= 1:
                print("E")
            elif 99 <= percentage <= 100:
                print("F")
            elif 1 < percentage < 99:
                print(f"{percentage}%")
            else:
                continue # if percentage is not between 0 and 100 continue
            break # Exit loop if input is valid and output is given
        except (ValueError, ZeroDivisionError):
            # Handle invalid input or division by zero and re-prompt
            pass
        except EOFError:
            break
        


if __name__ == "__main__":
    main()