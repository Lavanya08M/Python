def main():
    # Ask the user to enter the word
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(word):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in word:
        if i in vowels: # check if character in text is vowel
            word = word.replace(i,"") # replace vowel with empty string
    return word
if __name__ == "__main__":
    main()
