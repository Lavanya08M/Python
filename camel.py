def main():
    # Ask the user for the name of a variable in camel case
    camelCase = input("camelCase: ")

    # list to store indices
    list_of_indices = []

    # loop through each letter of camelCase
    for i in range(len(camelCase)):
        # if character in camelCase is in upper case then append the index
        if camelCase[i].isupper():
            list_of_indices.append(i)

    # Insert 0 at starting of list (string start with 0 index)
    list_of_indices.insert(0, 0)

    # Append length of camelCase string
    list_of_indices.append(len(camelCase))

    # list to store words
    list_of_words = []

    # loop through each index of list of indices
    for i in range(len(list_of_indices)):
        # if element of list of indices is 0 then slice the string "[:end_index]"
        if list_of_indices[i] == 0:
            list_of_words.append(camelCase[:list_of_indices[i+1]])
        # if element of list of indices is length of string then break the loop
        elif list_of_indices[i] == len(camelCase):
            break
        # ortherwise creat the word by slicing the string "[start_index:end_index]"
        else:
            list_of_words.append(camelCase[list_of_indices[i]:list_of_indices[i+1]].lower())

    # create snake case by joining the string elements from the list
    snake_case = '_'.join(list_of_words)

    # print the snake case variable
    print(f"snake_case: {snake_case}")

if __name__ == "__main__":
    main()