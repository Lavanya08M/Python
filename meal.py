"""
# 24-hour clock

def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    

    if 7 <= time <= 8:
        print("Breakfast Time")
    elif 12 <= time <= 13:
        print("Lunch Time")
    elif 18 <= time <= 19:
        print("Dinner Time")


def convert(tm):
    time_list = tm.split(":")
    time_list[1] = round(int(time_list[1]) / 60, 2)
    time = int(time_list[0]) + time_list[1]

    return float(time)

if __name__ == "__main__":
    main()


"""

"""
12-hour clock
"""
def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    

    if 7 <= time <= 8:
        print("Breakfast Time")
    elif 12 <= time <= 13:
        print("Lunch Time")
    elif 18 <= time <= 19:
        print("Dinner Time")


def convert(tm):
    if tm.endswith("a.m."):
        tm = tm.removesuffix(" a.m.")
        tm_list = tm.split(":")
        tm_list[1] = round(int(tm_list[1])/60, 2)
        if int(tm_list[0]) == 12:
            time = tm_list[1]
        else:
            time = int(tm_list[0]) + tm_list[1]
    elif tm.endswith("p.m."):
        tm = tm.removesuffix(" p.m.")
        tm_list = tm.split(":")
        tm_list[1] = round(int(tm_list[1])/60, 2)
        if int(tm_list[0]) == 12:
            time = int(tm_list[0]) + tm_list[1]
        else:
            time = 12 + int(tm_list[0]) + tm_list[1]

    return float(time)

if __name__ == "__main__":
    main()

    


    