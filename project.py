import argparse
import os
import re

from expenseList import ExpenseList
from export import export_pdf


def main():
    #argparse
    parser = argparse.ArgumentParser(description="Input data file")
    parser.add_argument("-f", help="csv file name")
    args = parser.parse_args()

    #To load expenses from csv file or prompt users to input manuelly
    expenses_list = ExpenseList()
    # pivot_table = expenses_list.summarize()

    if not args.f == None:
        try:
            expenses_list.load("data/" + args.f)
        except FileNotFoundError:
            print("No such file or directory")


    while True:
        match input(">"):
            case ".add":
                expenses_list.add()


            case ".amend":
                expenses_list.amend()


            case ".append":
                while True:
                    file_name = "data/" + input("Input file name: ") + ".csv"
                    if os.path.exists(file_name):
                        expenses_list.append_to_file(file_name)
                        break
                    else:
                        print("No such file or directory")


            case ".delete":
                expenses_list.delete()


            case ".export":
                export_pdf(expenses_list.stored_list, expenses_list.summarize())


            case ".help":
                help = "COMMAND:" + "\n" +\
                        "   .add    - Input an expense entry into the current expenses list manually" + "\n" +\
                        "   .amend  - Amend an expense entry in the current expenses list" + "\n" +\
                        "   .apend  - Add current expenses list into an existing csv file" + "\n" +\
                        "   .delete - Delete an expense entry in the current expenses list" + "\n" +\
                        "   .export - Export the summary pivot table and expenses list to a report in pdf format" + "\n" +\
                        "   .help   - Show help" + "\n" +\
                        "   .list   - List out the current expenses list in tabulated format" + "\n" +\
                        "   .load   - Load expense data from a csv file and append to the current expenses list" + "\n" +\
                        "   .pivot  - Print out a pivot summary of the current expenses list" + "\n" +\
                        "   .quit   - Exit the program" + "\n" +\
                        "   .save   - save current expenses list to a new csv file"

                print(help)


            case ".list":
                print(expenses_list.tabulate_list())
                print()


            case ".load":
                try:
                    file_name = "data/" + input("Input csv file name: ") + ".csv"
                    expenses_list.load(file_name)

                except FileNotFoundError:
                    print("No such file or directory")


            case ".pivot":
                # print summary pivot table
                print(expenses_list.tabulate_pivot(), "\n")


            case ".quit":
                break


            case ".save":
                    saved = False
                    while not saved:
                        file_name = "data/" + input("Input file name: ") + ".csv"
                        if not os.path.exists(file_name):
                            expenses_list.save_to_file(file_name)
                            saved = True
                        else:
                            while True:
                                match input("File already exist. Do you want to overwrite? (Y/N): ").lower():
                                    case "y":
                                        expenses_list.save_to_file(file_name)
                                        saved = True
                                        break

                                    case "n":
                                        break

                                    case _:
                                        print("Invalid input")


            case _:
                print("Invalid command\n")
                print_help()

    print("\n- END -\n")
    return 0


def save(expenses_list):
    while True:
        file_name = "data/" + input("Input file name: ") + ".csv"
        if not os.path.exists(file_name):
            expenses_list.save_to_file(file_name)
            return
        else:
            while True:
                match input("File already exist. Do you want to overwrite? (Y/N): ").lower():
                    case "y":
                        expenses_list.save_to_file(file_name)
                        return

                    case "n":
                        break

                    case _:
                        print("Invalid input")


def check_date_format(text):
    if re.search(r"^[1|2]\d{3}-(0[1-9]|11|12)-(0[1-9]|[1-2]\d|30|31)$", text):
        return True
    else:
        return False


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()