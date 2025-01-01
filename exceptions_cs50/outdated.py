def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    while True:
        try:
            date = input("Date: ")
            if date.count('/') == 2:
                final_date = date.split("/")
                final_date = list(map(int, final_date))                    
            elif date.count(' ') == 2:
                final_date = date.split(" ")
                if final_date[0].capitalize() in months.keys():
                    final_date[1] = final_date[1].removesuffix(',')
                    final_date[0] = months[final_date[0].capitalize()]
                    final_date = list(map(int, final_date))

            if len(final_date) == 3 and 1<=final_date[0]<=12 and 1<=final_date[1]<31 and len(str(final_date[2])) == 4:
                print(f"{final_date[2]}-{final_date[0]:02}-{final_date[1]:02}")
                break

            continue
        except (ValueError, TypeError):
            pass
        except EOFError:
            break
        

if __name__ == "__main__":
    main()
