import csv
from tabulate import tabulate
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            file_path = sys.argv[1].strip()
            if file_path.endswith(".csv"):
                table_format(file_path)
            else:
                sys.exit("Not a csv file.")      
    except FileNotFoundError:
        sys.exit("File not found")

def table_format(file_path):
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        print(tabulate(reader,headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()