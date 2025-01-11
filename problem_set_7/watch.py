import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r"https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)"
    match = re.search(pattern, s, re.IGNORECASE)
    if match:
        return f"https://youtu.be/{match.group(1)}"

if __name__ == "__main__":
    main()