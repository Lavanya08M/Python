import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(([1-9]?[0-9]|1[0-9]{1,2}|2[0-5]{1,2})\.){3}([1-9]?[0-9]|1[0-9]{1,2}|2[0-5]{1,2})$"
    match = re.search(pattern, ip)
    if match:
        return True
    return False


if __name__ == "__main__":
    main()


