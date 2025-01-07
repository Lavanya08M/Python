import os
import sys

def main():
    try:
        check_command_arguments()
        
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_command_arguments():
    if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_path = sys.argv[1].strip()
        if file_path.endswith(".py"):
            print(check_lines(file_path))
        else:
            sys.exit("Not a Python file")

def check_lines(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if len(line) == 0 or line.startswith("#"):
                continue
            else:
                count += 1
    return count
        
if __name__ == "__main__":
    main()


            
                


