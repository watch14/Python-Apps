from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font("Arial", size=20, style="B")
pdf.cell(0, 12, txt="Hello World!", ln=1, align="L", border=1)
pdf.cell(0, 12, txt="Data", ln=1, align="L", border=1)


pdf.output("test.pdf")
