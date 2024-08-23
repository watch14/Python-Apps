from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

content  = pd.read_csv("topics.csv")

for index, item in content.iterrows():
    for i in range(item["Pages"]):
        print(i)
        pdf.add_page()

        text = item["Topic"]
        pdf.set_font("Arial", size=20, style="B")
        pdf.cell(0, 12, txt=text, ln=1, align="L")
        pdf.line(10, 22, 200, 22)


pdf.output("test.pdf")
