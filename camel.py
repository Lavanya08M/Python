def main():
    camelCase = input("camelCase: ")
    start = 0
    list_of_indices = []
    count_capital = 0

    for i in range(len(camelCase)):
        if camelCase[i].isupper():
            count_capital += 1
            list_of_indices.append(i)

    list_of_indices.insert(0, 0)
    list_of_indices.append(len(camelCase))

    list_of_words = []
    for i in range(len(list_of_indices)):
        if list_of_indices[i] == 0:
            list_of_words.append(camelCase[:list_of_indices[i+1]])
        elif list_of_indices[i] == len(camelCase):
            break
        else:
            list_of_words.append(camelCase[list_of_indices[i]:list_of_indices[i+1]].lower())

    snake_case = '_'.join(list_of_words)
    print(f"snake_case: {snake_case}")

if __name__ == "__main__":
    main()