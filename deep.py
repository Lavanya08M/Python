def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    
    if is_correct(answer):
        print("Yes")
    else:
        print("No")

def is_correct(ans):
    match ans:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False

if __name__ == "__main__":
    main()