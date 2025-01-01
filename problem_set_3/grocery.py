def main():
    items_list = []
    items_dict = {}
    while True:
        try:
            user_item = input()
            items_list.append(user_item)
        except EOFError:
            items_list.sort()
            for item in items_list:
                if item in items_dict:
                    items_dict[item] += 1
                else:
                    items_dict[item] = 1
            
            for key in sorted(items_dict.keys()):
                print(f"{items_dict[key]} {key.upper()}")
            break

if __name__ == "__main__":
    main()
            

