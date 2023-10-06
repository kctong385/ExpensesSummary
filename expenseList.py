import csv
import pandas as pd
from expense import Expense
from tabulate import tabulate

class ExpenseList:
    stored_list = []


    def add(self):
        self.stored_list.append(Expense.create())
        self.sort_list()


    def amend(self):
        try:
            index = int(input("Input index of expense to be amended: "))
            if index >= len(self.stored_list):
                print("Invalid index")
                return False
        except ValueError:
            print("Invalid index")
            return False
        else:
            while True:
                field = input("Input field to be amended or back: ").lower()
                match field:
                    case "date" | "category" | "description" | "amount":
                        try:
                            self.stored_list[index].amend(field)
                        except ValueError:
                            print("Invalid input")

                    case "back":
                        self.sort_list()
                        break

                    case _:
                        print("Fields: date/category/description/amount")


    def append_to_file(self, file_name):
        with open(file_name, "a") as file:
            writer = csv.DictWriter(file, fieldnames=Expense.FIELD)
            for expense in self.stored_list:
                writer.writerow({"date": expense.date, "category": expense.category, "description": expense.description, "amount": expense.amount})


    def delete(self):
        try:
            index = int(input("Input index of expense to be deleted: "))
            if index >= len(self.stored_list):
                print("Invalid index")
                return False
        except ValueError:
            print("Invalid index")
            return False
        else:
            self.stored_list.pop(index)


    def load(self, file_name):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.stored_list.append(Expense(row["date"], row["category"], row["description"], row["amount"]))

        self.sort_list()


    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            writer = csv.DictWriter(file, fieldnames=Expense.FIELD)
            writer.writeheader()
            for expense in self.stored_list:
                writer.writerow({"date": expense.date, "category": expense.category, "description": expense.description, "amount": expense.amount})


    def sort_list(self):
        self.stored_list = sorted(self.stored_list, key=lambda expense: expense.date)


    def summarize(self):
        expenses = {"Date": [], "Category": [], "Description": [], "Amount": []}

        for expense in self.stored_list:
            expenses["Date"].append(expense.date)
            expenses["Category"].append(expense.category)
            expenses["Description"].append(expense.description)
            expenses["Amount"].append(expense.amount)

        df = pd.DataFrame(expenses)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Month_Year"] = df["Date"].dt.strftime("%m-%y")

        pivot_table = pd.pivot_table(df, values="Amount", index="Month_Year", columns="Category", aggfunc="sum", fill_value=0)
        pivot_table["Total"] = pivot_table.sum(axis=1)
        pivot_table = pivot_table.reindex(sorted(pivot_table.index, key=lambda x: pd.to_datetime(x, format="%m-%y")))

        return pivot_table


    def tabulate_pivot(self):
        return tabulate(self.summarize(), headers="keys", tablefmt="psql")


    def tabulate_list(self):
        table = []

        for expense in self.stored_list:
            table.append([expense.date, expense.category.capitalize(), \
                        expense.description, f"{'{:,.2f}'.format(expense.amount)}"])

        table_headers = [x.capitalize() for x in Expense.FIELD]
        table_headers.insert(0, "Index")

        return tabulate(table, headers=table_headers, tablefmt="psql", \
                        colalign=("left","left","left","left","right"), showindex="always")
