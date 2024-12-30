def main():
    # Amount due for each coca-cola 
    amount_due = 50

    # Total amount inserted by user
    total_amount_inserted = 0

    while True:
        try:
            if amount_due > 0: # check the condition if due amount > 0
                # print the due amount
                print(f"Amount Due: {amount_due}")

                # ask the user to insert coin
                insert_coin = int(input("Insert Coin:"))

                # accept only 25, 10, 5 cents
                if insert_coin in [25, 10, 5]:
                    amount_due -= insert_coin
                    total_amount_inserted += insert_coin
            elif amount_due <= 0: # if due amount  <= 0 then print chnage and break the loop
                change = total_amount_inserted - 50
                print(f"Change Owed: {change}")
                break
        # if coin inserted is not an integer then ignore it and continue 
        except ValueError: 
            continue

if __name__ == "__main__":
    main()