from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.cell(w=40, h=10, txt="Hello World!", border=1)

pdf.output("test.pdf")