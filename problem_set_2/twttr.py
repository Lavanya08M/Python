def main():
    # Ask the user to enter the word
    text = input("Input: ")
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in text:
        if i in vowels: # check if character in text is vowel
            text = text.replace(i,"") # replace vowel with empty string
    print(f"Output: {text}")
if __name__ == "__main__":
    main()