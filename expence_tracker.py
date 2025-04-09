from expence import Expense

def main ():
    print(f"running expence tracker")
    expense_file_path = "expenses.csv"
# get user input for expence
    expense=get_user_expense()
   
# write their epence to a file
    save_expense_to_file(expense_file_path)
# read files and summarise expences.
    summarize_expenses(expense_file_path)


def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter Expense name:")
    expense_ammount = float(input("Enter Expense Ammount:"))

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

        if selected_index in range (len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, ammount=expense_ammount
                                  )
            return new_expense
            
        else:
            print("Invalid Category please try again !")

        break

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expences:{expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.ammount}, {expense.category}\n")

def summarize_expenses():
    print(f"Summarise User Expenses")
    

if __name__ =="__main__":
    main()
print("work done")
