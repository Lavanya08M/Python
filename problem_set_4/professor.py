import sys
import random

def main():
    score = 0
    level = get_level()
    for i in range(1, 11):
        x, y = generate_integer(level)
        count = 0
        for i in range(1, 4):
            print(f"{x} + {y} = ", end="")
            try:
                result = int(input())
                if result == x+y:
                    score += 1
                    break
                raise ValueError
            except ValueError:
                print("EEE")
                count += 1
                if count == 3:
                    print(f"{x} + {y} = {x+y}")
                    break


    print(f"Score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
            continue
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y



if __name__ == "__main__":
    main()