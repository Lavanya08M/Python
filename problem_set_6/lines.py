import os
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            file_path = sys.argv[1].strip()
            if file_path.endswith(".py"):
                number_of_lines = check_lines(file_path)
                print(number_of_lines)
            else:
                sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_lines(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            if len(line.strip()) == 0 or line.strip().startswith("#"):
                continue
            else:
                count += 1
    return count
        
if __name__ == "__main__":
    main()


            
                


