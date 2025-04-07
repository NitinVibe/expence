def main ():
    print(f"running expence tracker")
    
# get user input for expence
    get_user_expence()

# write their epence to a file
    save_expence_to_file()
# read files and summarise expences.
    summarize_expences()


def get_user_expence():
    print(f"Getting User Expence")
    expense_name = input("Enter Expence name:")
    expense_ammount = float(input("Enter Expence Ammount:"))
    print(f"you'r entered {expense_name}, {expense_ammount}")

    expense_category = [
        "🍟food",
        "🏠home", 
        "🏢work", 
        "🎉fun", 
        "✨misc"
    ]
    while True:
        print("Select Category:")
        for i, category_name in enumerate(expense_category):
            print(f"{i+1}. {category_name}")
        value_range = f"[1-{len(expense_category)}]"
        selected_index = int(input(f"enter a category number{value_range}:")) -1

        break

def save_expence_to_file():
    print(f"Saving User Expences")
    

def summarize_expences():
    print(f"Summarise User Expences")
    

if __name__ =="__main__":
    main()
print("work done")
