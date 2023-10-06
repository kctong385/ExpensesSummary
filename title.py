from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_margin(10)
        self.set_font("helvetica", size=30)
        self.set_fill_color(50, 50, 100)
        self.ln(20)
        self.cell(w=0, h=10, new_x="START", new_y="NEXT", \
                  txt="CS50P Final Project", align="C", \
                  border=0, fill=False)
        self.ln(10)
        self.set_font("helvetica", size=40)
        self.cell(w=0, h=10, new_x="START", new_y="NEXT", \
                  txt="Expenses Summary", align="C", \
                  border=0, fill=False)
        self.ln(10)
        self.set_font("helvetica", size=30)
        self.cell(w=0, h=10, new_x="START", new_y="NEXT", \
                  txt="by TONG KA CHUN", align="C", \
                  border=0, fill=False)
        self.ln(10)
        self.cell(w=0, h=10, new_x="START", new_y="NEXT", \
                  txt="from HONG KONG", align="C", \
                  border=0, fill=False)


def main():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.output("title.pdf")


if __name__ == "__main__":
    main()