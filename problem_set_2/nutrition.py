def main():
    # Prompt the user for a food item and convert it to lowercase for case-insensitive matching.
    food_item = input("Item: ").lower()
    
    # Dictionary containing food items as keys and their corresponding calorie values as values.
    foods_and_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    
    # Iterate over each key-value pair in the dictionary.
    for key, value in foods_and_calories.items():
        # If user's input matches a key in the dictionary, print corresponding calorie value.
        if food_item == key:
            print(f"Calories: {value}")

if __name__ == "__main__":
    main()