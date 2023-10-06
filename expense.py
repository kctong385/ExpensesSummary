import datetime
from helper import check_date_format, isfloat, isint

class Expense:
    CATEGORY = [
        "food",
        "utilities",
        "travel",
        "housing",
        "living",
        "leisure",
        ]

    FIELD = [
        "date",
        "category",
        "description",
        "amount",
        ]

    # To add attributes "date", "category", "description", "amount"
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


    def __str__(self):
        return f"Date: {self.date}    Category: {self.category}    \
            Description: {self.description}   Amount: ${'{:,.2f}'.format(self.amount)}"



    def amend(self, field):
        match field:
            case "date":
                self.date = self.input_date()
            case "category":
                self.category = self.input_category()
            case "description":
                self.description = self.input_description()
            case "amount":
                self.amount = self.input_amount()
        return self


    @classmethod
    def create(cls):
        date = cls.input_date()
        category = cls.input_category()
        description = cls.input_description()
        amount = cls.input_amount()
        return cls(date, category, description, amount)

    @classmethod
    def input_category(cls):
        category = ""   # declare category in advance for while loop criteria
        help_text = ""

        for cat in cls.CATEGORY:
            help_text += cat.capitalize()
            help_text += "/"

        while not category in cls.CATEGORY:
            category = input(f"Category ({help_text.rstrip('/')}): ").lower()
        return category


    @staticmethod
    def input_date():
        date = ""
        while not check_date_format(date):
            date = input("Date (YYYY-MM-DD): ")
        return date

    @staticmethod
    def input_description():
        description = ""
        while description == "":
            description = input("Description: ")
        return description

    @staticmethod
    def input_amount():
        amount = ""
        while not isfloat(amount):
            amount = input("Amount: ")
        return amount


    #Getter for date
    @property
    def date(self):
        return self._date

    #Setter for date
    @date.setter
    def date(self, date):
        year, month, day = date.split("-")

        if isint(year) and isint(month) and isint(day):
            self._date = datetime.date(int(year), int(month), int(day))
        else:
            raise ValueError("Invalid date")



    #Getter for category
    @property
    def category(self):
        return self._category

    #Setter for category
    @category.setter
    def category(self, category):
        if category not in self.CATEGORY:
            raise ValueError("Invalid category")
        else:
            self._category = category


    #Getter for description
    @property
    def description(self):
        return self._description

    #Setter for description
    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Invalid input")
        else:
            self._description = description


    #Getter for amount
    @property
    def amount(self):
        return self._amount

    #Setter for amount
    @amount.setter
    def amount(self, amount):
        if isfloat(amount):
            self._amount = round(float(amount), 2)
        else:
            raise ValueError("Invalid amount")

