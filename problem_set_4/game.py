import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level < 0:
                continue
            random_number = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: ").strip())
                    if guess < 0:
                        continue
                    elif 1 <= guess < random_number:
                        print("Too small!")
                    elif random_number < guess <= level:
                        print("Too large!")
                    elif guess == random_number:
                        print("Just right!")
                        sys.exit()
                    else:
                        print(f"Please guess number within range of 1 <= guess <= {level} only.")
                except ValueError:
                    pass
        except ValueError:
            pass

if __name__ == "__main__":
    main()

        
