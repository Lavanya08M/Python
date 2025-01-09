import csv
import sys

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments.")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments.")
        else:
            input_file_path = sys.argv[1]
            output_file_path = sys.argv[2]
            if not input_file_path.endswith(".csv") or not output_file_path.endswith(".csv"):
                sys.exit("Not a CSV file.")
            else:
                create_new_file(input_file_path, output_file_path)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file_path}.")

def create_new_file(input_file_path, output_file_path):
    with open(input_file_path,"r") as before, open(output_file_path, "w", newline='') as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])

        writer.writeheader()
        for row in reader:
            name = row["name"].split(',')
            writer.writerow({'first':name[1], 'last':name[0], 'house':row['house']})
        

if __name__=="__main__":
    main()

