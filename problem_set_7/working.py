import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("Invalid time")

def convert(s):
    pattern = r"(?P<time1>(?:[1-9]|1[0-2]):?(?:[0-5][0-9])?) (?P<meridiem1>AM|PM) to (?P<time2>([1-9]|1[0-2]):?([0-5][0-9])?) (?P<meridiem2>AM|PM)"
    match = re.search(pattern, s)
    if match:
        time1 = match.group("time1")
        meridiem1 = match.group("meridiem1")
        time2 = match.group("time2")
        meridiem2 = match.group("meridiem2")

        if ":" in time1:
            hour, minutes = time1.split(":")
            time1 = convert_to_24(meridiem1, hour, minutes)
        else:
            time1 = convert_to_24(meridiem1, time1)
        if ":" in time2:
            hour, minutes = time2.split(":")
            time2 = convert_to_24(meridiem2, hour, minutes)
        else:
            time2 = convert_to_24(meridiem2, time2)
        
        return f"{time1} to {time2}"
    raise ValueError


def convert_to_24(meridiem, hour, minutes="00"):
    hour = int(hour)
    if meridiem == 'PM' and 1 <= hour <= 11:
        hour += 12
    elif meridiem == 'AM' and 12 <= hour < 1:
            hour -= 12
    
    if 1 <= hour <= 9:
        return f"0{hour}:{minutes}"
    return f"{hour}:{minutes}"


if __name__ == "__main__":
    main()