import calendar as cldr
from fpdf import FPDF
import pandas as pd


class PDF(FPDF):
    def header(self):
        self.set_margin(10)
        self.set_font("helvetica", size=20)
        self.set_fill_color(50, 50, 100)
        self.ln(10)
        self.cell(w=0, h=10, new_x="START", new_y="NEXT", \
                  txt="CS50P Final Project - Expenses Summary", align="C", \
                  border=0, fill=False)
        self.ln(0)
        self.cell(w=0, h=10, new_x="START", new_y="NEXT", \
                  txt="by TONG KA CHUN", align="C", \
                  border=0, fill=False)
        self.ln(10)


def export_pdf(expenses_list, pivot_table):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", size=30)

    pdf.cell(w=0, h=15, new_x="START", new_y="NEXT", \
              txt="Report", align="C", \
              border=0, fill=False)
    pdf.ln(5)

    pdf.set_font("helvetica", size=15)

    # Pivot summary
    pivot_df = pd.DataFrame(pivot_table.to_records())
    table1_data = df_to_table(pivot_df)

    # define columns alignment
    col_alignment_1 = []
    for index in pivot_df.columns:
        if index == 0:
            col_alignment_1.append("LEFT")
        else:
            col_alignment_1.append("RIGHT")

    # print table title
    pdf.cell(w=0, h=10, new_x="START", new_y="NEXT", \
             txt="Monthly Expenses Summary", align="L", border=0)

    # print table
    with pdf.table() as table1:
        print_table(table1, table1_data, col_alignment_1)

    # separation
    pdf.cell(w=0, h=10, new_x="START", new_y="NEXT", border=0)

    # Expenses List
    table2_data = list_to_table(expenses_list)

    # define columns alignment
    col_alignment_2 = ["LEFT", "CENTER", "LEFT", "RIGHT"]

    # print table title
    pdf.cell(w=0, h=10, new_x="START", new_y="NEXT", \
             txt="Expenses List", align="L", border=0)

    # print table
    with pdf.table() as table2:
        print_table(table2, table2_data, col_alignment_2)

    pdf.output("report/Expenses_Report.pdf")


def print_table(table, table_data, col_alignment):
    for data_row in table_data:
        row = table.row()
        if table_data.index(data_row) == 0:
            for datum in data_row:
                row.cell(datum, "C")
        else:
            for datum, alignment in zip(data_row, col_alignment):
                row.cell(datum, alignment)
    return True


def df_to_table(pivot_df):
    table_data = []

    data = []
    for col in pivot_df.columns:
        data.append(col.capitalize())

    data[0] = "Month"
    table_data.append(data)

    for index, row in pivot_df.iterrows():
        data = []
        for col in range(len(pivot_df.columns)):
            if col == 0:
                month, year = row[col].split("-")
                text = cldr.month_abbr[int(month)] + "-" + year
                data.append(text)
            else:
                data.append("{:,}".format(row[col]))

        table_data.append(data)

    return table_data


def list_to_table(expenses_list):
    table_data = []
    table_data.append(["Date", "Category", "Description" ,"Amount"])

    for expense in expenses_list:
        table_data.append([
            f"{expense.date.year}-{expense.date.month}-{expense.date.day}",
            expense.category.capitalize(),
            expense.description,
            f"{'{:,.2f}'.format(expense.amount)}"
            ])

    return table_data