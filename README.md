# EXPENSES SUMMARY
#### Video Demo: <URL https://youtu.be/xijJA5Eni2Q>
#### Description:
##### **Overview**
Expenses Summary is a command line app that stores user's expenses log data and report it back as a pivot table summary.

The program consists of serveral files.

###### project.py
It define the main structure of the program. It facilitates user to use command line argurements to input csv file name for loacing expenses into the program. After entering the program, it takes following commands from user inpput for the next action.

    - add
        To manually input an additional expense and add into stored expenses list.

    - amend
        To revise a particular entry in the stored expenses list.

    - append
        To append the stored expenses list to an existing csv file.

    - delete
        To delete a particular entry in the stored expenses list.

    - export
        To export the summary pivot table and expenses list to a report in pdf format.

    - help
        To display help, which is a complete list of all command and their descriptions.

    - list
        To list out the stored expenses list in tabulated format.

    - load
        To load expenses data from a csv file and append to the stored expenses list.

    - pivot
        To display the monthly expenses summary pivot table categorized by expenses categories.

    - quit
        To exit the program.

    - save
        To save the stored expenses list into a new csv file.

If user input invalid command, it will promt the user to input again.


###### expense.py
It defines the Expense class which consists of attributes "date", "category", "description" and "amount". The class also consists of methods "amend" and "create" for developers to amend an existing expense ot generate a new expense. Both methods utilize individual methods to prompt user until valid value for each attribute was input. Input verification is carried out in setter of each attribute.

It also defines the output for printing Expense class instance.

###### expenseList.py
It define the ExpenseList class which consists of a list of expenses and methods to manipulate the stored list.

Method includes:
    - add
        As described in project.py.
    - amend
        As described in project.py.
    - append_to_file
        As described in project.py.
    - delete
        As described in project.py.
    - load
        As described in project.py.
    - save_to_file
        As described in project.py.
    - sort_list
        To sort the latest stored list by expense date.
    - summarize
        To summarize the latest list into categorized mothly pivot table and return the pivot table.

###### export.py
It writes summary pivot table and the expenses list into a pdf file, formated to desired style.


###### helper.py
It contain a few general use funcitions.
    - check_date_input
        To validate if the user input date is in desired format utilizing regex.

    - isfloat
        To validate if the user input is a float.

    - isint
        To validate if the user input is an int.


