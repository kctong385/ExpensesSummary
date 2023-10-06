import csv
import argparse

from datetime import date
from random import randint
from expense import Expense as ex

def main():
    #argparse
    parser = argparse.ArgumentParser(description="Input data file")
    parser.add_argument("-s", help="start date")
    parser.add_argument("-e", help="end date")
    parser.add_argument("-n", help="number of sample")
    args = parser.parse_args()


    if not args.s == None:
        try:
            year, month, day = args.s.split("-")
            start_date = date(int(year), int(month), int(day))
        except ValueError:
            start_date = date(2022, 1, 1)
            print("Input invalid. Default start date = 2022-01-01")
    else:
        start_date = date(2022, 1, 1)
        print("Default start date = 2022-01-01")

    if not args.e == None:
        try:
            year, month, day = args.e.split("-")
            end_date = date(int(year), int(month), int(day))
        except ValueError:
            end_date = date(2023, 12, 31)
            print("Input invalid. Default end date = 2023-12-31")
    else:
        end_date = date(2023, 12, 31)
        print("Default end date = 2023-12-31")

    if not args.n == None:
        try:
            total_sample = int(args.n)
        except ValueError:
            total_sample = 1000
            print("Input invalid. Defult number of sample = 1000")
    else:
        total_sample = 1000
        print("Default number of sample = 1000")


    generated_sample = 0

    expenses_list = []

    # start = date(2022, 1, 1)
    # end = date(2023, 12, 31)
    start = start_date.toordinal()
    end = end_date.toordinal()


    # generate housing & utilities expenses
    monthly = date.fromordinal(start)
    with open("data/sample.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=ex.FIELD)
        while monthly < date.fromordinal(end):
            data = {
                "date": monthly,
                "category": "housing",
                "description": "Rent",
                "amount": 20000,
                }
            if generated_sample < total_sample:
                expenses_list.append(data)
                generated_sample += 1

            data = {
                "date": monthly,
                "category": "utilities",
                "description": "Elec bill",
                "amount": randint(1000, 2000),
                }
            if generated_sample < total_sample:
                expenses_list.append(data)
                generated_sample += 1

            data = {
                "date": monthly,
                "category": "utilities",
                "description": "Gas bill",
                "amount": randint(300, 600),
                }
            if generated_sample < total_sample:
                expenses_list.append(data)
                generated_sample += 1


            data = {
                "date": monthly,
                "category": "utilities",
                "description": "Water bill",
                "amount": randint(150, 300),
                }
            if generated_sample < total_sample:
                expenses_list.append(data)
                generated_sample += 1


            if monthly.month < 12:
                monthly = monthly.replace(month=monthly.month+1)
            else:
                monthly = monthly.replace(month=1, year=monthly.year+1)


    bal_of_sample_tbg = total_sample - generated_sample

    if bal_of_sample_tbg > 0:
        portion = {
            "food": 0.3,
            "travel": 0.3,
            "living": 0.3,
            "leisure": 0.1,
        }

        sample_food = int(bal_of_sample_tbg * portion["food"])
        sample_travel = int(bal_of_sample_tbg * portion["travel"])
        sample_living = int(bal_of_sample_tbg * portion["living"])
        sample_leisure = bal_of_sample_tbg - sample_food - sample_travel - sample_living

        # generate food expenses
        entry_count = sample_food
        max_amount = 500
        description = ["Dinner", "Lunch", "Afternoon tea", "Breakfast", "Snack"]
        expenses_list = genetate_expenses(expenses_list, "food", description, start, end, entry_count, max_amount)


        # generate travel expenses
        entry_count = sample_travel
        max_amount = 200
        description = ["Fuel", "Taxi", "Train", "Metro", "Bus"]
        expenses_list = genetate_expenses(expenses_list, "travel", description, start, end, entry_count, max_amount)


        # generate living expenses
        entry_count = sample_living
        max_amount = 500
        description = ["Groceries", "Clothing", "Home essential", "Home decoration", "Home maintenance"]
        expenses_list = genetate_expenses(expenses_list, "living", description, start, end, entry_count, max_amount)


        # generate leisure expenses
        entry_count = sample_leisure
        max_amount = 500
        description = ["Sports", "Movies", "Concerts", "Games", "Events"]
        expenses_list = genetate_expenses(expenses_list, "leisure", description, start, end, entry_count, max_amount)


    # write header to new data/sample.csv
    with open("data/sample.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=ex.FIELD)
        writer.writeheader()
        for expense in expenses_list:
            writer.writerow({
                "date": expense["date"],
                "category": expense["category"],
                "description": expense["description"],
                "amount": expense["amount"]
                })


def genetate_expenses(stored_list, category, description, start, end, entry_count, max_amount):
    for _ in range(entry_count):
        data = {
            "date": date.fromordinal(randint(start, end)),
            "category": category,
            "description": description[randint(0, len(description) - 1)],
            "amount": randint(20, max_amount)
            }
        stored_list.append(data)

    return sorted(stored_list, key=lambda _: _["date"])


if __name__ == "__main__":
    main()
